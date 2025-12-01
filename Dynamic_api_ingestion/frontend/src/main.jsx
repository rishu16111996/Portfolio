import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'

import { createBrowserRouter, RouterProvider } from "react-router-dom"

import { Layout } from "./components/Layout.jsx";
import Home from "./Home.jsx"
import CreateMetadata from './pages/CreateMetadata.jsx';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout/>,
    children: [
      {path: "/"  , element: <Home/>},
      {path: "/createMetadata", element: <CreateMetadata/>}
    ]
  }
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
)