"use client";

import React, { useEffect, useState } from "react";
import { listarEventos, removerEvento, obterQuantidadeEventos, filtrarEventos, verificarIntegridade, baixarBackup } from "../../services/api";
import Logo from "../template/Logo";
import Background from "../template/Background";
import Link from "next/link";
import EventoListar from "./EventList";
import EventFilter from "./EventFilter";
import BackupEHash from "./BackupAndHash";
import TotalEvent from "./TotalEvent";
import { useRouter } from "next/navigation";

interface Evento {
    id: number;
    titulo: string;
    descricao: string;
    data: string;
    local: string;
    publicoEsperado: number;
}

const EventoList: React.FC = () => {
    const [eventos, setEventos] = useState<Evento[]>([]);
    const [filtroTitulo, setFiltroTitulo] = useState<string>("");
    const [sha256, setSha256] = useState<string | null>(null);
    const [totalEventos, setTotalEventos] = useState<number>(0);
    const router = useRouter();

    const carregarEventos = async () => {
        const eventosList = await listarEventos();
        setEventos(eventosList);
    };

    const buscarEventosFiltrados = async () => {
        try {
            const eventosFiltrados = await filtrarEventos({ titulo: filtroTitulo });
            setEventos(eventosFiltrados.length === 0 ? [] : eventosFiltrados);
        } catch (error) {
            alert("Evento não encontrado");
            setEventos([]); // Garante que a lista fique vazia em caso de erro
        }
    };

    const atualizarEvento = (id: number) => {
        router.push(`/editar/${id}`); // Redireciona para /evento com o ID do evento
    };

    const excluirEvento = async (id: number) => {
        try {
            await removerEvento(id); // Remove o evento no backend
            setEventos((prev) => prev.filter((evento) => evento.id !== id)); // Atualiza a lista
            alert("Evento excluido")
        } catch (error) {
            console.error("Erro ao excluir evento:", error);
        }
    };

    const obterSha256 = async () => {
        const hash = await verificarIntegridade();
        setSha256(hash);
    };

    const baixarArquivo = async () => {
        const backupBlob = await baixarBackup();
        const link = document.createElement("a");
        link.href = URL.createObjectURL(backupBlob);
        link.download = "backup.zip";
        link.click();
    };

    useEffect(() => {
        carregarEventos();
    }, []);

    return (
        <Background>
            <div className="justify-items-center mb-3">
                <Logo />
            </div>
            <div className="max-w-lg mx-auto p-6 bg-white rounded-xl shadow-lg">
                <EventFilter filtroTitulo={filtroTitulo} setFiltroTitulo={setFiltroTitulo} Filtrar={buscarEventosFiltrados} />
                <Link href="/evento" className="mb-4 mt-4 botao azul px-4 py-2 ">
                    Crie o seu Evento
                </Link>
                {eventos.length > 0 && (
                    <>
                        <BackupEHash sha256={sha256} onDownload={baixarArquivo} onGenerateHash={obterSha256} />
                    </>
                )}
                <TotalEvent onUpdateTotal={setTotalEventos} />
                <EventoListar eventos={eventos} onEditar={atualizarEvento} onExcluir={excluirEvento} />
            </div>
        </Background>
    );
};

export default EventoList;
