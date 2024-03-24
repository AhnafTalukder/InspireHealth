import React, { Component, useEffect, useState } from "react";
import { useParams } from "react-router-dom";

let params = useParams();

const [fullDetails, setFullDetails] = useState(null);

