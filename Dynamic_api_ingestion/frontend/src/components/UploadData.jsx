import { useState } from "react";
import LoadingOverlay from "./LoadingOverlay";

const UploadData = ({ refreshPokemons }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const uploadData = async () => {
    if (!selectedFile) {
      alert("Please select a file first!");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      let output = typeof data.data === "string" ? data.data : JSON.stringify(data, null, 2);
      alert(output);
      refreshPokemons();
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Upload failed. Check console for details.");
    } finally {
      setLoading(false);
      setSelectedFile(null);
    }
  };

  return (
    <div style={{ display: "flex", gap: "10px", alignItems: "center" }}>
      <input
        type="file"
        onChange={handleFileChange}
        style={{
          padding: "8px",
          border: "1px solid #ccc",
          borderRadius: "5px",
          cursor: "pointer"
        }}
      />
      <button type="button" onClick={uploadData}>Upload Data</button>

      {loading && <LoadingOverlay message="Uploading file..." />}
    </div>
  );
};

export default UploadData;
