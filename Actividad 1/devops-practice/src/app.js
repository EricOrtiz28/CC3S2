const express = require('express');  // Importa el módulo Express
const app = express();  // Crea una instancia de la aplicación Express

app.get('/', (req, res) => {  // Define una ruta GET en la raíz
  res.send('Hello, World!');  // Envía una respuesta de texto 'Hello, World!' al cliente
});

const port = process.env.PORT || 3000;  // Define el puerto en el que la aplicación escuchará

const server = app.listen(port, () => {  // Hace que la aplicación escuche en el puerto definido y guarda la referencia al servidor
  console.log(`Server running on port ${port}`);  // Imprime en la consola un mensaje indicando
});

// Exporta la aplicación y el servidor para que puedan ser utilizados en otros módulos, como en pruebas
module.exports = { app, server };