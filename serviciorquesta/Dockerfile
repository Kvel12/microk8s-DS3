# Usa una imagen base oficial de Python con FastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY ./orquestar.py /app

# Instala las dependencias
RUN pip install httpx

# Comando para ejecutar la aplicación
CMD ["uvicorn", "orquestar:app", "--host", "0.0.0.0", "--port", "8000"]
