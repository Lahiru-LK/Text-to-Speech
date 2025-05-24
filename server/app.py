from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from tts_engine import synthesize_speech, list_available_voices
import io

app = Flask(__name__)
CORS(app)

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data.get('text', '')
    voice = data.get('voice', '')
    speed = float(data.get('speed', 1.0))

    try:
        audio_buffer = synthesize_speech(text, voice, speed)
        return send_file(
            io.BytesIO(audio_buffer.read()),
            mimetype='audio/mpeg',
            as_attachment=False,
            download_name='tts_output.mp3'
        )
    except Exception as e:
        return {'error': str(e)}, 500

@app.route('/voices', methods=['GET'])
def voices():
    all_voices = list_available_voices()
    print("Available Voices:", all_voices)  # 🧪 Debug log
    return jsonify(all_voices)


if __name__ == '__main__':
    app.run(debug=True)
