export default class FirebaseService {
    static list = (firestore, callback) => {
        let ref = firestore.collection('estudantes')
        ref.onSnapshot(
            (query) => {
                let alunos = []
                query.forEach(
                    (doc) => {
                        const { nome, curso, IRA } = doc.data()
                        alunos.push(
                            {
                                _id: doc.id,
                                nome,
                                curso,
                                IRA,
                            }
                        )
                    }
                )

                callback(alunos)
            }
        )
    }

    static delete = (firestore, callback, id) => {
        firestore.collection('estudantes').doc(id).delete()
            .then(
                () => callback('Registro deletado com sucesso')
            )

            .catch(error => console.log(error))
    }

    static create = (firestore, callback, aluno) => {
        firestore.collection('estudantes').add(
            {
                nome: aluno.nome,
                curso: aluno.curso,
                IRA: aluno.IRA
            }
        )

            .then(
                () => callback("Estudante inserido com sucesso")
            )

            .catch(error => callback(error))
    }

    static retrieve = (firestore, callback, id) => {
        firestore.collection('estudantes').doc(id).get()

        .then(
            (doc) => {

                callback(
                    {
                        nome: doc.data().nome,
                        curso: doc.data().curso,
                        IRA: doc.data().IRA
                    }
                )
            }
        )
        .catch(error => callback(null))
    }

    static edit = (firestore, callback, aluno, id) => {
        firestore.collection('estudantes').doc(id).set(
            {
                nome: aluno.nome,
                curso: aluno.curso,
                IRA: aluno.IRA
            }
        )

        .then(() => callback("Aluno atualizado com sucesso"))
        .catch((error) => callback(error))
    }
}