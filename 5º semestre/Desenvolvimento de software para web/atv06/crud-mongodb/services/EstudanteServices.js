const EstudanteModel = require('../models/EstudanteModel')

class EstudanteService {
    static register(req, res) {
        EstudanteModel.create(req.body)
            .then(
                (estudante) => {
                    res.status(201).json(estudante);
                }
            )

            .catch(
                (error) => {
                    res.status(500).json(error)
                }
            )
    }

    static list(req, res) {
        EstudanteModel.find().then(
            (estudantes) => {
                res.status(201).json(estudantes);
            }
        )

            .catch(
                (error) => {
                    res.status(500).json(error)
                }
            )
    }

    //retorna um user atualizado
    static update(req, res) {
        EstudanteModel.findByIdAndUpdate(req.params.id, req.body, { 'new': true })
        .then(
            (estudante) => {
                res.status(201).json(estudante);
            }
        )

        .catch(
            (error) => {
                res.status(500).json(error)
            }
        )
    }
    //retorna o user deletado
    static delete(req, res) {
        EstudanteModel.findByIdAndRemove(req.params.id)
        .then(
            (estudante) => {
                res.status(201).json(estudante);
            }
        )
        
        .catch(
            (error) => {
                res.status(500).json(error)
            }
        )
    }
    //retorna um user
    static retrieve(req, res) {
        EstudanteModel.findById(req.params.id)
        .then(
            (estudante) => {
                res.status(201).json(estudante);
            }
        )

        .catch(
            (error) => {
                res.status(500).json(error)
            }
        )
    }
}


module.exports = EstudanteService