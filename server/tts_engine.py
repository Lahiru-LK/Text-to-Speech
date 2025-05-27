# === tts_engine.py ===
import os
from io import BytesIO
import requests
from base64 import b64decode
from dotenv import load_dotenv

load_dotenv()

voice_labels = {
    "af_alloy": "Alloy (US Female)",
    "af_aoede": "Aoede (US Female)",
    "af_bella": "Bella (US Female)",
    "af_heart": "Heart (US Female)",
    "af_jessica": "Jessica (US Female)",
    "af_kore": "Kore (Female)",
    "af_nicole": "Nicole (US Female)",
    "af_nova": "Nova (US Female)",
    "af_river": "River (US Female)",
    "af_sarah": "Sarah (US Female)",
    "af_sky": "Sky (US Female)",
    "am_adam": "Adam (US Male)",
    "am_echo": "Echo (US Male)",
    "am_eric": "Eric (US Male)",
    "am_fenrir": "Fenrir (US Male)",
    "am_liam": "Liam (US Male)",
    "am_michael": "Michael (US Male)",
    "am_onyx": "Onyx (US Male)",
    "am_puck": "Puck (US Male)",
    "bf_alice": "Alice (UK Female)",
    "bf_emma": "Emma (UK Female)",
    "bf_isabella": "Isabella (UK Female)",
    "bf_lily": "Lily (UK Female)",
    "bm_daniel": "Daniel (UK Male)",
    "bm_fable": "Fable (UK Male)",
    "bm_george": "George (UK Male)",
    "bm_lewis": "Lewis (UK Male)",
    "en_us_female": "US Female (Generic)",
    "en_us_male": "US Male (Generic)",
    "ff_siwis": "Siwis (FR Female)",
    "hf_alpha": "Alpha (High Female)",
    "hf_beta": "Beta (High Female)",
    "hm_omega": "Omega (High Male)",
    "hm_psi": "Psi (High Male)"
}

def list_available_voices():
    return [
        {
            "id": f,
            "name": voice_labels.get(f, f.capitalize()),
            "language": "en"
        }
        for f in voice_labels
    ]

def synthesize_speech(text, voice_file, speed=1.0, engine='deepinfra'):
    if not text.strip():
        raise ValueError("Text is empty")

    if engine == 'deepinfra':
        api_key = os.getenv("DEEPINFRA_API_KEY")
        if not api_key:
            raise EnvironmentError("Missing DEEPINFRA_API_KEY in .env")

        url = "https://api.deepinfra.com/v1/inference/hexgrad/Kokoro-82M"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "text": text,
            "voice": voice_file,
            "speed": speed,
            "format": "mp3"
        }

        print("📤 Payload:", payload)
        response = requests.post(url, headers=headers, json=payload)
        print("📥 Response:", response.status_code)

        if response.status_code != 200:
            print("🔴 DeepInfra Error:", response.status_code, response.text)
            response.raise_for_status()

        result = response.json()
        audio_uri = result.get("audio")

        if not audio_uri or not audio_uri.startswith("data:audio"):
            raise ValueError("No audio returned from DeepInfra")

        base64_data = audio_uri.split(",", 1)[1]  # ✅ extract only base64 content
        audio_bytes = b64decode(base64_data)
        return BytesIO(audio_bytes)
