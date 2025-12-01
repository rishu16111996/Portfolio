import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { api } from "../api/client";

export default function PokemonDetails() {
  const { id } = useParams();
  const [info, setInfo] = useState<any>(null);

  useEffect(() => {
    api.get(`/pokemon/${id}`).then(res => setInfo(res.data));
  }, [id]);

  if (!info) return <h2>Loading…</h2>;

  return (
    <div className="max-w-xl mx-auto bg-white shadow-md p-6 rounded-lg">
      <img
        src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${info.id}.png`}
        className="mx-auto"
      />
      <h2 className="text-3xl font-bold text-center capitalize mt-4">
        {info.name}
      </h2>
      <p className="text-center mt-2 text-gray-700">
        Type(s): {info.types.join(", ")}
      </p>
      <p className="text-center mt-2 text-gray-700">
        Base Exp: {info.base_experience}
      </p>
    </div>
  );
}
