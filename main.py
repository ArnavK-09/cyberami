"""
    uvicorn main:app --reload --workers 2
"""
from __future__ import annotations
import asyncio
import time
import math
from datetime import timedelta
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Step 0: Init API
app = FastAPI()
MODEL = None

# Step 1: Setup Helper functions
def get_system_uptime() -> str:
    """Function to get uptime"""
    with open('/proc/uptime', 'r', encoding='utf-8') as f:
        uptime_seconds: float = float(f.readline().split()[0])
        uptime_string: str = str(timedelta(seconds=uptime_seconds))
    return uptime_string

# Step 2: Load Model
async def load_model_data():
    """Asynchronously load and preprocess data"""

    global MODEL
    model_start_time = time.time()
    print("[Model] Started Processing Data...")
    data: pd.DataFrame = pd.read_csv("data/main.csv")
    data["Label"] = data["Label"].map({"bad": 0, "good": 1})
    X: pd.Series = data["URL"]
    Y: pd.Series = data["Label"]
    model: Pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('classifier', LogisticRegression(solver='lbfgs', max_iter=1000000))
    ])
    model.fit(X, Y)
    print("[Model] Processing Done...", math.floor(
        time.time() - model_start_time), end="s\n")
    MODEL = model

# Start model loading asynchronously
asyncio.create_task(load_model_data())

# Step 3: Configure Routes
@app.get('/')
async def index():
    """ GET / """
    introduction: str = "Welcome to the Our API! This API provides information about phishing links. Go to `/checkurl`"
    usage_time: str = time.strftime("%Y-%m-%d %H:%M:%S")
    uptime: str = get_system_uptime()
    return {
        "introduction": introduction,
        "usage_time": usage_time,
        "uptime": uptime
    }

@app.get('/checkurl', response_class=JSONResponse)
async def check_url(url: str = ""):
    """ GET /checkurl?url=... """
    # Wait for the model to be loaded if not loaded yet
    while MODEL is None:
        await asyncio.sleep(1)
    prediction = MODEL.predict([url])[0]
    return {"url": url, "type": "good" if prediction == 1 else "bad"}
