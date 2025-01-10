import React, { useState, useEffect } from "react";

interface Evento {
  id: number;
  titulo: string;
  descricao: string;
  data: string;
  local: string;
  publicoEsperado: number;
}

interface EventoAtualizarProps {
  evento: Evento;
  onSubmit: (evento: Evento) => void;  // Função para enviar o evento atualizado
}

const EventoUpdate: React.FC<EventoAtualizarProps> = ({ evento, onSubmit }) => {
  const [formData, setFormData] = useState<Evento>(evento);  // Preenche os dados iniciais

  useEffect(() => {
    // Formatar a data recebida da API
    const formattedDate = formatDate(evento.data);
    setFormData((prevData) => ({
      ...prevData,
      data: formattedDate,  // Atualiza o campo de data com o formato correto
    }));
  }, [evento]);

  // Função para formatar a data no formato adequado para o campo datetime-local
  const formatDate = (date: string) => {
    const dateObj = new Date(date);  // Converte a string da data para um objeto Date
    const year = dateObj.getFullYear();
    const month = (dateObj.getMonth() + 1).toString().padStart(2, "0");
    const day = dateObj.getDate().toString().padStart(2, "0");
    const hours = dateObj.getHours().toString().padStart(2, "0");
    const minutes = dateObj.getMinutes().toString().padStart(2, "0");

    return `${year}-${month}-${day}T${hours}:${minutes}`;
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(formData);  // Envia o evento atualizado para o onSubmit
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-lg mx-auto p-6 bg-white rounded-lg shadow-lg">
      <div className="mb-4">
        <label htmlFor="titulo" className="block text-lg font-semibold text-black mb-2">
          Título:
        </label>
        <input
          name="titulo"
          id="titulo"
          value={formData.titulo}
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
          value={formData.descricao}
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
          value={formData.data}
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
          value={formData.local}
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
          value={formData.publicoEsperado}
          onChange={handleChange}
          className="w-full p-3 border-2 border-gray-300 rounded-lg focus:outline-none focus:border-green-500 focus:ring-1 focus:ring-green-500"
          required
        />
      </div>
      <button
        type="submit"
        className="w-full p-3 bg-green-500 text-white font-semibold rounded-lg hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-400"
      >
        Atualizar Evento
      </button>
    </form>
  );
};

export default EventoUpdate;
