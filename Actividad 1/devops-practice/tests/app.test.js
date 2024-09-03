const request = require('supertest');
const { app, server } = require('../src/app');  // Importa tanto la aplicación como el servidor

afterAll((done) => {
  server.close(done);  // Cierra el servidor al finalizar las pruebas
});

test('should return Hello, World!', async () => {
  const res = await request(app).get('/');  // Utiliza `app` para realizar solicitudes en las pruebas
  expect(res.statusCode).toEqual(200);  // Verifica que el código de estado de la respuesta sea 200 (OK)
  expect(res.text).toBe('Hello, World!');  // Verifica que el texto de la respuesta sea 'Hello, World!'
});
