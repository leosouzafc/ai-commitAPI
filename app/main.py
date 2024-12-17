from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()
client = OpenAI(
    api_key=os.getenv("API_KEY"),
)
app = FastAPI()

class BodyModel(BaseModel):
    diff: str
    style: Optional[str] = "conventional"

@app.get("/")
async def read_root():
    return {"Hello": "World"}
   
@app.post("/generate-commit")
def call_openai_api(body: BodyModel):
    try:
        client = OpenAI()

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Gere uma mensagem de commit, seguindo o padrão " + body.style + " Diff: " + body.diff,
                }
            ],
            model="gpt-3.5-turbo",
        )
        return {"response": chat_completion.choices[0].message.content}

    except Exception as e:
        return {"Erro ao chamar a API": str(e)}
