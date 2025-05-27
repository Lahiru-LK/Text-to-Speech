# Text-to-Speech Converter (AI-Powered TTS)

> Convert your thoughts to clear spoken audio using React + Flask + DeepInfra API.

Live Demo: [https://www.textspeech.42web.io/](https://www.textspeech.42web.io/)

## 🚀 Project Overview

This is an AI-powered Text-to-Speech (TTS) web application developed using:

* **Frontend**: React + Tailwind CSS + Flowbite
* **Backend**: Flask (Python)
* **TTS Engine**: DeepInfra API using Kokoro-82M voice model
* **Deployment**: Hosted on Azure (Static Web App + Python Web App)

  ![Image](https://github.com/user-attachments/assets/899f9b7f-ecef-439e-8a80-846d0825e4a4)

## 🎯 Features

* Text area input with dark/light mode toggle
* 30+ voice options (currently placeholder for UI)
* Audio generation using DeepInfra
* MP3 preview + download
* Responsive UI (Desktop + Mobile)
* Runtime voice synthesis with temporary cloud execution
* Toast message for voice selection and future personalization note

## 🧠 Why AI-powered?

Although the app only returns a single default voice output now, it uses:

* AI-generated speech via **Kokoro TTS model** hosted on **DeepInfra**
* Voice synthesis handled using a cloud-based inference API

The AI model is downloaded on runtime, used temporarily in memory, and deleted after synthesis.

## 🔧 Tech Stack & Tools

* **React** (Vite) + TailwindCSS + Flowbite
* **Python Flask API**
* **DeepInfra API** (Kokoro-82M)
* **.env** files for API keys and base URLs
* Azure Web App for both frontend and backend
* GitHub Actions for deployment pipeline

## 📁 File Structure

```
TEXT-TO-SPEECH-REACT-WITH-PYTHON
├── client
│   ├── src
│   │   ├── components
│   │   │   ├── TextToSpeechUI.jsx
│   │   │   └── VoiceToast.jsx
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── public
│   └── .env (VITE_API_URL)
├── server
│   ├── app.py
│   ├── tts_engine.py
│   ├── requirements.txt
│   └── .env (DEEPINFRA_API_KEY)
├── .github/workflows
│   └── azure-static-web-apps.yml
```

## 🌐 Hosting

* **Frontend**: Azure Static Web App
* **Backend**: Azure Python Web App using Flask API

## 📌 Notes

* Currently, audio is generated using a **default voice**.
* Voice selection UI is implemented, but all requests are routed to the default Kokoro model.
* Future updates will support **multi-voice selection** once API flexibility is expanded.

## 🧪 Runtime Behavior

* Kokoro model and voices are loaded at runtime from DeepInfra servers.
* No large voice model files are stored in the Azure backend.
* Everything is fetched, generated, and discarded per request.

## 👤 Author

**Lahiru Prasad**
Software Engineering Undergraduate, University of Ruhuna
[Portfolio](https://www.lahiruprasad.me/) | [LinkedIn](https://linkedin.com/in/lahiruprasad)

---

> For feedback, open issues or pull requests.
