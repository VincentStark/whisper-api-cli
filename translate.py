import argparse
import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set up command-line arguments
parser = argparse.ArgumentParser(
    description="Translate audio using OpenAI API")
parser.add_argument("file", help="Path to audio file")
args = parser.parse_args()

# Set API endpoint and headers
url = "https://api.openai.com/v1/audio/translations"
headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "multipart/form-data",
}

# Prepare file and data for API call
with open(args.file, "rb") as f:
    files = {"file": (os.path.basename(args.file), f)}
    data = {"model": "whisper-1"}

    # Make API call
    response = requests.post(url, headers=headers, data=data, files=files)

# Check for errors and print output
if response.status_code == 200:
    print(response.json()["translation"])
else:
    print(f"Error {response.status_code}: {response.text}")
