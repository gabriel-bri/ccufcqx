from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

    
class Aluno(BaseModel):
    id: Optional[str] = Field(default=None,  alias="_id")
    nome_completo: str
    descricao: Optional[str] = None
    contato_email: str
    cursos: List[str] = []
    certificados: List[str] = []


class Aula(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    titulo: str
    descricao: Optional[str] = None
    duracao: str
    material: Optional[str] = None
    modulo_id: Optional[str] = None


class Avaliacao(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    curso_id: Optional[str] = None
    aluno_id: Optional[str] = None
    nota: float
    comentario: Optional[str] = None
    data_avaliacao: datetime = Field(default_factory=datetime.utcnow)


class Categoria(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    nome_categoria: str
    descricao: Optional[str] = None
    data_criacao: datetime = Field(default_factory=datetime.utcnow)
    cursos: List[str] = []


# 1:1 Embedding (documentos embutidos) Embutir detalhes do aluno dentro do Certificado:
class Certificado(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    aluno: Aluno
    curso_id: Optional[str] = None
    data_emissao: datetime = Field(default_factory=datetime.utcnow)
    codigo_verificacao: str
    
    

class Instrutor(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    nome_completo: str
    descricao: Optional[str] = None
    especialidade: Optional[str] = None
    contato_email: str
    cursos: List[str] = []
    
    

# 1:N Referenciamento (relacionamentos entre coleções) um curso tem vários módulos
# N:N Coleção extra para relacionamento bidirecional - curso tem alunos. e aluno tem cursos.
# 1:1 Embedding (documentos embutidos) Embutir detalhes do instrutor dentro do Curso:
class Curso(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    nome_curso: str
    descricao: str
    categoria_id: Optional[str] = None  
    horas_totais: str
    modulos: List[str] = []
    alunos: List[str] = [] 
    instrutor: Optional[Instrutor] = None 



# 1:N Referenciamento (relacionamentos entre coleções) um módulo tem várias aulas
class Modulo(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    nome_modulo: str
    descricao: Optional[str] = None
    curso_id: Optional[str] = None
    aulas: List[str] = []