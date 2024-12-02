from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os
from app.app_constants import Constants

# MongoDB URI (using environment variable or default connection string)
MONGO_URI = "mongodb://{}:{}@{}:{}/{}".format(Constants.get_mongo_username(),
                                                      Constants.get_mongo_password(),
                                                      Constants.get_mongo_host(),
                                                      Constants.get_mongo_port(),
                                                      Constants.get_environment())
# MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

# Create a custom lifespan context manager for FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Ping MongoDB server on startup
        await client.admin.command("ping")
        print("MongoDB connected successfully")
        yield
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise

# Create the FastAPI app instance and pass the lifespan context
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "MongoDB Ping Test Passed!"}

if __name__ == "__main__":
    # Run the Uvicorn server directly from the script
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)