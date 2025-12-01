import React, { useEffect, useState } from "react";
import { PokemonTable } from "../components/PokemonTable";
import { fetchPokemon } from "../apiServices/api";
import type { Pokemon } from "../apiServices/api";

export const PokemonPage: React.FC = () => {
  const [pokemon, setPokemon] = useState<Pokemon[]>([]);
  const [loading, setLoading] = useState(true);
  const [typeFilter, setTypeFilter] = useState("");
  const [tankyFilter, setTankyFilter] =
    useState<"all" | "tanky" | "not-tanky">("all");

  useEffect(() => {
    fetchPokemon().then((data) => {
      setPokemon(data);
      setLoading(false);
    });
  }, []);

  if (loading) return <div>Loading…</div>;

  return (
    <div className="p-6">
      {/* FIXED */}
      <PokemonTable data={pokemon} />
    </div>
  );
};
