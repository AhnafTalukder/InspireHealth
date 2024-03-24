import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

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
        <p style={{padding: "30px", fontSize: "30px"}}>Spotlights</p>
        <h5 style={{color:"#cb416b"}}>Women’s History Month:</h5>
        <p>
          Provide a 1000 women with <br></br>
          women’s hygiene products</p>
      </div>

      <div className="donate-hero-panel">
        <img src="" alt="" />
        <div className="hero-content">

        </div>

      </div>
    </>
  )
}

export default App
