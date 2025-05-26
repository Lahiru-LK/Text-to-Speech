import os
from io import BytesIO

# 🔧 voice files තියෙන්නෙ මෙම folder එකේ
VOICE_FOLDER = "voices"

# 🧾 අර්ථවත් නමක් assign කරන dictionary එකක්
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

# ✅ voice list එකක් return කරන function එක
def list_available_voices():
    if not os.path.exists(VOICE_FOLDER):
        return []

    voices = sorted([
        f for f in os.listdir(VOICE_FOLDER)
        if f.endswith(".pt")
    ])

    return [
        {
            "id": filename,
            "name": voice_labels.get(filename, filename.replace(".pt", "").capitalize()),
            "language": "en"
        } for filename in voices
    ]

# 🧪 test purpose එකට fake audio buffer එකක්
def synthesize_speech(text, voice_file, speed=1.0):
    buffer = BytesIO()
    buffer.write(b"FAKE_MP3_DATA")
    buffer.seek(0)
    print(f"[DEBUG] Synthesizing: {text} | Voice: {voice_file} | Speed: {speed}")
    return buffer
