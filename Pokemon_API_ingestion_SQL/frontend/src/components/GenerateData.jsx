import { useState } from "react";
import LoadingOverlay from "./LoadingOverlay";
import UploadData from "./UploadData";

const GenerateData = ({ refreshPokemons }) => {
  const [query, setQuery] = useState("https://pokeapi.co/api/v2/pokemon/");
  const [loading, setLoading] = useState(false);

  const createData = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:5000/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await response.json();
      let output = typeof data.data === "string" ? data.data : JSON.stringify(data, null, 2);
      alert(output);
      refreshPokemons();
    } catch (err) {
      console.error("Error", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      marginTop: "40px",
      gap: "20px"
    }}>
      {/* Generate Data Section */}
      <div style={{ display: "flex", gap: "10px", alignItems: "center" }}>
        <input
          type="text"
          value={query}
          placeholder="https://pokeapi.co/api/v2/pokemon/"
          onChange={(e) => setQuery(e.target.value)}
          style={{
            width: "400px",
            padding: "10px",
            fontSize: "16px",
            border: "1px solid #ccc",
            borderRadius: "5px"
          }}
        />
        <button onClick={createData} type="button" disabled={loading}>
          {loading ? "Generating..." : "Generate Data"}
        </button>
      </div>
      <UploadData refreshPokemons={refreshPokemons} />

      {loading && <LoadingOverlay message="Generating data..." />}
    </div>
  );
};

export default GenerateData;
