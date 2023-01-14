import React from 'react';
import axios from 'axios';
import './App.css';
import Cookies from 'universal-cookie';
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
            'token': '',
        }
    }

    logout(){
        this.set_token('')
        /*this.setState({'books':[]})*/
    }

    is_auth(){
        /*return this.state.token != ''*/
        return !!this.state.token
    }

    set_token(token){
        /*localStorage.setItem('token',token)*/
        console.log(token)
        const cookies = new Cookies()
        cookies.set('token',token)
        this.setState({'token':token}, () => this.load_data())

    }

    get_token_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username,password){
        /*console.log(username,password)*/
        const data = {username:username,password:password}
        axios.post('http://127.0.0.1:8000/api-token-auth/',data).then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль.'))
    }

    get_headers(){
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_auth()){
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
        }

        load_data() {
        const headers = this.get_headers()
            axios.get('http://127.0.0.1:8000/api/users', {headers})
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))


            axios.get('http://127.0.0.1:8000/api/projects', {headers})
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))

            axios.get('http://127.0.0.1:8000/api/todos', {headers})
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_storage()
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
