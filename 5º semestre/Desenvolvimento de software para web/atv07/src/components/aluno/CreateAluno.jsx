import React, {Component} from 'react'

import FirebaseContext from '../../utils/FirebaseContext'
import FirebaseService from '../../services/FirebaseService'

const CreatePage = () => (
    <FirebaseContext.Consumer>
        { (contexto) => <CreateAluno firebase={contexto}/>}
    </FirebaseContext.Consumer>
)


class CreateAluno extends Component{
    
    constructor(props) {
        super(props)
        this.state = {nome:'', curso:'', IRA:0}
        this.setNome = this.setNome.bind(this)
        this.setCurso = this.setCurso.bind(this)
        this.setIRA = this.setIRA.bind(this)
        this.onSubmit = this.onSubmit.bind(this)
    }

    setNome(e) {
        this.setState({nome:e.target.value})
    }

    setCurso(e) {
        this.setState({curso:e.target.value})
    }

    setIRA(e) {
        this.setState({IRA:e.target.value})
    }

    onSubmit(e) {
        e.preventDefault()
        const alunos = {nome:this.state.nome, curso:this.state.curso, IRA:this.state.IRA}
        FirebaseService.create(
            this.props.firebase.getFirestore(),
            (mensagem) => {
                if(mensagem === "Estudante inserido com sucesso"){
                    alert("Estudante inserido com sucesso")
                }
            },
            alunos
        )
        // this.props.firebase.getFirestore().collection('estudantes').add(
        //     {
        //         nome: this.state.nome,
        //         curso: this.state.curso,
        //         IRA: this.state.IRA
        //     }
        // )

        // .then(
        //     () => alert("Estudante inserido com sucesso")
        // )

        // .catch(error => console.log(error))
        
        
        this.setState({nome:'', curso:'', IRA:0})
    }
    render() {
        return(
            <div style={{marginTop:50}}>
                <h4>Criar Aluno</h4>
                <form onSubmit={this.onSubmit}>
                    <div className='form-group'>
                        <label>Nome:</label>
                        <input type='text' className='form-control' value={this.state.nome} onChange={this.setNome} placeholder="Entre com seu nome"/>
                    </div>

                    <div className='form-group'>
                        <label>Curso:</label>
                        <input type='text' className='form-control' value={this.state.curso} onChange={this.setCurso} placeholder="Seu curso"/>
                    </div>

                    <div className='form-group'>
                        <label>IRA:</label>
                        <input type='text' className='form-control' value={this.state.IRA} onChange={this.setIRA}/>
                    </div>

                    <div className='form-group' style={{marginTop:10}}>
                        <input type='submit' className='btn btn-primary' value='SALVAR'/>
                    </div>
                </form>
            </div>
        )
    }
}

export default CreatePage