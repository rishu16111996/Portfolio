import React from "react";

export const Home: React.FC = () => (
  <div className="grid gap-4 md:grid-cols-2">
    <div className="card">
      <h1 className="text-2xl font-bold mb-2">PokeAPI SQLite Dashboard</h1>
      <p className="text-sm text-slate-300">
        Full-stack project that ingests Generation 1 Pokémon from PokeAPI into a
        normalized SQLite database, then exposes analytics via FastAPI and a React +
        Tailwind UI.
      </p>
      <ul className="mt-3 text-sm list-disc list-inside text-slate-300 space-y-1">
        <li>Data ingestion & normalization</li>
        <li>SQL window functions for stat rankings</li>
        <li>“Tanky” Pokémon labeling logic</li>
        <li>Interactive tables & charts</li>
      </ul>
    </div>
    <div className="card">
      <p className="text-sm text-slate-300">
        Use the navigation above to explore:
      </p>
      <ul className="mt-3 text-sm list-disc list-inside text-slate-300 space-y-1">
        <li>
          <span className="font-semibold">Pokémon</span> – base stats & tanky labels
        </li>
        <li>
          <span className="font-semibold">Types</span> – distinct type combinations
        </li>
        <li>
          <span className="font-semibold">Rankings</span> – stat-based rankings per type
        </li>
        <li>
          <span className="font-semibold">Tanky</span> – which types are the tankiest
        </li>
      </ul>
    </div>
  </div>
);
