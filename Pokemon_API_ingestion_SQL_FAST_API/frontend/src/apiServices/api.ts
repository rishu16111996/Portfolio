export const API_BASE = "http://localhost:8000/api";

export type Pokemon = {
  id: number;
  name: string;
  types: string[];
  hp: number;
  attack: number;
  defense: number;
  special_attack: number;
  special_defense: number;
  speed: number;
  tanky_label: string;
};

export type TypeCombo = {
  type_combo: string;
  count: number;
};

export type TankyType = {
  type_name: string;
  tanky_count: number;
};

export type Ranking = {
  type_name: string;
  pokemon_name: string;
  total_stats: number;
  rank_in_type: number;
};

export async function fetchPokemon(params?: {
  type?: string;
  tanky?: boolean;
  limit?: number;
}): Promise<Pokemon[]> {
  const url = new URL(`${API_BASE}/pokemon`);
  if (params?.type) url.searchParams.set("type", params.type);
  if (params?.tanky !== undefined)
    url.searchParams.set("tanky", params.tanky ? "true" : "false");
  if (params?.limit) url.searchParams.set("limit", params.limit.toString());
  const res = await fetch(url);
  if (!res.ok) throw new Error("Failed to fetch pokemon");
  return res.json();
}

export async function fetchTypeCombos(): Promise<TypeCombo[]> {
  const res = await fetch(`${API_BASE}/stats/type-combos`);
  if (!res.ok) throw new Error("Failed to fetch");
  return res.json();
}

export async function fetchTankyTypes(): Promise<TankyType[]> {
  const res = await fetch(`${API_BASE}/stats/tanky-types`);
  if (!res.ok) throw new Error("Failed to fetch");
  return res.json();
}

export async function fetchRankings(): Promise<Ranking[]> {
  const res = await fetch(`${API_BASE}/stats/rankings`);
  if (!res.ok) throw new Error("Failed to fetch");
  return res.json();
}
