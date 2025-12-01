import React from "react";

type Props = {
  current: string;
  onNavigate: (page: string) => void;
};

const items = [
  { id: "home", label: "Home" },
  { id: "pokemon", label: "Pokémon" },
  { id: "types", label: "Types" },
  { id: "rankings", label: "Rankings" },
  { id: "tanky", label: "Tanky" },
];

export const Navbar: React.FC<Props> = ({ current, onNavigate }) => {
  return (
    <nav className="border-b border-slate-800 bg-slate-950/80 backdrop-blur sticky top-0 z-10">
      <div className="max-w-6xl mx-auto flex items-center justify-between px-4 py-3">
        <div className="font-semibold text-lg text-emerald-400">
          PokeAPI SQLite Dashboard
        </div>
        <div className="flex gap-3 text-sm">
          {items.map((item) => (
            <button
              key={item.id}
              onClick={() => onNavigate(item.id)}
              className={`px-3 py-1 rounded-full transition ${
                current === item.id
                  ? "bg-emerald-500 text-slate-950"
                  : "text-slate-300 hover:bg-slate-800"
              }`}
            >
              {item.label}
            </button>
          ))}
        </div>
      </div>
    </nav>
  );
};
