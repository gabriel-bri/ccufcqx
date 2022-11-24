import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css' 
import {Link, Switch, Route} from 'react-router-dom'

import Home from "./components/Home";
import CreateAluno from "./components/aluno/CreateAluno";
import ListAluno from "./components/aluno/ListAluno";
import EditAluno from "./components/aluno/EditAluno";
import Dropdown from 'react-bootstrap/Dropdown';

function App() {
  return (
    <div className="container">
      <nav className='navbar navbar-expand-lg navbar-dark bg-dark'>
        <Link to={'/'} className='navbar-brand'>CRUD</Link>
          <Dropdown>
            <Dropdown.Toggle className='bg-dark'>
              Alunos
            </Dropdown.Toggle>

            <Dropdown.Menu>
              <Dropdown.Item>
                <Link to={'/'} className='nav-link'>
                  Home
                </Link>
              </Dropdown.Item>
              <Dropdown.Item>
                <Link to={'/createAluno'} className='nav-link'>
                  Criar Alunos
                </Link>
              </Dropdown.Item>

              <Dropdown.Item>
                <Link to={'/listAluno'} className='nav-link'>
                  Listar Alunos
                </Link>
              </Dropdown.Item>

            </Dropdown.Menu>
          </Dropdown>
        {/* <div className='collapse navbar-collapse' id='navbarSupoortedContent'>

          <ul className='navbar-nav mr-auto'>

            <li className='nav-item'>

            </li>

            <li className='nav-item'>
              <Link to={'/createAluno'} className='nav-link'>
                Create Aluno
              </Link>
            </li>

            <li className='nav-item'>
              <Link to={'/listAluno'} className='nav-link'>
                List Aluno
              </Link>
            </li>

          </ul> */}

        {/* </div> */}

      </nav>
        <h2>Projeto Crud</h2>
        <Switch>
          <Route exact path='/' component={Home}></Route>
          <Route path='/createAluno' component={CreateAluno}></Route>
          <Route path='/listAluno' component={ListAluno}></Route>
          <Route path='/editAluno/:id' component={EditAluno}></Route>                    
        </Switch>
    </div>
  );
}

export default App;
