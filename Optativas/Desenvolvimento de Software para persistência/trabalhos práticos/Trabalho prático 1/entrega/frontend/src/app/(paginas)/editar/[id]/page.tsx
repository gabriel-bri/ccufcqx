"use client"

import React, { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation"; // useParams do App Router
import { atualizarEvento, buscarEventoPorId } from "../../../../services/api";  // Função para atualizar evento
import EventoUpdate from "@/components/evento/EventUpdate";  // Componente de atualização de evento

interface Evento {
  id: number;
  titulo: string;
  descricao: string;
  data: string;
  local: string;
  publicoEsperado: number;
}

const EventoPage: React.FC = () => {
  const router = useRouter();
  const { id } = useParams();  // Captura o id da URL
  const [evento, setEvento] = useState<Evento | null>(null);  // Evento a ser exibido
  const [loading, setLoading] = useState<boolean>(true);  // Estado de carregamento
  const [erro, setErro] = useState<string>("");  // Estado de erro

  // Simulação de carregamento do evento (pode ser substituído por dados reais)
  useEffect(() => {
    if (id) {
      const fetchEvento = async () => {
        try {
          const eventoData = await buscarEventoPorId(Number(id));  // Chama a função buscarEventoPorId
          setEvento(eventoData);
          setLoading(false);
        } catch (error) {
          setErro(error instanceof Error ? error.message : "Erro desconhecido");
          setLoading(false);
        }
      };
      fetchEvento();
    }
  }, [id]);


  const handleSubmit = async (eventoAtualizado: Evento) => {
    try {
      if (id) {
        await atualizarEvento(Number(id), eventoAtualizado);  // Chama a função para atualizar o evento
        alert("Evento atualizado com sucesso!");
        router.push("/eventos");  // Redireciona para a lista de eventos
      }
    } catch (error) {
      alert("Erro ao atualizar evento.");
    }
  };

  if (loading) {
    return <div>Carregando...</div>;  // Exibe um carregamento enquanto o evento é carregado
  }

  if (erro) {
    return <div className="text-red-500">{erro}</div>;  // Exibe erro se não conseguir carregar o evento
  }

  return (
    <div>
      {evento && <EventoUpdate evento={evento} onSubmit={handleSubmit} />} {/* Passa o evento e o handleSubmit */}
    </div>
  );
};

export default EventoPage;
