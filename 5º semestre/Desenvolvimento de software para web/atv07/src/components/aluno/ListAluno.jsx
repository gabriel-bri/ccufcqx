import React, {Component} from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

import FirebaseContext from '../../utils/FirebaseContext'
import FirebaseService from '../../services/FirebaseService'
import { firestore } from 'firebase'

const ListPage = () => (
    <FirebaseContext.Consumer>
        { (contexto) => <ListAluno firebase={contexto}/>}
    </FirebaseContext.Consumer>
)

class ListAluno extends Component{
    constructor(props) {
        super(props)
        this._isMounted = false
        this.state = {alunos:[], loading:true}
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
        console.log(this.props)
        this._isMounted = true
        this.setState({loading:true})
        FirebaseService.list(this.props.firebase.getFirestore(), 
            (alunos) => {
                if(alunos) {
                    if(this._isMounted) {
                        this.setState({alunos: alunos, loading: false})
                    }
                }
            }
        )
        //this.ref = this.props.firebase.getFirestore().collection('estudantes')
        //this.ref.onSnapshot(this.alimentarEstudantes.bind(this))
    }
    
    componentWillUnmount() {
        this._isMounted = false
    }

    alimentarEstudantes(query) {
        let alunos = []
        query.forEach(
            (doc) =>{
                const {nome, curso, IRA} = doc.data()
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
        if(this._isMounted) {
            this.setState({alunos:alunos, loading:false})
        }
    }
    montarTabela() {
        if(!this.state.alunos) {
            return
        }

        return this.state.alunos.map(
            (aluno, i)=>{
                return <TableRow aluno={aluno} key={i} apagarAlunoPorId={this.apagarAlunoPorId} firebase={this.props.firebase}></TableRow>
            }
        )
    }

    gerarConteudo() {
        if(this.state.loading) {
            return(
                <tr>
                    <td colSpan='6' style={{textAlign:"center"}}>
                        <div className="spinner-border" role="status">
                            <span className="sr-only"></span>
                        </div>
                    </td>
                </tr>
            )

        }

        else {
            return this.montarTabela()
        }
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
                        {this.gerarConteudo()}
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

    apagarAluno(id, nome) {
        let res = window.confirm(`Deseja apagar ${nome}?`)

        if(res) {
            // this.props.firebase.getFirestore().collection('estudantes').doc(id).delete()
            // .then(() =>alert('Registro deletado com'))

            // .catch(error=>console.log(error))
            FirebaseService.delete(
                this.props.firebase.getFirestore(),
                (mennsagem) => {
                    if(mennsagem === "Registro deletado com sucesso") {
                        alert("Registro deletado com sucesso")
                    }
                },
                id
            )
        }
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
                    <button className='btn btn-danger' onClick={() => this.apagarAluno(this.props.aluno._id, this.props.aluno.nome)}>Apagar</button>
                </td>
            </tr>
        )
    }
}
export default ListPage