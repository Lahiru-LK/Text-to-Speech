import os
from io import BytesIO
import soundfile as sf
from kokoro import KPipeline

SAMPLE_RATE = 24000
VOICE_FOLDER = "voices"

# 🔤 Voice display names
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
    "bf_alice.pt": "Alice (UK Female)",
    "bf_emma.pt": "Emma (UK Female)",
    "bf_isabella.pt": "Isabella (UK Female)",
    "bf_lily.pt": "Lily (UK Female)",
    "bm_daniel.pt": "Daniel (UK Male)",
    "bm_fable.pt": "Fable (UK Male)",
    "bm_george.pt": "George (UK Male)",
    "bm_lewis.pt": "Lewis (UK Male)",
    "en_us_female.pt": "US Female (Generic)",
    "en_us_male.pt": "US Male (Generic)",
    "ff_siwis.pt": "Siwis (FR Female)",
    "hf_alpha.pt": "Alpha (High Female)",
    "hf_beta.pt": "Beta (High Female)",
    "hm_omega.pt": "Omega (High Male)",
    "hm_psi.pt": "Psi (High Male)"
}

# 📃 Show available voices from folder
def list_available_voices():
    if not os.path.exists(VOICE_FOLDER):
        return []

    voices = sorted([
        f for f in os.listdir(VOICE_FOLDER)
        if f.endswith(".pt")
    ])

    return [
        {
            "id": f,
            "name": voice_labels.get(f, f.replace(".pt", "").capitalize()),
            "language": "en"
        }
        for f in voices
    ]

# 🔊 Generate audio buffer from text + voice
def synthesize_speech(text, voice_file, speed=1.0):
    if not text.strip():
        raise ValueError("Text is empty")

    voice_path = os.path.join(VOICE_FOLDER, voice_file)
    if not os.path.exists(voice_path):
        raise FileNotFoundError(f"Voice file not found: {voice_file}")

    print(f"[INFO] Synthesizing text='{text}' with voice='{voice_file}' and speed={speed}")

    # Kokoro engine
    try:
        pipeline = KPipeline(lang_code="a")
        generator = pipeline(text, voice=voice_path)

        buffer = BytesIO()
        for _, _, audio in generator:
            sf.write(buffer, audio, SAMPLE_RATE, format='MP3')
            break

        buffer.seek(0)
        return buffer

    except Exception as e:
        print(f"[ERROR] Kokoro synthesis failed: {e}")
        raise RuntimeError("Synthesis failed: " + str(e))
