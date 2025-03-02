from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, time 
from typing import List, Optional

class Curso(SQLModel, table=True):
    id_curso: Optional[int] = Field(default=None, primary_key=True)
    nome_curso: str
    descricao: str
    categoria_id: Optional[int] = Field(default=None, foreign_key="categoria.id_categoria")
    horas_totais: str
    modulos: List["Modulo"] = Relationship(back_populates='curso')
    instrutor_id: int = Field(foreign_key="instrutor.id_instrutor")
    instrutor: List["Instrutor"] = Relationship(back_populates='cursos')
    alunos: List["Inscricao"] = Relationship(back_populates='curso')
    categoria: List["Categoria"] = Relationship(back_populates='cursos')

class Aluno(SQLModel, table=True):
    id_aluno: Optional[int] = Field(default=None, primary_key=True)
    nome_completo: str
    descricao: Optional[str]
    contato_email: str
    cursos: List["Inscricao"] = Relationship(back_populates="aluno")
    certificados: List["Certificado"] = Relationship(back_populates="aluno")

class Aula(SQLModel, table=True):
    id_aula: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    descricao: Optional[str]
    duracao: str
    material: Optional[str]
    modulo_id: Optional[int] = Field(default=None, foreign_key="modulo.id_modulo")
    modulo: Optional["Modulo"] = Relationship(back_populates="aulas")

class Avaliacao(SQLModel, table=True):
    id_avaliacao: Optional[int] = Field(default=None, primary_key=True)
    curso_id: Optional[int] = Field(default=None, foreign_key="curso.id_curso")
    aluno_id: Optional[int] = Field(default=None, foreign_key="aluno.id_aluno")
    nota: float
    comentario: Optional[str]
    data_avaliacao: datetime = Field(default_factory=datetime.utcnow)
    curso: Optional["Curso"] = Relationship()
    aluno: Optional["Aluno"] = Relationship()

class Categoria(SQLModel, table=True):
    id_categoria: Optional[int] = Field(default=None, primary_key=True)
    nome_categoria: str
    descricao: Optional[str]
    data_criacao: datetime = Field(default_factory=datetime.utcnow)
    cursos: List["Curso"] = Relationship(back_populates="categoria")

# 1:1 Certificado e Aluno
class Certificado(SQLModel, table=True):
    id_certificado: Optional[int] = Field(default=None, primary_key=True)
    aluno_id: Optional[int] = Field(default=None, foreign_key="aluno.id_aluno")
    curso_id: Optional[int] = Field(default=None, foreign_key="curso.id_curso")
    data_emissao: datetime = Field(default_factory=datetime.utcnow)
    codigo_verificacao: str
    aluno: Optional["Aluno"] = Relationship(back_populates="certificados")
    curso: Optional["Curso"] = Relationship()

# N:N Curso e Aluno atráves de Inscricao
class Inscricao(SQLModel, table=True):
    id_inscricao: Optional[int] = Field(default=None, primary_key=True)
    aluno_id: Optional[int] = Field(default=None, foreign_key="aluno.id_aluno")
    curso_id: Optional[int] = Field(default=None, foreign_key="curso.id_curso")
    data_inscricao: datetime = Field(default_factory=datetime.utcnow)
    status: str # Exemplo: "Ativo", "Concluído", "Cancelado"
    progresso: float = 0.0  # Percentual de conclusão (0.0 a 100.0)
    aluno: Optional["Aluno"] = Relationship(back_populates="cursos")
    curso: Optional["Curso"] = Relationship(back_populates="alunos")

class Instrutor(SQLModel, table=True):
    id_instrutor: Optional[int] = Field(default=None, primary_key=True)
    nome_completo: str
    descricao: Optional[str]
    especialidade: Optional[str]
    contato_email:str
    cursos: List["Curso"] = Relationship(back_populates="instrutor")
    
# 1:N Curso e Modulo.
class Modulo(SQLModel, table=True):
    id_modulo: Optional[int] = Field(default=None, primary_key=True)
    nome_modulo: str
    descricao: Optional[str]
    curso_id : Optional[int] = Field(default=None, foreign_key="curso.id_curso")
    curso: Optional["Curso"] = Relationship(back_populates="modulos")
    aulas: List["Aula"] = Relationship(back_populates="modulo")


class Suporte(SQLModel, table=True):
    id_suporte: Optional[int] = Field(default=None, primary_key=True)
    aluno_id: Optional[int] = Field(default=None, foreign_key="aluno.id_aluno")
    curso_id: Optional[int] = Field(default=None, foreign_key="curso.id_curso")
    data_abertura:  datetime = Field(default_factory=datetime.utcnow)
    descricao_problema: str
    status: str  # Exemplo: "Aberto", "Em Andamento", "Resolvido"
    aluno: Optional["Aluno"] = Relationship()
    curso: Optional["Curso"] = Relationship()
