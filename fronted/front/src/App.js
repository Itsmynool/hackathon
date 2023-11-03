import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [imageUrl, setImageUrl] = useState('');

  useEffect(() => {
    fetch('http://127.0.0.1:5000/')
      .then((response) => {
        if (!response.ok) {
          throw new Error('La solicitud no fue exitosa');
        }
        return response.json();
      })
      .then((data) => {
        // Extraer la URL del JSON recibido
        const url = data.url;
        console.log('Valor de imageUrl:', url);
        setImageUrl(url);
        console.log('Valor de imageUrl después de setImageUrl:', imageUrl);
      })
      .catch((error) => {
        console.error('Error al obtener la URL:', error);
      });
  }, []);

  return (
    <div className="App">
      {imageUrl ? (
        <div className="img-container">
          <img src={imageUrl} alt="Imagen" className="img-small" />
        </div>
      ) : (
        <p class="loader"></p>
      )}
    </div>
  );
}

export default App;
