import React from 'react'
import ReactDOM from 'react-dom/client'

import App from './App.jsx'
import Discover from './pages/Discover.jsx'
import Network from './pages/Network.jsx'
import Contact from './pages/Contact.jsx'
import About from './pages/About.jsx'
import DetailView from './routes/DetailView.jsx'

import './index.css'
import Layout from './routes/Layout.jsx';
import { BrowserRouter, Route, Routes } from "react-router-dom"

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index={true} element={<App />} />
        </Route>
        <Route path="/discover" element={<Layout />}>
          <Route index={true} element={<Discover />} />
        

        </Route>
        <Route index={false} path="/coinDetails/:id" element={<DetailView />} />
        <Route path="/join-our-network" element={<Layout />}>
          <Route index={true} element={<Network />} />
        </Route>
        <Route path="/about-us" element={<Layout />}>
          <Route index={true} element={<About />} />
        </Route>
        <Route path="/contact-us" element={<Layout />}>
          <Route index={true} element={<Contact />} />
        </Route>
      </Routes>
</BrowserRouter>
  </React.StrictMode>,
)
