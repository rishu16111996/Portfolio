import { useState } from "react";
import GenerateData from "../components/GenerateData";

// Default Pokémon schema
const DEFAULT_POKEMON_SCHEMA = `
id: int primary_key,
name: string unique,
type1: string,
type2: string nullable,
hp: int,
attack: int,
defense: int,
special_attack: int,
special_defense: int,
speed: int
`;

const CreateMetadata = () => {
    const [metadata, setMetadata] = useState("");
    const [className, setClassName] = useState("MyModel"); // DYNAMIC model
    const [responseMessage, setResponseMessage] = useState("Response will appear here...");
    const [showGenerator, setShowGenerator] = useState(false);

    const onSubmit = async (e) => {
        e.preventDefault();

        if (!metadata.trim()) {
            alert("Please enter a schema before submitting!");
            return;
        }

        if (!className.trim()) {
            alert("Please enter a class name.");
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:5000/createMetadata", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    className,
                    schema: metadata,
                }),
            });

            const data = await response.json();
            setResponseMessage(JSON.stringify(data, null, 2));

        } catch (error) {
            console.error("Submit error:", error);
            setResponseMessage(`Error: ${error.message}`);
        }
    };


    const onDefault = async () => {
        try {
            const response = await fetch("http://127.0.0.1:5000/setdefault", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    className: "Pokemon",
                    schema: DEFAULT_POKEMON_SCHEMA,
                }),
            });

            const data = await response.json();
            setResponseMessage(JSON.stringify(data, null, 2));

        } catch (error) {
            console.error("Default Error:", error);
            setResponseMessage(`Error: ${error.message}`);
        }
    };


    const handleResetDatabase = async () => {
        const confirmReset = window.confirm(
            "This will delete ALL tables and data. Are you sure?"
        );
        if (!confirmReset) return;

        try {
            const res = await fetch("http://127.0.0.1:5000/reset-db", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
            });

            const data = await res.json();

            if (!res.ok || !data.ok) {
                alert("Reset failed: " + (data.message || "Unknown error"));
                return;
            }

            alert(data.message || "Database reset successfully!");
        } catch (err) {
            console.error("Reset error:", err);
            alert("Network error while resetting database");
        }
    };


    return (
        <div style={{ padding: "20px" }}>
            <h2>Create Metadata Schema</h2>

            {/* Model Name Input */}
            <div style={{ marginBottom: "10px" }}>
                <label
                    htmlFor="className"
                    style={{ display: "block", marginBottom: "5px", fontWeight: "bold" }}
                >
                    Model / Table Name:
                </label>
                <input
                    id="className"
                    type="text"
                    value={className}
                    onChange={(e) => setClassName(e.target.value)}
                    placeholder="Example: HPCharacters"
                    style={{
                        width: "100%",
                        padding: "8px",
                        borderRadius: "5px",
                        border: "1px solid #ccc",
                        marginBottom: "15px",
                        fontSize: "14px",
                    }}
                />
            </div>

            {/* Metadata Input */}
            <form onSubmit={onSubmit}>
                <div style={{ marginBottom: "10px" }}>
                    <label
                        htmlFor="metadata"
                        style={{ display: "block", marginBottom: "5px", fontWeight: "bold" }}
                    >
                        Enter Schema:
                    </label>

                    <p>
                        Example:
                        <br />
                        <code>id: int primary_key, name: string, height: int</code>
                    </p>

                    <textarea
                        id="metadata"
                        value={metadata}
                        onChange={(e) => setMetadata(e.target.value)}
                        placeholder="id: int primary_key, name: string, species: string"
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

                <button type="submit" style={{ marginRight: "10px" }}>
                    Apply Custom Schema
                </button>

                <button type="button" onClick={onDefault} style={{ marginRight: "10px" }}>
                    Load Pokémon Default Schema
                </button>

                <button type="button" onClick={handleResetDatabase}>
                    Reset Entire Database
                </button>
            </form>

            {/* Response Panel */}
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
                    minHeight: "40px",
                    color: "black",
                    fontSize: "14px",
                }}
            >
                {responseMessage}
            </div>

            {/* Show Data Generator */}
            <div style={{ marginTop: "30px" }}>
                <button onClick={() => setShowGenerator(!showGenerator)}>
                    {showGenerator ? "Hide Data Generator" : "Show Data Generator"}
                </button>

                {showGenerator && (
                    <div style={{ marginTop: "20px" }}>
                        <GenerateData modelName={className} />
                    </div>
                )}
            </div>
        </div>
    );
};

export default CreateMetadata;
