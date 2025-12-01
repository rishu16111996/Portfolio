import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import type { TankyType } from "../apiServices/api";

type Props = {
  data: TankyType[];
};

export const TankyChart: React.FC<Props> = ({ data }) => {
  return (
    <div className="card h-80">
      <h2 className="text-lg font-semibold mb-3">Tanky Pokémon by type</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="type_name" tick={{ fill: "#cbd5f5", fontSize: 11 }} />
          <YAxis tick={{ fill: "#cbd5f5", fontSize: 11 }} />
          <Tooltip
            contentStyle={{ backgroundColor: "#020617", border: "1px solid #1e293b" }}
          />
          <Bar dataKey="tanky_count" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};
