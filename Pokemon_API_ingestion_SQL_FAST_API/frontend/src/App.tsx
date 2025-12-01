import React, { useState } from "react";
import { Navbar } from "./components/Navbar";
import { Home } from "./pages/Home";
import { PokemonPage } from "./pages/PokemonPage";
import { TypesPage } from "./pages/TypesPage";
import { TankyPage } from "./pages/TankyPage";
import { RankingsPage } from "./pages/RankingsPage";

export type PageId = "home" | "pokemon" | "types" | "tanky" | "rankings";

const App: React.FC = () => {
  const [page, setPage] = useState<PageId>("home");

  let content: React.ReactNode;
  if (page === "home") content = <Home />;
  else if (page === "pokemon") content = <PokemonPage />;
  else if (page === "types") content = <TypesPage />;
  else if (page === "tanky") content = <TankyPage />;
  else content = <RankingsPage />;

  return (
    <div className="min-h-screen flex flex-col">
      <Navbar current={page} onNavigate={setPage} />
      <main className="flex-1 max-w-6xl mx-auto w-full px-4 py-6">{content}</main>
      <footer className="text-xs text-slate-500 text-center py-4">
        Built with FastAPI · SQLite · React · Tailwind
      </footer>
    </div>
  );
};

export default App;
