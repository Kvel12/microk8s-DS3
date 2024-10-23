const express = require('express');
const app = express();
const port = 3004;

app.get('/servicio-d', (req, res) => {
  res.json({ mensaje: "Respuesta desde Servicio D: Jose Manuel Palma" });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Servicio D escuchando en http://0.0.0.0:${port}`);
});