import React from "react";
import './Network.css'

const Network = () =>{


    return(
        <>
      
   
        <div className="network-form">
       
        <br></br>
        <h1>Join our network of hospitals</h1>
        <br></br>
        <form action="http://localhost:5000" method="POST">
        <label for="name">Hospital Name:</label><br></br>
        <input type="text" id="hospital_name" name="name" required/><br></br>
        
        <label for="name">City:</label><br></br>
        <input type="text" id="city" name="name" required/><br></br>
        
        <label for="name">Country:</label><br></br>
        <input type="text" id="country" name="name" required/><br></br>

        <label for="name">Campaign Name:</label><br></br>
        <input type="text" id="name" name="name" required/><br></br>
        
        <label for="quantity">Pledge Amount: </label>
        <input type="number" id="pledge_amount" name="quantity" min="5" max="2147483648"/><br></br>

        <label for="message">Campaign Description:</label><br></br>
        <textarea id="description" name="message" rows="4" cols="50" required></textarea><br></br>
        <label for="start">Start date:</label>

        <input type="date" id="start" name="trip-start" value="2024-01-01" min="2024-01-01" max="2200-12-31" /> 
        <label for="start">End date:</label>

        <input type="date" id="end" name="trip-start" value="2024-01-01" min="2024-01-01" max="2200-12-31" /><br></br>

        <label for="email">Email Contact:</label><br></br>
        <input type="email" id="contact_email" name="email" required/><br></br>

        <label for="name">Paypal Username:</label><br></br>
        <input type="text" id="paypal" name="name" required/><br></br>

        <label for="avatar">Upload an image to be used for your mission:</label><br></br>
        <input type="file" id="image-link" name="avatar" accept="image/png, image/jpeg" /><br></br>

        <label for="avatar">Upload a video presenting your mission:</label><br></br>
        <input type="file" id="video-link" name="avatar" accept="image/png, image/jpeg" /><br></br><br></br>
        <input type="submit" value="Submit"/>
        </form>
        </div>
     
    
        </>
    )


}


export default Network;