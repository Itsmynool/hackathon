import requests
import openai
import json

import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
from torchaudio.transforms import Resample


def getData(api_url):
    try:
        timeout = 120  # segundos

        response = requests.get(api_url, timeout=timeout, verify=False)
        if response.status_code == 200:
            data = response.json()
            data = data["values"]
        else:
            print(f"Error en la solicitud: Código {response.status_code}")

    except requests.exceptions.Timeout:
        print("Error en la solicitud: Tiempo de espera agotado")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {str(e)}")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        
    return data

def getPrompt(data):
    openai.api_key = "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"
    prompt = "Genera una descripción (Con los indices) para representar el entorno de manera visual con los siguientes datos:\n" + json.dumps(data) + "\n(La descripcion no debe superar 950 caracteres)"
    
    responseGPT = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000 
    )
    
    response = responseGPT.choices[0].text
    
    return response

def getImage(prompt):
    response = openai.Image.create(
        prompt = prompt,
        n = 1,
        size = '1024x1024'
    )
    
    return response.get('data')[0].get('url')