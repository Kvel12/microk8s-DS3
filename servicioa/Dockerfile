# Usa una imagen base de Node.js
FROM node:14

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia el archivo del proyecto al contenedor
COPY ./servicio_a.js ./

# Instala Express
RUN npm init -y
RUN npm install express

# Expone el puerto en el que se ejecutará el servicio
EXPOSE 3001

# Comando para ejecutar la aplicación
CMD ["node", "servicio_a.js"]