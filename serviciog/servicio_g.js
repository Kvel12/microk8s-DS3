const express = require('express');
const app = express();
const port = 3007;

app.get('/servicio-g', (req, res) => {
  res.json({ mensaje: "Respuesta desde Servicio g: Brayan Urrea" });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Servicio G escuchando en http://0.0.0.0:${port}`);
});