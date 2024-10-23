const express = require('express');
const app = express();
const port = 3002;

app.get('/servicio-b', (req, res) => {
  res.json({ mensaje: "Respuesta desde Servicio B: Juan Cifuentes" });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Servicio B escuchando en http://0.0.0.0:${port}`);
});