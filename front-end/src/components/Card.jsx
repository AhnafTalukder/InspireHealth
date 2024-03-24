import React from "react"
import './Card.css'


const Card = (props) =>{

    return(
        <>
            <div className="card-container">
               

                <div  style = {{
                    width: "300px",
                    backgroundImage: `url(${props.image_url})`,
                    backgroundSize:     "cover",                  
                    backgroundRepeat:   "no-repeat",
                    backgroundPosition: "center center"
                }} className="image-container">

                </div>

                <div className="card-content">
                <h1>{props.name}</h1>
                <p>{props.city}, {props.country}</p>
                <p>{props.description}</p>
                <p><span style={{fontSize:"25px"}}>${props.pledge_amount}</span>/month</p>
                
                <button className="button">Donate Now</button>

                </div>
                


            </div>
        
        </>
    )
}

export default Card;