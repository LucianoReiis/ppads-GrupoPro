import { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Altere para o URL do seu servidor FastAPI

const useTokenAuthentication = () => {
  const [authenticated, setAuthenticated] = useState(false);

  useEffect(() => {
    const checkAuthentication = async () => {
      const accessToken = localStorage.getItem('accessToken');
      if (accessToken) {
        try {
          const response = await axios.get(`${API_URL}/auth/users`, {
            headers: {
              Authorization: `Bearer ${accessToken}`,
            },
          });
          if (response.status === 200) {
            setAuthenticated(true);
          }
        } catch (error) {
          console.error('Authentication failed:', error);
          // Limpar o token de acesso inválido
          localStorage.removeItem('accessToken');
        }
      }
    };

    checkAuthentication();
  }, []);

  const login = async (username, password) => {
    try {
      const data = new URLSearchParams();
      data.append('username', username);
      data.append('password', password);

      const response = await axios.post(`${API_URL}/auth/token`, data, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });

      const { access_token } = response.data;
      localStorage.setItem('accessToken', access_token);
      setAuthenticated(true);
    } catch (error) {
      console.error('Login failed:', error);
      // Verificar se a resposta contém detalhes do erro
      if (error.response && error.response.data) {
        console.error('Error details:', error.response.data);
      }
      throw new Error('Login failed');
    }
  };

  const logout = () => {
    localStorage.removeItem('accessToken');
    setAuthenticated(false);
  };

  return { authenticated, login, logout };
};

export default useTokenAuthentication;
