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

      let output =
        typeof data.data === "string"
          ? data.data
          : JSON.stringify(data, null, 2);

      alert(output);

      if (typeof refreshPokemons === "function") {
        refreshPokemons();
      }

    } catch (err) {
      console.error("Error:", err);
      alert("An error occurred while generating data.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        marginTop: "40px",
        gap: "20px",
        padding: "20px",
        width: "100%",
      }}
    >
      {/* API Input + Generate Button */}
      <div
        style={{
          display: "flex",
          gap: "10px",
          alignItems: "center",
          width: "100%",
          justifyContent: "center",
        }}
      >
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
            borderRadius: "5px",
          }}
        />

        <button
          onClick={createData}
          type="button"
          disabled={loading}
          style={{
            padding: "10px 16px",
            borderRadius: "5px",
            fontSize: "16px",
            cursor: "pointer",
            backgroundColor: loading ? "#aaa" : "#007bff",
            color: "white",
            border: "none",
          }}
        >
          {loading ? "Generating..." : "Generate Data"}
        </button>
      </div>

      {/* Upload DB File */}
      <UploadData refreshPokemons={refreshPokemons} />

      {/* Loading overlay */}
      {loading && <LoadingOverlay message="Generating data..." />}
    </div>
  );
};

export default GenerateData;
