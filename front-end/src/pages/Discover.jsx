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
        "paypal": ""
  
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
                <Card image_url="https://ahiglobal.org/sites/ahiglobal.org/files/field/image/waterloostaff.jpg" name={obj.name} city={obj.city} country={obj.country} description={obj.description} pledge_amount={obj.pledge_amount}/>

            )
            
            )}


        </div>

        
        </>
    )


}


export default Discover;