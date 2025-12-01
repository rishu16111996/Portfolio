import React from "react"

const PokemonList = ({ pokemons }) => {
  if (!pokemons || pokemons.length === 0) {
    return <p>Loading Pokémon...</p>
  }

  return (
    <div>  
      <h2>Original Table of Pokemons</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Type1</th>
            <th>Type2</th>
            <th>HP</th>
            <th>Attack</th>
            <th>Defense</th>
            <th>Special Attack</th>
            <th>Special Defense</th>
            <th>Speed</th>
          </tr>
        </thead>
        <tbody>
            {pokemons.slice(0, 10).map((pokemon) => (
                <tr key={pokemon.id}>
                <td>{pokemon.name}</td>
                <td>{pokemon.type1}</td>
                <td>{pokemon.type2}</td>
                <td>{pokemon.hp}</td>
                <td>{pokemon.attack}</td>
                <td>{pokemon.defense}</td>
                <td>{pokemon.specialAttack}</td>
                <td>{pokemon.specialDefense}</td>
                <td>{pokemon.speed}</td>
                </tr>
            ))}
        </tbody>
      </table>
    </div>
  )
}

export default PokemonList