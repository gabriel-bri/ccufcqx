import React from "react";

interface EventFilterProps {
    filtroTitulo: string;
    setFiltroTitulo: (value: string) => void;
    Filtrar: () => void;
}

const EventFilter: React.FC<EventFilterProps> = ({ filtroTitulo, setFiltroTitulo, Filtrar }) => {
    return (
        <div className="flex gap-2">
            <input
                type="text"
                value={filtroTitulo}
                onChange={(e) => setFiltroTitulo(e.target.value)}
                className="border p-2 rounded flex-1"
                placeholder="Procurar por título"
            />
            <button onClick={Filtrar} className="botao azul px-4 py-2">
                Filtrar
            </button>
        </div>
    );
};

export default EventFilter;