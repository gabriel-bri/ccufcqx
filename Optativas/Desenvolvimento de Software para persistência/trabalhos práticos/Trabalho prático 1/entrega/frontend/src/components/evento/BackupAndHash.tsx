import React from "react";

interface BackupAndHashProps {
    sha256: string | null;
    onDownload: () => void;
    onGenerateHash: () => void;
}

const BackupAndHash: React.FC<BackupAndHashProps> = ({ sha256, onDownload, onGenerateHash }) => {
    return (
        <div className="mt-4 mb-3 p-4 border rounded-lg bg-gray-100">
            <div className="mt-4 text-center">
                <img src="/logo.png" alt="Logo" className="w-20 h-20 mx-auto mb-4" />
                <p className="text-gray-600 text-sm">Baixe todos os eventos da lista.</p>
            </div>
            <div className="flex justify-between mt-4">
                <button className="botao azul px-4 py-2" onClick={onDownload}>
                    Download
                </button>
                <button className="botao cinza px-4 py-2" onClick={onGenerateHash}>
                    Sum
                </button>
            </div>
            {sha256 && (
                <div className="mt-4 p-4 bg-white">
                    <p className="text-sm text-gray-600 break-words">SHA256: {sha256}</p>
                </div>
            )}
        </div>
    );
};

export default BackupAndHash;
