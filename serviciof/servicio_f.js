const express = require('express');
const app = express();
const port = 3006;

app.get('/servicio-f', (req, res) => {
  res.json({ mensaje: "Respuesta desde Servicio F: Moreno Miguel Angel" });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Servicio F escuchando en http://0.0.0.0:${port}`);
});
