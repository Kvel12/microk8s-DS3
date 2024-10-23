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
        
        try:
            respuesta_c = await client.get("http://servicio-c-service:3003/servicio-c")
            data_c = respuesta_c.json()
        except httpx.RequestError as e:
            data_c = f"El servicio C no está disponible: {str(e)}"

        try:
            respuesta_d = await client.get("http://servicio-d-service:3004/servicio-d")
            data_d = respuesta_d.json()
        except httpx.RequestError as e:
            data_d = f"El servicio D no está disponible: {str(e)}"

        try:
            respuesta_e = await client.get("http://servicio-e-service:3005/servicio-e")
            data_d = respuesta_e.json()
        except httpx.RequestError as e:
            data_e = f"El servicio E no está disponible: {str(e)}"
        
        try:
            respuesta_f = await client.get("http://servicio-f-service:3006/servicio-f")
            data_f = respuesta_f.json()
        except httpx.RequestError as e:
            data_f = f"El servicio F no está disponible: {str(e)}"

    return {"respuesta_a": data_a, "respuesta_b": data_b, "respuesta_c": data_c,"respuesta_d": data_d, "respuesta_e": data_e, "respuesta_f": data_f}
