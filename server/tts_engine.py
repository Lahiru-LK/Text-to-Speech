# ===== tts_engine.py =====
import os
import io
import soundfile as sf
from kokoro import KPipeline
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'kokoro')))

VOICE_FOLDER = "voices"
SAMPLE_RATE = 24000

voice_labels = {
    "af_alloy.pt": "Alloy (US Female)",
    "af_aoede.pt": "Aoede (US Female)",
    "af_bella.pt": "Bella (US Female)",
    "af_heart.pt": "Heart (US Female)",
    "af_jessica.pt": "Jessica (US Female)",
    "af_kore.pt": "Kore (Female)",
    "af_nicole.pt": "Nicole (US Female)",
    "af_nova.pt": "Nova (US Female)",
    "af_river.pt": "River (US Female)",
    "af_sarah.pt": "Sarah (US Female)",
    "af_sky.pt": "Sky (US Female)",
    "am_adam.pt": "Adam (US Male)",
    "am_echo.pt": "Echo (US Male)",
    "am_eric.pt": "Eric (US Male)",
    "am_fenrir.pt": "Fenrir (US Male)",
    "am_liam.pt": "Liam (US Male)",
    "am_michael.pt": "Michael (US Male)",
    "am_onyx.pt": "Onyx (US Male)",
    "am_puck.pt": "Puck (US Male)",
    "en_us_female.pt": "US Female Generic",
    "en_us_male.pt": "US Male Generic",
    "bf_alice.pt": "Alice (UK Female)",
    "bf_emma.pt": "Emma (UK Female)",
    "bf_isabella.pt": "Isabella (UK Female)",
    "bf_lily.pt": "Lily (UK Female)",
    "bm_daniel.pt": "Daniel (UK Male)",
    "bm_fable.pt": "Fable (UK Male)",
    "bm_george.pt": "George (UK Male)",
    "bm_lewis.pt": "Lewis (UK Male)",
    "ff_siwis.pt": "Siwis (FR Female)",
    "hf_alpha.pt": "Alpha (High Female)",
    "hf_beta.pt": "Beta (High Female)",
    "hm_omega.pt": "Omega (High Male)",
    "hm_psi.pt": "Psi (High Male)"
}

def list_available_voices():
    if not os.path.exists(VOICE_FOLDER):
        return []
    voices = sorted([f for f in os.listdir(VOICE_FOLDER) if f.endswith(".pt")])
    return [
        {
            "id": vf,
            "name": voice_labels.get(vf, vf.replace(".pt", "")),
            "language": "en"
        } for vf in voices
    ]

def synthesize_speech(text, voice_file, speed=1.0):
    if not text.strip():
        raise ValueError("Text is empty")

    voice_path = os.path.join(VOICE_FOLDER, voice_file)
    if not os.path.exists(voice_path):
        raise FileNotFoundError(f"Voice file not found: {voice_file}")

    pipeline = KPipeline(lang_code="a")
    generator = pipeline(text, voice=voice_path)

    buffer = io.BytesIO()
    for _, _, audio in generator:
        sf.write(buffer, audio, SAMPLE_RATE, format='MP3')
        break

    buffer.seek(0)
    return buffer