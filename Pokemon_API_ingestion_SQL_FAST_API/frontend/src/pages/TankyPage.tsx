import React, { useEffect, useState } from "react";
import { TankyChart } from "../components/TankyChart";
import { fetchTankyTypes  } from "../apiServices/api";
import type { TankyType } from "../apiServices/api";

export const TankyPage: React.FC = () => {
  const [data, setData] = useState<TankyType[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTankyTypes()
      .then(setData)
      .finally(() => setLoading(false));
  }, []);

  return loading ? (
    <div>Loading…</div>
  ) : (
    <div className="grid gap-4">
      <TankyChart data={data} />
    </div>
  );
};
