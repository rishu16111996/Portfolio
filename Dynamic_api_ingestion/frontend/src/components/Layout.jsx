import React from "react";
import { Outlet, Link, useLocation } from "react-router-dom";

export function Layout() {
  const location = useLocation();

  return (
    <div className="app-layout">
      <header className="app-header">
        <div className="header-content">
          <nav>
            <Link
              to="/"
              className={location.pathname === "/" ? "active" : ""}>
              Home
            </Link>
            <Link
              to="/createMetadata"
              className={location.pathname === "/createMetadata" ? "active" : ""}>
              Create Metadata
            </Link>
          </nav>
        </div>
      </header>

      <main>
        <Outlet />
      </main>
    </div>
  );
}
