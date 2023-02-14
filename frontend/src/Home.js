import React from 'react';
import axios from 'axios';
import Cookies from 'universal-cookie';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import TodoList from './components/Todo.js';

import {
    Route,
    Routes,
    Link,
    Navigate
} from "react-router-dom";


class Home extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': '',
        }
    }

    deleteTodo(id) {
        console.log(id)
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todos/${id}`, {headers})
            .then(response => {
                this.load_data()
            }).catch(error => {
                this.setState({'todos': []})})
        }

    deleteProject(id) {
        console.log(id)
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}`, {headers})
            .then(response => {
                this.load_data()
            }).catch(error => {
                this.setState({'projects': []})})
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
                <h1>Page Home</h1>
                <h3>List of users</h3>
                <UserList users={this.state.users} />
                <h3>Projects</h3>
                <ProjectList projects={this.state.projects} deleteProject={(id)=>this.deleteProject(id)}/>
                <h3>List of todos</h3>
                <TodoList todos={this.state.todos} deleteTodo={(id)=>this.deleteTodo(id)}/>
            </div>
        );
    }
}
export default Home;