const express = require('express');  // Importa el módulo Express
const app = express();  // Crea una instancia de la aplicación Express

app.get('/', (req, res) => {  // Define una ruta GET en la raíz
  res.send('Hello, World!');  // Envía una respuesta de texto 'Hello, World!' al cliente
});

const port = process.env.PORT || 3001;  // Define el puerto en el que la aplicación escuchará

// Solo inicia el servidor si el archivo no es requerido por otro módulo (como en las pruebas)
if (require.main === module) {
  app.listen(port, () => {
    console.log(`Server running on port ${port}`);  // Imprime en la consola un mensaje indicando que el servidor está corriendo
  });
}

// Exporta la aplicación para que puedan ser utilizados en otros módulos, como en pruebas
module.exports = app;