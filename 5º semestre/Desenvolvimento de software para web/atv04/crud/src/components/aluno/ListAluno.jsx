import React, {Component} from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

import Swal from 'sweetalert2'
import withReactContent from 'sweetalert2-react-content'
const MySwal = withReactContent(Swal)

export default class ListAluno extends Component{
    constructor(props) {
        super(props)
        this.state = {alunos:[]}
        this.apagarAlunoPorId = this.apagarAlunoPorId.bind(this)
    }

    apagarAlunoPorId(id){
        let alunosTemp = this.state.alunos

        for(let i = 0; i < alunosTemp.length; i++) {
            if(alunosTemp[i]._id === id){
                alunosTemp.splice(i, 1)
            }
        }

        this.setState({aluno:alunosTemp})
    }

    componentDidMount() {
        axios.get('http://localhost:3002/estudantes/list')
        // axios.get('http://localhost:3001/alunos')
        .then(
            (response)=>{
                this.setState({alunos:response.data})
                console.log(this.state.alunos)
            }
        )

        .catch(
            (error)=>{
                console.log("vish kkkk")
            }
        )
    }
    
    montarTabela() {
        if(!this.state.alunos) {
            return
        }

        return this.state.alunos.map(
            (aluno, i)=>{
                return <TableRow aluno={aluno} key={i} apagarAlunoPorId={this.apagarAlunoPorId}></TableRow>
            }
        )
    }

    render() {
        return(
            <div>
                <p>Listagem de alunos</p>
                <table className='table table-striped' style={{marginTop:20}}>
                    <thead>
                        <tr>
                            <td>ID</td>
                            <td>Nome</td>
                            <td>Curso</td>
                            <td>IRA</td>
                            <td colSpan='2' style={{textAlign: 'center'}}>Ações</td>
                        </tr>
                    </thead>
                    <tbody>
                        {this.montarTabela()}
                    </tbody>
                </table>
            </div>
        )
    }
}

class TableRow extends Component{
    constructor(props) {
        super(props)
        this.apagarAluno = this.apagarAluno.bind(this)
    }

    apagarAluno() {
        // console.log(this.props.aluno.id)
        axios.delete('http://localhost:3002/estudantes/delete/' + this.props.aluno._id)
        // axios.delete('http://localhost:3001/alunos/' + this.props.aluno.id)
        .then(
            (response)=>{
                // alert("Registro apagado com sucesso!")
                MySwal.fire({
                    title: <strong>Tudo certo!</strong>,
                    html: <p>Aluno apagado com sucesso!</p>,
                    icon: 'success'
                })
                this.props.apagarAlunoPorId(this.props.aluno._id)
            }
        ) 

        .catch(
            (error)=>{
                MySwal.fire({
                    title: <strong>Ops!</strong>,
                    html: <p>Algo deu errado, tente novamente</p>,
                    icon: 'error'
                })
                console.log("ERRO")
            }
        )
    }
    
    render(){
        return(
            <tr>
                <td>{this.props.aluno._id}</td>
                <td>{this.props.aluno.nome}</td>
                <td>{this.props.aluno.curso}</td>
                <td>{this.props.aluno.IRA}</td>
                <td style={{textAlign:"center"}}>
                    <Link to={'/editAluno/' + this.props.aluno._id} className='btn btn-primary'>Editar</Link>
                </td>
                <td style={{textAlign:"center"}}>
                    <button className='btn btn-danger' onClick={() => this.apagarAluno()}>Apagar</button>
                </td>
            </tr>
        )
    }
}