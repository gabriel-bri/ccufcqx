import React from "react";
import { useRouter } from "next/navigation";

interface Evento {
    id: number;
    titulo: string;
    descricao: string;
    data: string;
    local: string;
    publicoEsperado: number;
}

interface EventListProps {
    eventos: Evento[];
    onEditar: (id: number) => void;
    onExcluir: (id: number) => void;
}

const EventList: React.FC<EventListProps> = ({ eventos, onEditar: onEditar, onExcluir: onExcluir }) => {
    return (
        <ul>
            {eventos.length > 0 ? (
                eventos.map((evento) => (
                    <li className="mb-4 w-full p-3 border-2 border-gray-300 rounded-lg" key={evento.id}>
                        <h2 className="block text-lg font-semibold text-black">Titulo: {evento.titulo}</h2>
                        <p>Descrição: {evento.descricao}</p>
                        <p>
                            Data: {new Intl.DateTimeFormat("pt-BR", {
                                day: "2-digit",
                                month: "2-digit",
                                year: "numeric", // 'numeric' para o ano com 4 dígitos
                                hour: "2-digit",
                                minute: "2-digit",
                                hour12: false, // Formato 24h
                            }).format(new Date(evento.data))}
                        </p>
                        <p>Local: {evento.local}</p>
                        <p>Público esperado: {evento.publicoEsperado}</p>
                        <button onClick={() => onEditar(evento.id)} className="botao verde mb-4 px-5">
                            Editar
                        </button>
                        <button onClick={() => onExcluir(evento.id)} className="botao vermelho px-5">
                            Excluir
                        </button>
                    </li>
                ))
            ) : (
                <p className="text-gray-500 text-center">Nenhum evento encontrado.</p>
            )}
        </ul>
    );
};

export default EventList;
