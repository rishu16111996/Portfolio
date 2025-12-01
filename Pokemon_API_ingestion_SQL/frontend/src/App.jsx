import { useState, useEffect } from 'react'
import PokemonList from './components/PokemonList'
import './App.css'
import Query from './components/Query'
import GenerateData from './components/GenerateData'

function App() {
  const [pokemons, setPokemons] = useState([])

  useEffect(() => {
    fetchPokemons()
  }, [])

  const fetchPokemons = async () => {
    const response = await fetch("http://127.0.0.1:5000/pokemons")
    const data = await response.json()
    setPokemons(data.Pokemons)
  }

  return <> <GenerateData refreshPokemons={fetchPokemons} />
  <PokemonList pokemons={pokemons}/>
  <Query/></>
}

export default App
