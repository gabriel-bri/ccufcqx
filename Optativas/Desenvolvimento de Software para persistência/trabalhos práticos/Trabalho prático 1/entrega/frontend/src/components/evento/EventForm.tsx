"use client"

import React, { useState } from "react";
import { criarEvento } from "../../services/api";
import { useRouter } from "next/navigation";
import Background from "../template/Background";

interface Evento {
  id: number;
  titulo: string;
  descricao: string;
  data: string;
  local: string;
  publicoEsperado: number;
}

const EventForm: React.FC = () => {
  const [evento, setEvento] = useState<Evento>({
    id: 0,
    titulo: "",
    descricao: "",
    data: "",
    local: "",
    publicoEsperado: 0,
  });

  const [erro, setErro] = useState<string>("");

  const router = useRouter();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setEvento((prevEvento) => ({
      ...prevEvento,
      [name]: value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (evento.publicoEsperado < 1) {
      alert("Público esperado deve ser maior ou igual a 1.");
      return;
    }

    const eventSubmit = {
      ...evento,
      data: new Date(evento.data).toISOString(),
      publicoEsperado: Number(evento.publicoEsperado),
    };



    try {
      await criarEvento(eventSubmit);
      alert("Evento criado com sucesso!");
      setEvento({
        id: 0,
        titulo: "",
        descricao: "",
        data: "",
        local: "",
        publicoEsperado: 0,
      });
      // A navegação agora usa o contexto correto
      router.push("/eventos");
    } catch (error) {
      console.error("Erro ao criar evento:", error);
      alert("Verifique os dados e tente novamente.");
    }
  };

  return (
    <>
    <Background>
      <form onSubmit={handleSubmit} className="max-w-lg mx-auto p-6 bg-white rounded-lg shadow-lg">
        {erro && <div className="text-red-500 mb-4">{erro}</div>}
        <div className="mb-4">
          <label htmlFor="titulo" className="block text-lg font-semibold text-black mb-2">
            Título:
          </label>
          <input
            name="titulo"
            id="titulo"
            value={evento.titulo}
            onChange={handleChange}
            className="w-full p-3 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-green-500 focus:ring-1 focus:ring-green-500"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="descricao" className="block text-lg font-semibold text-black mb-2">
            Descrição:
          </label>
          <textarea
            name="descricao"
            id="descricao"
            value={evento.descricao}
            onChange={handleChange}
            className="w-full p-3 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-green-500 focus:ring-1 focus:ring-green-500"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="data" className="block text-lg font-semibold text-black mb-2">
            Data:
          </label>
          <input
            type="datetime-local"
            name="data"
            id="data"
            value={evento.data}
            onChange={handleChange}
            className="w-full p-3 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-green-500 focus:ring-1 focus:ring-green-500"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="local" className="block text-lg font-semibold text-black mb-2">
            Local:
          </label>
          <input
            name="local"
            id="local"
            value={evento.local}
            onChange={handleChange}
            className="w-full p-3 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-green-500 focus:ring-1 focus:ring-green-500"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="publicoEsperado" className="block text-lg font-semibold text-black mb-2">
            Público Esperado:
          </label>
          <input
            type="number"
            name="publicoEsperado"
            id="publicoEsperado"
            value={evento.publicoEsperado}
            onChange={handleChange}
            className="w-full p-3 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-green-500 focus:ring-1 focus:ring-green-500"
            required
          />
        </div>
        <button
          type="submit"
          className="w-full p-3 bg-green-500 text-white font-semibold rounded-lg hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-400"
        >
          Criar Evento
        </button>
      </form>
      </Background>
  </>
  );
};

export default EventForm;