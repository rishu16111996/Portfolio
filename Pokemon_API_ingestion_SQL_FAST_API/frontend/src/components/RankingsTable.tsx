import React from "react";
import type { Ranking } from "../apiServices/api";

type Props = {
  data: Ranking[];
};

export const RankingsTable: React.FC<Props> = ({ data }) => {
  return (
    <div className="card max-h-[500px] overflow-y-auto">
      <h2 className="text-lg font-semibold mb-3">Rankings by type</h2>
      <table className="min-w-full text-sm">
        <thead className="border-b border-slate-800 text-slate-400">
          <tr>
            <th className="text-left py-1 pr-4">Type</th>
            <th className="text-left py-1 pr-4">Pokémon</th>
            <th className="text-right py-1 pr-4">Total stats</th>
            <th className="text-right py-1 pr-4">Rank</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, idx) => (
            <tr
              key={`${row.type_name}-${row.pokemon_name}-${idx}`}
              className="border-b border-slate-900/60 hover:bg-slate-900/60"
            >
              <td className="py-1 pr-4 capitalize">{row.type_name}</td>
              <td className="py-1 pr-4 capitalize">{row.pokemon_name}</td>
              <td className="py-1 pr-4 text-right">{row.total_stats}</td>
              <td className="py-1 pr-4 text-right">{row.rank_in_type}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
