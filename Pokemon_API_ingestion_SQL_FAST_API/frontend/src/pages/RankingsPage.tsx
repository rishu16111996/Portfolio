import React, { useEffect, useState } from "react";
import { RankingsTable } from "../components/RankingsTable";
import { fetchRankings } from "../apiServices/api";
import type { Ranking } from "../apiServices/api";

export const RankingsPage: React.FC = () => {
  const [data, setData] = useState<Ranking[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchRankings()
      .then(setData)
      .finally(() => setLoading(false));
  }, []);

  return loading ? (
    <div>Loading…</div>
  ) : (
    <RankingsTable data={data} />
  );
};
