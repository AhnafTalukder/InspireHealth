import React, { useInsertionEffect } from "react"
import Card from "../components/Card";
import './Discover.css'


import { useState, useEffect } from "react";


const Discover = () =>{

    

    const [cardInfo, setCardInfo] = useState([{
        "start": "",
        "end": "",
        "name": "",
        "description": "",
        "hospital_name": "",
        "pledge_amount": 0,
        "city": "",
        "country": "",
        "contact_email": "",
        "paypal": "",
        "image_link": "test_image.png",
        "video_link": "test_video.mp4",
        "id": "test_id"
  
    }])
   
    
    function fetchFromBackend() {
        const apiURL = "http://localhost:5000/get_campaigns"
        return fetch(apiURL, {
            options: 'GET',
        })
            .then(response => {return response.json()})
            .then(responseData => {
                setCardInfo(responseData)
    
            })
            .catch(error => {
                console.error('There was an error!', error);
            });
    }
    
    useEffect(() => {
        fetchFromBackend()
    
      }, []);
    


    return(
        <>
        <div className="campaign-list">
            {cardInfo.map((obj, index) =>
            
            (
                
                <Card  image={index === 0 ? "https://cloudfront-us-east-2.images.arcpublishing.com/reuters/ZVUG5DVFY5MH5MNYRVCFXQBL5I.jpg" : "http://localhost:5000/" + obj.image_link} video={"http://localhost:5000/" + obj.video_link} name={obj.name} city={obj.city} country={obj.country} description={obj.description} pledge_amount={obj.pledge_amount} paypal={obj.paypal}/>

            )
            
            )}


        </div>

        
        </>
    )


}


export default Discover;