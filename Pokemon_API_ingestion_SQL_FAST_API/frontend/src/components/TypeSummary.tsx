import React from "react";
import type { TypeCombo } from "../services/api";

type Props = {
  data: TypeCombo[];
};

export const TypeSummary: React.FC<Props> = ({ data }) => (
  <div className="card">
    <h2 className="text-lg font-semibold mb-3">Type combinations</h2>
    <div className="space-y-1 text-sm max-h-80 overflow-y-auto">
      {data.map((row) => (
        <div
          key={row.type_combo}
          className="flex justify-between items-center border-b border-slate-900/70 pb-1 last:border-0"
        >
          <span className="capitalize">{row.type_combo}</span>
          <span className="font-mono text-emerald-300">{row.count}</span>
        </div>
      ))}
    </div>
  </div>
);
