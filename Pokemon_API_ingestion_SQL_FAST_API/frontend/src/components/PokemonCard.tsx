interface Props {
  name: string;
  id: number;
}

export default function PokemonCard({ name, id }: Props) {
  return (
    <a
      href={`/pokemon/${id}`}
      className="bg-white shadow-md p-4 rounded-lg hover:shadow-xl transition cursor-pointer"
    >
      <img
        src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${id}.png`}
        alt={name}
        className="mx-auto"
      />
      <h3 className="text-center text-xl font-semibold capitalize">{name}</h3>
    </a>
  );
}
