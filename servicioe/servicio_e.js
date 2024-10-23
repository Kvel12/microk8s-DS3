const express = require('express');
const app = express();
const port = 3005;

app.get('/servicio-a', (req, res) => {
  res.json({ mensaje: "Respuesta desde Servicio E: David Urrego" });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Servicio E escuchando en http://0.0.0.0:${port}`);
});