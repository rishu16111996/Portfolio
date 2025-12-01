import React from "react";
import type { Pokemon } from "../apiServices/api";

type Props = {
  data: Pokemon[];
};

export const PokemonTable: React.FC<Props> = ({ data }) => {
  return (
    <div className="card overflow-x-auto">
      <h2 className="text-lg font-semibold mb-3">Pokémon (Gen 1)</h2>
      <table className="min-w-full text-sm">
        <thead className="border-b border-slate-800 text-slate-400">
          <tr>
            <th className="text-left py-1 pr-4">Name</th>
            <th className="text-left py-1 pr-4">Types</th>
            <th className="text-right py-1 pr-4">HP</th>
            <th className="text-right py-1 pr-4">Atk</th>
            <th className="text-right py-1 pr-4">Def</th>
            <th className="text-right py-1 pr-4">SpA</th>
            <th className="text-right py-1 pr-4">SpD</th>
            <th className="text-right py-1 pr-4">Spe</th>
            <th className="text-center py-1 pr-4">Tanky?</th>
          </tr>
        </thead>
        <tbody>
          {data.map((p) => {
            const safeTypes = Array.isArray(p.types) ? p.types : [];
            return (
              <tr
                key={p.id}
                className="border-b border-slate-900/60 hover:bg-slate-900/60"
              >
                <td className="py-1 pr-4 capitalize">{p.name}</td>
                <td className="py-1 pr-4">
                  {safeTypes.map((t) => (
                    <span
                      key={t}
                      className="inline-flex items-center px-2 py-0.5 rounded-full bg-slate-800 text-xs mr-1 capitalize"
                    >
                      {t}
                    </span>
                  ))}
                </td>
                <td className="py-1 pr-4 text-right">{p.hp}</td>
                <td className="py-1 pr-4 text-right">{p.attack}</td>
                <td className="py-1 pr-4 text-right">{p.defense}</td>
                <td className="py-1 pr-4 text-right">{p.special_attack}</td>
                <td className="py-1 pr-4 text-right">{p.special_defense}</td>
                <td className="py-1 pr-4 text-right">{p.speed}</td>
                <td className="py-1 pr-4 text-center">
                  <span
                    className={`px-2 py-0.5 rounded-full text-xs ${
                      p.tanky_label === "tanky"
                        ? "bg-emerald-500/20 text-emerald-300 border border-emerald-500/30"
                        : "bg-slate-800 text-slate-300"
                    }`}
                  >
                    {p.tanky_label}
                  </span>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};
