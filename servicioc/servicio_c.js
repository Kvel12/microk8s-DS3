const express = require('express');
const app = express();
const port = 3003;

app.get('/servicio-c', (req, res) => {
  res.json({ mensaje: "Respuesta desde Servicio c: Yhan Carlos Trujillo" });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Servicio c escuchando en http://0.0.0.0:${port}`);
});