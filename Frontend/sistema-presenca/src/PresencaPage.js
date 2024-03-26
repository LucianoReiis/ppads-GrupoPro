import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';


const PresencaPage = () => {

  const navigate = useNavigate();

  
  

  const myFunction = (id) => {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") === -1) {
        x.className += " w3-show";
        x.previousElementSibling.className += " w3-theme-d1";
    } else { 
        x.className = x.className.replace("w3-show", "");
        x.previousElementSibling.className = 
        x.previousElementSibling.className.replace(" w3-theme-d1", "");
    }
  }

  

  return (
    <div className="w3-container w3-content" style={{maxWidth: "1400px", marginTop: "80px"}}>
      <h1>Teste Index</h1>
      <p>Essa msg deve aparecer! haha...</p>  
    </div>
  );
};

export default PresencaPage;
