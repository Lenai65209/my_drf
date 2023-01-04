import React from 'react';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import TodoList from './components/Todo.js';
import ProjectsFilter from './components/ProjectsFilter';

import {
    Link,
    Routes,
    Route,
} from "react-router-dom";


class Projects extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
        }
    }

        componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8000/api/projects')
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todos')
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div className='app-wrapper'>
                <h1>Page Projects</h1>

                <nav className='app-wrapper-nav'>
                    <li>
                        <Link to='/users'>Users</Link>
                    </li>
                </nav>
                <UserList users={this.state.users} />
                <nav className='app-wrapper-nav'>
                   <li>
                       <Link to='/todos'>Todos</Link>
                   </li>
                </nav>
                <TodoList todos={this.state.todos} />
                <nav className='app-wrapper-nav'>
                    <li>
                        <Link to='/projects'>Projects</Link>
                    </li>
                </nav>
                <Routes exact path='/projects/*'>
                    <Route index element={<ProjectList projects={this.state.projects} />}/>
                    <Route exact path=':projectId' element={<ProjectsFilter projects={this.state.projects}/>}/>
                </Routes>

            </div>
        );
    }
}
export default Projects;
