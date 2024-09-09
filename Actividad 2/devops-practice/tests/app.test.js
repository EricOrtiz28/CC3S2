const request = require('supertest');  // Se requiere el módulo supertest para realizar peticiones HTTP en las pruebas
const app = require('../src/app');  // Se requiere la aplicación (app) para poder hacer pruebas sobre ella

let server;  // Variable para almacenar la instancia del servidor

beforeAll(() => {
    server = app.listen(0);  // Inicia el servidor antes de las pruebas
});

describe('GET /', () => {  // Se define un bloque de pruebas que describe el comportamiento de la ruta GET '/'
    it('should return Hello, World!', async () => {  // Caso de prueba que verifica si la respuesta es "Hello, World!"
        const res = await request(app).get('/');  // Se hace una petición GET a la ruta raíz '/'
        expect(res.statusCode).toEqual(200);  // Se espera que el código de estado de la respuesta sea 200 (OK)
        expect(res.text).toBe('Hello, World!');  // Se espera que el texto de la respuesta sea "Hello, World!"
    });
});


afterAll((done) => {
    server.close(done);  // Cierra el servidor al finalizar las pruebas
});