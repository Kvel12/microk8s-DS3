const express = require('express');
const app = express();
const port = 3001;

app.get('/servicio-a', (req, res) => {
  res.json({ mensaje: "Respuesta desde Servicio A" });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Servicio A escuchando en http://0.0.0.0:${port}`);
});