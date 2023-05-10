#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import openai
import json
import random
from fastapi import FastAPI, Request, Response
from jsonrpcserver import method, Result, InvalidParams, Success, dispatch, serve
import uvicorn

# Define the available constraint keywords
constraint_keywords = ['red', 'green', 'blue', 'yellow', 'purple']

# Define the available image constraints
image_constraints = ['landscape', 'portrait']

openai.organization = "org-ShRy1Ith2eKCV8KxSP1x8CZj"
openai.api_key = os.getenv("OPENAI_API_KEY") 
openai.engine = "DALL-E"

app = FastAPI()

# Define the JSON-RPC endpoint method for generating images
@app.post("/api")
async def generate_image(request: Request):
    request_body = await request.json()

    print(request_body)

    data = request_body['params']

    print(data)

    print("generating images")
    # Parse the constraints into lists of keywords and image constraints
    # keywords, img_constraints = constraints.get('constraintKeywords', []), constraints.get('imageConstraints', [])
    # Apply the constraints to randomly generate an image
    response = openai.Image.create(
        prompt=data['subject'],
        n=10,
        size="1024x1024",
    )
    # img_url = response['data'][0]['url']
    # Return the generated image URL as a JSON-RPC response
    print(response)

    return response 

@method
def OPTIONS() -> Result:
    return Success()

# Start the JSON-RPC server on port 5000

if __name__ == "__main__":
    uvicorn.run(app, port=5555)    
