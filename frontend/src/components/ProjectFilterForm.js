import React from 'react'
import axios from 'axios';
import Cookies from 'universal-cookie';
import PartProjects from './PartProjects.js'
import ProjectList from './Project.js';


class ProjectFilterForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'projects': [],
            'title': '',
            'token': '',
        }
    }

    handleTitleChange(event)
    {
        console.log(event.target.value); // ++
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
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

        axios.get('http://127.0.0.1:8000/api/projects', {headers})
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))

    }

    componentDidMount() {
        this.get_token_storage()
    }

    render() {
    return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <div className="form_group">
                <h1>Search by part of the project title</h1>
                <label htmlFor="title"></label>
                <input type="text" name="title" placeholder="part of the project title"
                    value={this.state.title} onChange={(event)=>this.handleTitleChange(event)} />
            </div>
            <h1>All projects</h1>
            <ProjectList projects={this.state.projects}/>
            <h1>Selection</h1>
            <PartProjects projects={this.state.projects} title={this.state.title}/>
        </form>
        );
    }
}

export default ProjectFilterForm