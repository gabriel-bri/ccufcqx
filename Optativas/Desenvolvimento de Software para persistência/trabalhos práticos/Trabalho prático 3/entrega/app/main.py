from fastapi import FastAPI
from Routes import alunos, cursos, aulas, avaliacao, categoria, certificado, instrutor, modulo, consultas_complexas

app = FastAPI()

app.include_router(alunos.router, tags=["Alunos"])
app.include_router(consultas_complexas.router, tags=["Consultas Complexas"])
app.include_router(cursos.router, tags=["Cursos"])
app.include_router(aulas.router, tags=["Aulas"])
app.include_router(avaliacao.router, tags=["Avaliação"])
app.include_router(categoria.router, tags=["Categoria"])
app.include_router(certificado.router, tags=["Certificado"])
app.include_router(instrutor.router, tags=["Instrutor"])
app.include_router(modulo.router, tags=["Modulo"])