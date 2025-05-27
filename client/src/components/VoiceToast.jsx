import { useEffect } from "react";
import { Info } from "lucide-react"; // Icon library

export default function VoiceToast({ message, onClose }) {
    useEffect(() => {
        const timer = setTimeout(() => {
            onClose();
        }, 8000); // Auto-dismiss after 6s
        return () => clearTimeout(timer);
    }, [onClose]);

    return (
        <div className="fixed bottom-6 right-6 z-50 bg-white dark:bg-gray-800 text-gray-900 dark:text-white border-l-4 border-red-500 shadow-xl rounded-xl px-5 py-4 w-full max-w-xs animate-fade-in-down transition-all duration-500">
            <div className="flex items-start gap-3">
                <Info className="text-red-600 mt-0.5 shrink-0" size={22} />
                <div className="flex flex-col">
                    <p className="font-semibold text-sm">{message}</p>
                    <p className="text-xs text-gray-500 dark:text-gray-400 mt-1 italic leading-snug">
                        Currently, audio is generated using the default voice.
                        <br />
                        Voice selection is not yet active, but preview and download still work.
                        <br />
                        Voice-based personalization is Coming Soon..!
                    </p>

                </div>
            </div>
        </div>
    );
}
