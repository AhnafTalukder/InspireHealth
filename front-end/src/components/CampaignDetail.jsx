import React, { Component, useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const CampaignDetail = () =>{

    let params = useParams();
    const [fullDetails, setFullDetails] = useState(null);

    function fetchFromBackend() {
        const apiURL = "http://localhost:5000/get_campaigns?"
        return fetch(apiURL + params.id, {
            options: 'GET',
        })
            .then(response => {return response.json()})
            .then(responseData => {
                console.log(responseData)
                setFullDetails(responseData)
            })
            .catch(error => {
                console.error('There was an error!', error);
            });
    }

    useEffect(() => {

         fetchFromBackend();

      }, [params.id]);


    return(
    <>
 
    </>
    )
}

export default CampaignDetail;

