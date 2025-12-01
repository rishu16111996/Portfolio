import React, { useEffect, useState } from "react";
import { TypeSummary } from "../components/TypeSummary";
import { fetchTypeCombos } from "../apiServices/api";
import type { TypeCombo } from "../apiServices/api";

export const TypesPage: React.FC = () => {
  const [data, setData] = useState<TypeCombo[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTypeCombos()
      .then(setData)
      .finally(() => setLoading(false));
  }, []);

  return loading ? (
    <div>Loading…</div>
  ) : (
    <div className="grid md:grid-cols-2 gap-4">
      <TypeSummary data={data} />
    </div>
  );
};

