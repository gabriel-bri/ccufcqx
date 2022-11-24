import React, {Component} from 'react'
import axios from 'axios'

import Swal from 'sweetalert2'
import withReactContent from 'sweetalert2-react-content'
const MySwal = withReactContent(Swal)

export default class EditAluno extends Component{
    
    constructor(props) {
        super(props)
        this.state = {nome:'', curso:'', IRA:0}
        this.setNome = this.setNome.bind(this)
        this.setCurso = this.setCurso.bind(this)
        this.setIRA = this.setIRA.bind(this)
        this.onSubmit = this.onSubmit.bind(this)
    }

    componentDidMount() {
        // console.log(this.props.match.id)
        axios.get('http://localhost:3002/estudantes/retrieve/' + this.props.match.params.id)
        // axios.get('http://localhost:3001/alunos/' + this.props.match.params.id)
        .then(
            (response)=>{
                // alert("Obrigado senhor")
                this.setState(
                    {
                        nome:response.data.nome,
                        curso:response.data.curso,
                        IRA:response.data.IRA
                    }
                )
            }
        )

        .catch(
            (error)=>{
                alert("erro")
            }
        )
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
        const alunoAtualizado = {nome:this.state.nome, curso:this.state.curso, IRA:this.state.IRA}

        // axios.put('http://localhost:3001/alunos/'+ this.props.match.params.id, alunoAtualizado)
        axios.put('http://localhost:3002/estudantes/update/'+ this.props.match.params.id, alunoAtualizado)
        .then(
            (response)=>{
                MySwal.fire({
                    title: <strong>Tudo certo!</strong>,
                    html: <p>Aluno <strong>{response.data.nome}</strong> atualizado com sucesso!</p>,
                    icon: 'success'
                })
                this.props.history.push('/listAluno')
            }
        )

        .catch(
            (error)=>{
                MySwal.fire({
                    title: <strong>Ops!</strong>,
                    html: <p>Algo deu errado, tente novamente</p>,
                    icon: 'error'
                })
                console.log(error)
            }
        )
        //alert('Nome: ' + this.state.nome + this.state.curso + this.state.IRA)
        //this.setState({nome:'', curso:'', IRA:0})
    }
    render() {
        return(
            <div style={{marginTop:50}}>
                <h4>Editar Aluno</h4>
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
                        <input type='submit' className='btn btn-primary' value='ATUALIZAR'/>
                    </div>
                </form>
            </div>
        )
    }
}