#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import openai
import json
import random
from jsonrpcserver import method, Result, InvalidParams, Success, dispatch, serve

# Define the available constraint keywords
constraint_keywords = ['red', 'green', 'blue', 'yellow', 'purple']

# Define the available image constraints
image_constraints = ['landscape', 'portrait']

openai.organization = "org-ShRy1Ith2eKCV8KxSP1x8CZj"
openai.api_key = "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"
openai.engine = "DALL-E"

# Define the JSON-RPC endpoint method for generating images
@method
def generate_image(constraintKeywords, imageConstraints, subject) -> Result:
    print("generating images")
    # Parse the constraints into lists of keywords and image constraints
    # keywords, img_constraints = constraints.get('constraintKeywords', []), constraints.get('imageConstraints', [])
    # Apply the constraints to randomly generate an image
    response = openai.Image.create(
        prompt=subject,
        n=5,
        size="1024x1024"
    )
    # img_url = response['data'][0]['url']
    # Return the generated image URL as a JSON-RPC response
    print(response)
    return Success(response)

@method
def OPTIONS() -> Result:
    return Success()

# Start the JSON-RPC server on port 5000

if __name__ == "__main__":
    serve(port=5555)
