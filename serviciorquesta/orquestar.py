from fastapi import FastAPI
import httpx

app = FastAPI()

# Endpoint en Servicio Orquetador para iniciar la orquestación
@app.get("/orquestar")
async def orquestar():
    async with httpx.AsyncClient() as client:
        try:
            respuesta_a = await client.get("http://servicio-a-service/servicio-a")
            data_a = respuesta_a.json()
        except httpx.RequestError:
            data_a = "El servicio A no está disponible"

        try:
            respuesta_b = await client.get("http://servicio-b-service/servicio-b")
            data_b = respuesta_b.json()
        except httpx.RequestError:
            data_b = "El servicio B no está disponible"

    return {"respuesta_a": data_a, "respuesta_b": data_b}