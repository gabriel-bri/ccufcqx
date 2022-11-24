const EstudanteModel = require('../models/EstudanteModel')

let estudantes = [
    {_id:0,nome: 'Machado de Assis', curso: 'ES', IRA:5.6},
    {_id:1,nome: 'Costa e Silva', curso: 'ES', IRA:5.6},
    {_id:2,nome: 'Assis', curso: 'ES', IRA:5.6}
]
let _id = 3

class EstudanteService{

    static register(data) {
        let estudante = new EstudanteModel(
            _id++,
            data.nome,
            data.curso,
            data.IRA
        )
        estudantes.push(estudante)
        return estudante
    }

    static list(){
        return estudantes
    }

    static update(_id, data) {
        for(let e of estudantes) {
            if(e._id == _id) {
                e.nome = data.nome,
                e.curso = data.curso,
                e.IRA = data.IRA
                return e;

            }
        }

        return null
    }

    static delete(_id) {
        for(let i = 0; i < estudantes.length; i++) {
            if(estudantes[i]._id == _id) {
                estudantes.splice(i, 1)
                return true
            }
        }

        return false
    }

    static retrieve(_id) {
        for(let i = 0; i < estudantes.length; i++) {
            if(estudantes[i]._id == _id) {
                return estudantes[i]
            }
        }

        return {}
    }
}

module.exports = EstudanteService