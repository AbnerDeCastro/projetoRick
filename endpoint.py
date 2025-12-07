from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/personagem/{id}")
async def get_personagem(id: int):
    url = f"https://rickandmortyapi.com/api/character/{id}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    # response.json() devolve o JSON da API
    return response.json()