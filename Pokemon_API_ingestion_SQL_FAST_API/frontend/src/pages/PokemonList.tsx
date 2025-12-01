import { useEffect, useState } from "react";
import { api } from "../api/client";
import PokemonCard from "../components/PokemonCard";

export default function PokemonList() {
  const [pokemon, setPokemon] = useState([]);

  useEffect(() => {
    api.get("/pokemon").then(res => setPokemon(res.data));
  }, []);

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6">
      {pokemon.map((p: any) => (
        <PokemonCard key={p.id} name={p.name} id={p.id} />
      ))}
    </div>
  );
}
