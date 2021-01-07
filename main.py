from fastapi import FastAPI
from typing import List, Optional
import connection
import uvicorn
import numpy as np
from bson import ObjectId
import re
import math
import requests
from bs4 import BeautifulSoup
from fastapi.responses import PlainTextResponse
from collections import Counter
from schematics.models import Model
from schematics.types import StringType, EmailType
from fastapi.middleware.cors import CORSMiddleware
import os
from pymongo import MongoClient
from datetime import date, datetime, time, timedelta
import pytz
import time
import date_format
import hashlib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def result(res):
    return {"result": res}


@app.get("/")
async def main():
    return 'Hello World'


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80, debug=True)
