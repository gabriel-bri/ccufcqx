import React, {Component} from 'react'
import FirebaseContext from '../../utils/FirebaseContext'
import FirebaseService from '../../services/FirebaseService'

const EditPage = (props) => (
    <FirebaseContext.Consumer>
        { (contexto) => <EditAluno firebase={contexto} id={props.match.params.id}/>}
    </FirebaseContext.Consumer>
)

class EditAluno extends Component{
    
    constructor(props) {
        super(props)
        this.state = {nome:'', curso:'', IRA:0}
        this.setNome = this.setNome.bind(this)
        this.setCurso = this.setCurso.bind(this)
        this.setIRA = this.setIRA.bind(this)
        this.onSubmit = this.onSubmit.bind(this)
    }

    componentDidMount() {
        FirebaseService.retrieve(
            this.props.firebase.getFirestore(),
            (aluno) => {
                if(aluno) {
                    this.setState({
                        nome: aluno.nome,
                        curso: aluno.curso,
                        IRA: aluno.IRA
                    })
                }
            },
            this.props.id
        )
        // this.props.firebase.getFirestore().collection('estudantes').doc(this.props.id).get()

        // .then(
        //     (doc) => {
        //         this.setState({
        //             nome: doc.data().nome,
        //             curso: doc.data().curso,
        //             IRA: doc.data().IRA
        //         })
        //     }
        // )
        // .catch(error=>console.log(error))

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

        FirebaseService.edit(
            this.props.firebase.getFirestore(),
            (mensagem) => {
                if(mensagem === "Aluno atualizado com sucesso") {
                    alert("Aluno atualizado com sucesso")
                }
            },
            alunos,
            this.props.id

        )

        this.setState({nome:'', curso:'', IRA:0})

        // this.props.firebase.getFirestore().collection('estudantes').doc(this.props.id).set(
        //     {
        //         nome: this.state.nome,
        //         curso: this.state.curso,
        //         IRA: this.state.IRA
        //     }
        // )

        // .then(() => alert("Aluno atualizado com sucesso"))
        // .catch((error) => console.log(error))
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

export default EditPage