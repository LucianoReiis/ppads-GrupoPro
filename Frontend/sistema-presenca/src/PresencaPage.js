import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import aluno from './aluno.jpg'


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
      <div>
        <div className='aluno'><img src='{aluno}'></img></div>
      <h4>Aluno: Luciano Teste</h4>
      <p>Matéria: Matemática</p>
      <p>Turma: A1</p>
      <p>Aula: 1 de 10</p>
      <div><h2>Esteve Presente na Aula?</h2></div>
      </div>
    </div>
  );
};

export default PresencaPage;
