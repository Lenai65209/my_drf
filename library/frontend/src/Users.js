import React from 'react';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import TodoList from './components/Todo.js';

import {
    Link
} from "react-router-dom";


class Users extends React.Component {

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
                <h1>Page Users</h1>
                <UserList users={this.state.users} />
                <nav className='app-wrapper-nav'>
                    <li>
                        <Link to='/projects'>Projects</Link>
                    </li>
                </nav>
               <ProjectList projects={this.state.projects} />
               <nav className='app-wrapper-nav'>
                   <li>
                       <Link to='/todos'>Todos</Link>
                   </li>
               </nav>
               <TodoList todos={this.state.todos} />
            </div>
        );
    }
}
export default Users;
