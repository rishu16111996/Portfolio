import {useState} from "react"

function ThemeInput({onSubmit}) {
    const [theme, setTheme] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        
        if (!theme.trim()) {
            setError("Theme cannot be empty.");
            return;
        }

        onSubmit(theme);

    }

    return <div className="theme-input-container">
        <h2>Generate Your Story</h2>
        <p>Enter a theme to start your adventure.</p>
        <form onSubmit={handleSubmit}>
            <div className="input-group">
                <input
                    type="text"
                    value={theme}
                    onChange={(e) => setTheme(e.target.value)}
                    placeholder="Enter your Theme"
                    className={error ? 'error': ''}
                />
                {error && <p className="error-text">{error}</p>}
            </div>
            <button type="submit" className='generate-btn'>Generate</button>
        </form>
    </div>
}

export default ThemeInput;
