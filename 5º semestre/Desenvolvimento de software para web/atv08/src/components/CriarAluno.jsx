import React, {Component} from 'react'

export default class CriarAluno extends Component {
    constructor(props){
        super(props)

        this.state = {nomeAluno:'',curso:'',IRA:''}
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleChange(event){
        this.setState({
            [event.target.name]:event.target.value
        })
    }

    handleSubmit(event) {
        event.preventDefault()
        alert(`Aluno ${this.state.nomeAluno} do curso ${this.state.curso} e IRA de ${this.state.IRA} inserido com sucesso!`)
        console.log(this.state.nomeAluno)
        console.log(this.state.curso)
        console.log(this.state.IRA)
        this.setState({nomeAluno:''})
        this.setState({curso:''})
        this.setState({IRA:''})
    }

    render(){
        return (
            <div>
                <h1>Cadastro de alunos.</h1>
                <p>Dados requiridos: Nome, Curso e IRA.</p>
                <form onSubmit={this.handleSubmit}>
                    <div className='form-group'>
                        <label htmlFor='nomeAluno'>Nome: </label>
                        <input name='nomeAluno' type='text' value={this.state.nomeAluno} onChange={this.handleChange}
                            className = 'form-control'
                        />
                    </div>
                    
                    <div className='form-group'>
                        <label htmlFor='curso'>Curso: </label>
                        <input name='curso' type='text' value={this.state.curso} onChange = {this.handleChange} 
                            className = 'form-control'
                        />

                    </div>

                    <div className='form-group'>
                        <label htmlFor='IRA'>IRA: </label>
                        <input name='IRA' type='number' value={this.state.IRA} onChange={this.handleChange}
                         className='form-control'
                        />

                    </div>
 
                    <div>
                        <button type='submit' className='btn btn-primary'>Cadastrar aluno.</button>
                    </div>
                </form>
            </div>
        )
    }
}