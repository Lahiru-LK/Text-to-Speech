import { useEffect } from "react";
import { Info } from "lucide-react";

export default function VoiceToast({ message, onClose }) {
    useEffect(() => {
        const timer = setTimeout(() => {
            onClose();
        }, 4000);
        return () => clearTimeout(timer);
    }, [onClose]);

    return (
        <div className="
            fixed z-50 
            w-[92%] max-w-sm 
            left-1/2 sm:left-auto -translate-x-1/2 sm:translate-x-0 
            top-4 sm:top-auto 
            bottom-auto sm:bottom-6 
            sm:right-6 
            bg-white dark:bg-gray-800 
            text-gray-900 dark:text-white 
            border-l-4 border-red-500 
            shadow-xl rounded-xl px-4 py-4 
            animate-fade-in-down transition-all duration-500
        ">
            <div className="flex items-start gap-3">
                <Info className="text-red-600 mt-0.5 shrink-0" size={20} />
                <div className="flex flex-col">
                    <p className="font-semibold text-sm">{message}</p>
                    <p className="text-xs text-gray-500 dark:text-gray-400 mt-1 italic leading-snug">
                        Currently, audio is generated using the default voice.
                        <br />
                        Voice selection is not yet active, but preview and download still work.
                        <br />
                        Voice-based personalization is coming soon!
                    </p>
                </div>
            </div>
        </div>
    );
}
