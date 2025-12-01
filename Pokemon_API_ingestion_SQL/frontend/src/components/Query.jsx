import { useState } from "react";

const Query = () => {
  const [query, setQuery] = useState("");
  const [generatedText, setGeneratedText] = useState("Output will appear here...");

  const onSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      const data = await response.json();

      let output;
      if (typeof data.data === "string") {
        output = data.data.trim().length > 0 ? data.data : "Backend returned empty string.";
      } else {
        output = JSON.stringify(data, null, 2);
      }
      setGeneratedText(output);
    } catch (err) {
      console.error("Submit error:", err);
      setGeneratedText(`Error: ${err.message}`);
    }
  };

  const onGenerate = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
      });
      const data = await response.json();
      
      let output;
      if (typeof data.data === "string") {
        output = data.data.trim().length > 0 ? data.data : "Backend returned empty string.";
      } else {
        output = JSON.stringify(data, null, 2);
      }

      setGeneratedText(output);
    } catch (error) {
      console.error("Fetch error:", error);
      setGeneratedText(`Error: ${error.message}`);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <form onSubmit={onSubmit}>
        <div style={{ marginBottom: "10px" }}>
          <label htmlFor="query" style={{ display: "block", marginBottom: "5px" }}>
            SQL Query:
          </label>
          <textarea
            id="query"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            style={{
              width: "100%",
              height: "120px",
              fontFamily: "monospace",
              fontSize: "14px",
              padding: "8px",
              borderRadius: "5px",
              border: "1px solid #ccc",
            }}
          />
        </div>
        <button type="submit" style={{ marginRight: "10px" }}>Send Query</button>
        <button type="button" onClick={onGenerate}>Generate</button>
      </form>

      <div
        style={{
          marginTop: "20px",
          backgroundColor: "white",
          padding: "15px",
          borderRadius: "8px",
          boxShadow: "0 0 5px rgba(0,0,0,0.1)",
          maxHeight: "300px",
          overflowY: "auto",
          whiteSpace: "pre-wrap",
          fontFamily: "monospace",
          minHeight: "150px",
          color: "black",
          fontSize: "14px",
        }}
      >
        {generatedText ?? "No output."}
      </div>
    </div>
  );
};

export default Query;
