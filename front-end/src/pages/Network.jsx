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
        <form action="http://127.0.0.1:5000/upload_video" method="POST" encType="multipart/form-data">
        <label for="name">Hospital Name:</label><br></br>
        <input type="text" id="hospital_name" name="hospital_name" required/><br></br>
        
        <label for="name">City:</label><br></br>
        <input type="text" id="city_name" name="city_name" required/><br></br>
        
        <label for="name">Country:</label><br></br>
        <input type="text" id="country_name" name="country_name" required/><br></br>

        <label for="name">Campaign Name:</label><br></br>
        <input type="text" id="campaign_name" name="campaign_name" required/><br></br>
        
        <label for="quantity">Pledge Amount: </label>
        <input type="number" id="pledge_amount" name="pledge_amount" min="5" max="2147483648"/><br></br>

        <label for="message">Campaign Description:</label><br></br>
        <textarea id="description" name="description" rows="4" cols="50" required></textarea><br></br>
        


        <label>
          Start Date:
          <input
            type="date"
            id="start_date"
            name="start_date"
            value={startDate}
            placeholder="DD/MM/YY"
            onChange={(e) => setStartDate(e.target.value)}
          />
        </label>

        <label>
          End Date:
          <input
            type="date"
            id="end_date"
            name="end_date"
            value={endDate}
            placeholder="DD/MM/YY"
            onChange={(e) => setEndDate(e.target.value)}
          />
        </label>
     
        <label for="contact_email">Email Contact:</label><br></br>
        <input type="email" id="contact_email" name="contact_email" required/><br></br>

        <label for="paypal_user">Paypal Username:</label><br></br>
        <input type="text" id="paypal_user" name="paypal_user" required/><br></br>

        <label for="image">Upload an image to be used for your mission:</label><br></br>
        <input type="file" id="image" name="image" accept="image/png" /><br></br>

        <label for="video">Upload a video presenting your mission:</label><br></br>
        <input type="file" id="video" name="video" accept="video/mp4" /><br></br><br></br>
        <input type="submit" value="Submit"/>
        </form>
        </div>
     
    
        </>
    )


}


export default Network;