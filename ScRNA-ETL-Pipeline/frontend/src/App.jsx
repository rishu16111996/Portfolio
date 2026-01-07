import React, { useEffect, useState } from "react";
import { fetchRuns } from "./api.js";

export default function App() {
    const [runs, setRuns] = useState([]);
    const [err, setErr] = useState("");

    useEffect(() => {
        fetchRuns()
        .then((data) => setRuns(data.items || []))
        .catch((e) => setErr(String(e)));
    }, []);

    return (
        <div style={{ fontFamily: "system-ui", padding: 24, maxWidth: 980, margin: "0 auto" }}>
            <h1>Summary Dashboard</h1>
            <p style={{ color: "#888" }}>
                Shows pipeline runs + key QC metrics by fastAPI backend
            </p>

            {err && <div style={{ color: "red" }}>{err}</div>}

            <div style={{ display: "grid", gap: 12 }}>
                {runs.map((r) => (
                    <div>
                        <div key={r.run_id} style={{ border: "1px solid #333", borderRadius: 12, padding: 16 }}>
                            <strong>{r.run_id}</strong>
                            <span>{r.status || "unkown"}</span>
                        </div>
                        <div style= {{ marginTop: 8, color: "#aaa" }}>
                            sample: {r.sample_id || "n/a"} • cells: {r.cells ?? "n/a"} • median genes/cell: {r.median_genes_cell ?? "n/a"}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}