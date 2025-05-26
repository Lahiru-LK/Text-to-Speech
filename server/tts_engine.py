def list_available_voices():
    return [
        {"id": "test_voice", "name": "Test Voice", "language": "en"}
    ]

def synthesize_speech(text, voice_file, speed=1.0):
    from io import BytesIO
    fake_audio = BytesIO()
    fake_audio.write(b"FAKE_MP3_DATA")
    fake_audio.seek(0)
    print(f"[TTS Engine] Synthesizing text: {text} with voice: {voice_file} at speed: {speed}")
    return fake_audio
