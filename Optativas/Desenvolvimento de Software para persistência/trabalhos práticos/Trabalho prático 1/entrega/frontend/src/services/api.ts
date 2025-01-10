const baseURL = "http://127.0.0.1:8000";

// Modelo do Evento
export interface Evento {
  id: number;
  titulo: string;
  descricao: string;
  data: string; 
  local: string;
  publicoEsperado: number;
}

interface FiltrosEvento {
  titulo?: string;
  data_inicio?: string; // formato ISO 8601
  data_fim?: string;    // formato ISO 8601
}

// Função para listar eventos
export async function listarEventos(): Promise<Evento[]> {
  const response = await fetch(`${baseURL}/eventos`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error(`Erro ao listar eventos: ${response.statusText}`);
  }

  return response.json();
}

// Função para criar evento
export async function criarEvento(evento: Evento): Promise<Evento> {
  const response = await fetch(`${baseURL}/eventos`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(evento),
  });
  return response.json();
}

// Função para atualizar evento
export const atualizarEvento = async (id: number, evento: Evento) => {
  const response = await fetch(`${baseURL}/eventos/${id}`, {
    method: "PUT",  
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(evento), 
  });

  if (!response.ok) {
    throw new Error("Erro ao atualizar o evento");
  }

  return await response.json();
};


// Função para remover evento
export async function removerEvento(id: number): Promise<void> {
  const response = await fetch(`${baseURL}/eventos/${id}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error(`Erro ao remover evento: ${response.statusText}`);
  }
}

// Função para obter a quantidade de eventos
export async function obterQuantidadeEventos(): Promise<number> {
  const response = await fetch(`${baseURL}/eventos/quantidade`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error(`Erro ao obter quantidade de eventos: ${response.statusText}`);
  }

  const data = await response.json();
  return data.quantidade;
}

// Função para verificar integridade do arquivo CSV
export async function verificarIntegridade(): Promise<string> {
  const response = await fetch(`${baseURL}/integridade`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error(`Erro ao verificar integridade: ${response.statusText}`);
  }

  const data = await response.json();
  return data.hash;
}

// Função para fazer download do backup
export async function baixarBackup(): Promise<Blob> {
  const response = await fetch(`${baseURL}/backup`, {
    method: "GET",
  });

  if (!response.ok) {
    throw new Error(`Erro ao fazer backup: ${response.statusText}`);
  }

  return response.blob();
}

export const filtrarEventos = async (filtros: FiltrosEvento): Promise<Evento[]> => {
  const url = new URL(`${baseURL}/eventos/filtro`);

  // Adiciona os parâmetros de filtro à URL
  if (filtros.titulo) {
    url.searchParams.append("nome", filtros.titulo);
  }
  if (filtros.data_inicio) {
    url.searchParams.append("data_inicio", filtros.data_inicio);
  }
  if (filtros.data_fim) {
    url.searchParams.append("data_fim", filtros.data_fim);
  }

  try {
    const response = await fetch(url.toString(), {
      method: "GET",
    });

    if (!response.ok) {
      if (response.status === 404) {
        throw new Error("Nenhum evento encontrado com os filtros fornecidos.");
      }
      throw new Error("Erro ao buscar eventos. Tente novamente mais tarde.");
    }

    const data: Evento[] = await response.json();
    return data;
  } catch (error) {
    throw new Error(`Erro na requisição: ${error instanceof Error ? error.message : "Erro desconhecido"}`);
  }
} 

export const buscarEventoPorId = async (id: number): Promise<Evento> => {
  const response = await fetch(`${baseURL}/eventos/${id}`, {
    method: "GET",
  });

  
  if (!response.ok) {
    throw new Error(`Erro ao buscar evento com ID ${id}: ${response.statusText}`);
  }
  const evento = await response.json();
  if (evento.data) {
    evento.data = new Date(evento.data).toISOString(); // Converte a data para ISO 8601
  }

  return evento;
};
