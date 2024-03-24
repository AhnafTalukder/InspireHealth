import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Link } from "react-router-dom";

import Hero1 from './assets/hero-image-1.jpg'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className="banner">
          <h1>Connecting Hospitals Around The World</h1>
          <p>Use our platform to discover donation campaigns by local hospitals internationally</p>
          <div class="overlay"></div>
      </div>


      <div  className="spotlight">
        <p style={{padding: "30px", fontSize: "30px"}}>Spotlight</p>
        <h5 style={{color:"#cb416b"}}>Women’s History Month:</h5>
        <p>
          Provide a 1000 women with <br></br>
          women’s hygiene products</p>
      </div>

      <div className="donate-hero-panel">
        <img src={Hero1} alt="" />
        <div className="hero-content">
            <h1>Choose from a variety of campaigns to support</h1>
            <br></br>
            <p>Empower hospitals around the world to benefit their local communities. Donate to hospitals in need. You can choose global campaigns, which Inspire Health runs or choose to support a campaign initiated by a local hospital.</p>
            <br></br>
            <button className="button">
              <Link to="/discover">
                 Discover
              </Link>
            </button>
        </div>

      </div>
    </>
  )
}

export default App
