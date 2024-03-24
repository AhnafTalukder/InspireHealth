import React from "react";
import './Network.css'

import { useState } from "react";

const Network = () =>{

    const [startDate, setStartDate] = useState("");
    const [endDate, setEndDate] = useState("");


    return(
        <>
      
   
        <div className="network-form">
       
        <br></br>
        <h1>Join our network of hospitals</h1>
        <br></br>
        <form action="http://localhost:5000/upload_video" method="POST">
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
        


        <label>
          Start Date:
          <input
            type="date"
            id="start-date"
            name="start-date"
            value={startDate}
            placeholder="DD/MM/YY"
            onChange={(e) => setStartDate(e.target.value)}
          />
        </label>

        <label>
          End Date:
          <input
            type="date"
            id="end-date"
            name="end-date"
            value={endDate}
            placeholder="DD/MM/YY"
            onChange={(e) => setEndDate(e.target.value)}
          />
        </label>
     
        <label for="email">Email Contact:</label><br></br>
        <input type="email" id="contact_email" name="email" required/><br></br>

        <label for="name">Paypal Username:</label><br></br>
        <input type="text" id="paypal" name="name" required/><br></br>

        <label for="avatar">Upload an image to be used for your mission:</label><br></br>
        <input type="file" id="image-link" name="avatar" accept="image/png, image/jpeg" /><br></br>

        <label for="avatar">Upload a video presenting your mission:</label><br></br>
        <input type="file" id="video-link" name="avatar" accept="video/mp4" /><br></br><br></br>
        <input type="submit" value="Submit"/>
        </form>
        </div>
     
    
        </>
    )


}


export default Network;