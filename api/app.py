from typing import Union 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn 

description = """help financial institutions quickly and efficiently 
recalibrate their machine learning and AI models. Our platform provides a streamlined process for approving and deploying recalibrated models, reducing the time and resources needed to stay ahead of the 
rapidly changing financial landscape. With our innovative approach, financial institutions can avoid false positives and prevent potential financial collapses. Don't let outdated models hold you back, 
join our platform and stay ahead of the curve."""
from routes import base_router


app = FastAPI(
    title="graphieeapi",
    description=description,
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(base_router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)