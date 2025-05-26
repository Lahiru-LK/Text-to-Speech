import { Button, Select, Textarea } from 'flowbite-react';
import { useEffect, useState } from 'react';
import axios from 'axios';

export default function TextToSpeechUI() {
    const [text, setText] = useState('');
    const [voice, setVoice] = useState('');
    const [voices, setVoices] = useState([]);
    const [speed, setSpeed] = useState(1.0);
    const [audioSrc, setAudioSrc] = useState('');
    const [blobUrl, setBlobUrl] = useState('');
    const [loading, setLoading] = useState(false);
    const [showButtons, setShowButtons] = useState(false);
    const [isPreviewing, setIsPreviewing] = useState(false);
    const [isDownloading, setIsDownloading] = useState(false);
    const [isDark, setIsDark] = useState(() => {
        return document.documentElement.classList.contains('dark');
    });

    const API = import.meta.env.VITE_API_URL;


    useEffect(() => {
        axios.get(`${API}/voices`)
            .then(res => {
                setVoices(res.data);
                if (res.data.length > 0) setVoice(res.data[0].id);
            })
            .catch(err => console.error('Voice list error:', err));
    }, []);




    const handleSubmit = async () => {
        setLoading(true); // Start spinner
        try {
                const res = await axios.post(
                    `${API}/tts`,  
                    { text, voice, speed },
                    { responseType: 'blob' }
                );


            const blob = new Blob([res.data], { type: 'audio/mpeg' });
            const url = URL.createObjectURL(blob);

            setBlobUrl(url);
            setAudioSrc(url);
            setShowButtons(true);

        } catch (err) {
            console.error('TTS error:', err);
        } finally {
            setLoading(false); //Stop spinner
        }
    };

    const toggleDark = () => {
        document.documentElement.classList.toggle('dark');
        setIsDark(!isDark);
    };


    return (
        <div className="min-h-screen bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-white flex items-center justify-center px-4 relative">
            {/*  Mode Toggle */}
            <button
                onClick={toggleDark}
                className="absolute top-4 right-4 p-2 bg-gray-200 dark:bg-gray-700 rounded-md hover:scale-105 transition text-xl"
                title="Toggle Theme"
            >
                {isDark ? '🌙' : '☀️'}
            </button>


            <div className="w-full max-w-3xl bg-white dark:bg-gray-800 p-6 sm:p-8 rounded-2xl shadow-2xl space-y-6 transition-all duration-300">

                {/* 🎧 Top Gradient Bar Decoration */}
                <div className="h-1 w-full bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 rounded-t-md mb-2"></div>

                {/* 🗣️ Title with Icon + Subtitle */}
                <div className="text-center space-y-1">
                    <h1 className="text-3xl font-bold flex items-center justify-center gap-2">
                        🗣️ Text-to-Speech
                    </h1>
                    <p className="text-gray-500 dark:text-gray-300 text-sm">
                        Convert your thoughts to clear spoken audio
                    </p>
                </div>

                {/* Text Input */}
                <Textarea
                    id="text"
                    placeholder="Enter your message..."
                    rows={6}
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    className="w-full min-h-[150px] text-base resize-none focus:ring-2 focus:ring-blue-500 transition-all"
                />

                {/* 🎙️ Voice Selection */}
                <div className="flex flex-col sm:flex-row gap-4 items-start sm:items-end justify-between">
                    <div className="w-full sm:w-2/3 flex flex-col gap-2">
                        <div>
                            <label className="text-sm font-medium">Voice</label>
                            <Select
                                value={voice}
                                onChange={(e) => {
                                    setVoice(e.target.value);
                                    setShowButtons(false); // 👉 Hide buttons if voice changed
                                }}
                                className="w-full"
                            >
                                {voices.length === 0 && (
                                    <option disabled selected>No voices found</option>
                                )}
                                {voices.map((v, i) => (
                                    <option key={i} value={v.id}>
                                        {v.name || v.id}
                                    </option>
                                ))}
                            </Select>
                        </div>
                    </div>


                    <Button
                        onClick={handleSubmit}
                        disabled={loading}
                        className={`text-white bg-gradient-to-r from-blue-500 to-blue-600  w-full sm:w-auto px-6  py-2 transition-transform duration-200  ${loading ? 'opacity-70 cursor-not-allowed' : 'hover:scale-105'}`}
                    >
                        {loading ? (
                            <div className="flex items-center gap-2">
                                <svg
                                    className="animate-spin h-4 w-4 text-white"
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                >
                                    <circle
                                        className="opacity-25"
                                        cx="12"
                                        cy="12"
                                        r="10"
                                        stroke="currentColor"
                                        strokeWidth="4"
                                    ></circle>
                                    <path
                                        className="opacity-75"
                                        fill="currentColor"
                                        d="M4 12a8 8 0 018-8v4l5-5-5-5v4a10 10 0 00-10 10h4z"
                                    ></path>
                                </svg>
                                Generating...
                            </div>
                        ) : (
                            "Generate Audio"
                        )}
                    </Button>

                </div>

                {showButtons && (
                    <div className="flex flex-col sm:flex-row gap-4 mt-6 justify-center">
                        {/* Preview Button */}
                        <button
                            onClick={() => {
                                const audio = document.getElementById('audio-player');
                                if (audio) {
                                    setIsPreviewing(true);
                                    audio.play();
                                    audio.onended = () => setIsPreviewing(false); // reset after finish
                                }
                            }}
                            disabled={!audioSrc}
                            className="inline-flex items-center justify-center gap-2 px-5 py-2 bg-emerald-500 text-white rounded-xl shadow hover:bg-emerald-600 hover:scale-105 active:scale-95 transition-all duration-300 disabled:opacity-50"
                            title="Play Audio"
                        >
                            {isPreviewing ? (
                                <>
                                    <svg
                                        className="animate-ping h-5 w-5 text-white"
                                        xmlns="http://www.w3.org/2000/svg"
                                        fill="currentColor"
                                        viewBox="0 0 24 24"
                                    >
                                        <path d="M12 3a9 9 0 100 18 9 9 0 000-18z" />
                                    </svg>
                                    Previewing...
                                </>
                            ) : (
                                <>
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        className="h-5 w-5"
                                        fill="none"
                                        viewBox="0 0 24 24"
                                        stroke="currentColor"
                                    >
                                        <path
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth={2}
                                            d="M14.752 11.168l-5.197-3.034A1 1 0 008 9.034v5.932a1 1 0 001.555.832l5.197-3.034a1 1 0 000-1.696z"
                                        />
                                    </svg>
                                    Preview
                                </>
                            )}
                        </button>


                        {/* Download Button */}
                        <a
                            href={blobUrl}
                            download="Text-to-Speech.mp3"
                            onClick={() => {
                                setIsDownloading(true);
                                setTimeout(() => setIsDownloading(false), 1200); // auto reset after 1.2s
                            }}
                            className="inline-flex items-center justify-center gap-2 px-5 py-2 text-white bg-gradient-to-r from-blue-500 to-blue-600 rounded-xl shadow-md hover:scale-105 hover:shadow-lg active:scale-95 transition-transform duration-300"
                            title="Download Audio"
                        >
                            {isDownloading ? (
                                <>
                                    {/* Spinner Icon */}
                                    <svg className="h-5 w-5 animate-spin text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                        <circle
                                            className="opacity-25"
                                            cx="12"
                                            cy="12"
                                            r="10"
                                            stroke="currentColor"
                                            strokeWidth="4"
                                        />
                                        <path
                                            className="opacity-75"
                                            fill="currentColor"
                                            d="M4 12a8 8 0 018-8v4l5-5-5-5v4a10 10 0 00-10 10h4z"
                                        />
                                    </svg>
                                    Downloading...
                                </>
                            ) : (
                                <>
                                    {/* Static Download Icon */}
                                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 24 24" fill="currentColor">
                                        <path d="M4.5 20a1 1 0 001 1h13a1 1 0 001-1v-1.5a.5.5 0 011 0V20a2 2 0 01-2 2H5.5a2 2 0 01-2-2v-1.5a.5.5 0 011 0V20z" />
                                        <path d="M12 3a1 1 0 011 1v10.586l3.293-3.293a1 1 0 111.414 1.414l-5 5a1 1 0 01-1.414 0l-5-5a1 1 0 011.414-1.414L11 14.586V4a1 1 0 011-1z" />
                                    </svg>
                                    Download
                                </>
                            )}
                        </a>



                    </div>
                )}
                {/*  Add audio player element here */}
                <audio id="audio-player" className="hidden" src={audioSrc}></audio>


            </div>
        </div>
    );
}
