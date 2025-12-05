import os
import requests

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
       raise RuntimeError("Set GOOGLE_API_KEY in your environment first")

url = "https://generativelanguage.googleapis.com/v1beta/models"
params = {"key": api_key}

resp = requests.get(url, params=params)
resp.raise_for_status()
print(resp.json())