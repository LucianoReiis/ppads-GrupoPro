import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "./App.css";
import useTokenAuthentication from './useTokenAuthentication';
import logo from './logo.png';

const LoginPage = () => {
  const { login } = useTokenAuthentication();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await login(username, password);
      navigate("/presenca");
    } catch (error) {
      console.error('Login failed:', error);
      setErrorMessage('Login failed. Please check your credentials.');
    }
  };

  const togglePassword = () => {
    const passwordField = document.getElementById("password");
    if (passwordField.type === "password") {
      passwordField.type = "text";
    } else {
      passwordField.type = "password";
    }
  };

  return (
    <div className="App">
      <div className="background"></div>
      <div className="login-container">
      <div className="logo">
      <img src={logo} alt="Logo da Escola" />
      </div>
      <h2>Escola Octógno - Sistema de Presença</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="username" id="username" placeholder="Usuário" value={username} onChange={(e) => setUsername(e.target.value)} required />
        <input type="password" name="password" id="password" placeholder="Senha" value={password} onChange={(e) => setPassword(e.target.value)} required />
        <input type="submit" value="Entrar" />
        <input type="checkbox" id="show-password" onClick={togglePassword} />
        <label htmlFor="show-password" className="show-password-label">Mostrar Senha</label>
      </form>
    </div>
  </div>
  );
};

export default LoginPage;
