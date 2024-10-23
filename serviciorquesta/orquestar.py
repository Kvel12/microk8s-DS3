from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/orquestar")
async def orquestar():
    async with httpx.AsyncClient() as client:
        try:
            respuesta_a = await client.get("http://servicio-a-service:3001/servicio-a")
            data_a = respuesta_a.json()
        except httpx.RequestError as e:
            data_a = f"El servicio A no está disponible: {str(e)}"

        try:
            respuesta_b = await client.get("http://servicio-b-service:3002/servicio-b")
            data_b = respuesta_b.json()
        except httpx.RequestError as e:
            data_b = f"El servicio B no está disponible: {str(e)}"

    return {"respuesta_a": data_a, "respuesta_b": data_b}