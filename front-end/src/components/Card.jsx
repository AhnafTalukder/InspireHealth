import React from "react"
import './Card.css'

import { Link } from "react-router-dom"


const Card = (props) =>{

    return(
        <>
            <div className="card-container">
               

                <div  style = {{
                    width: "300px",
                    backgroundImage: `url(${props.image})`,
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
                <p><b>paypal:</b>{props.paypal}</p>
                <button className="button"> 
                    <Link to={props.video}>
                        See Impact
                    </Link>
                </button>

                </div>
                


            </div>
        
        </>
    )
}

export default Card;