"use client";

import React, { useEffect, useState } from "react";
import { obterQuantidadeEventos } from "../../services/api"; // Ajuste o caminho conforme necessário

interface TotalEventProps {
    onUpdateTotal: (newTotal: number) => void;
}

const TotalEvent: React.FC<TotalEventProps> = ({ onUpdateTotal }) => {
    const [totalEventos, setTotalEventos] = useState(0);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const buscarTotalEventos = async () => {
            try {
                const quantidade = await obterQuantidadeEventos();
                setTotalEventos(quantidade);
                onUpdateTotal(quantidade);
            } catch (error) {
                console.error('Erro ao obter quantidade de eventos:', error);
                setError("Houve um erro ao carregar a quantidade de eventos.");
            }
        };

        buscarTotalEventos();
    }, [onUpdateTotal]);

    return (
        <div className="mb-3">
            {error ? (
                <p className="text-red-500">{error}</p>
            ) : (
                <h2>Total de Eventos: {totalEventos}</h2>
            )}
        </div>
    );
};

export default TotalEvent;

