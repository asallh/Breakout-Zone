from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

# MongoDB URI (using environment variable or default connection string)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://nhlUser:nhlPassword@localhost:27017/NHL?directConnection=true")

# MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

@app.on_event("startup")
async def startup_db():
    try:
        # Ping the MongoDB server to check connection
        await client.admin.command("ping")
        print("MongoDB connected successfully")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

@app.get("/")
async def root():
    return {"message": "MongoDB Ping Test Passed!"}