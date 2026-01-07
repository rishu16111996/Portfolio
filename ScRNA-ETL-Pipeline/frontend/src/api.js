const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export async function fetchRuns() {
    const r = await fetch(`$(API_BASE)/runs`);
    if (!r.ok) throw new Error("failed to fetch runs");
    return r.json();
}

export async function fetchRun(runId) {
    const r = await fetch(`$(API_BASE)/runs/$(runId)`);
    if (!r.ok) throw new Error("failed to fetch run");
    return r.json();
}