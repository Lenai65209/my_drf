import React from 'react';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import AuthorList from './components/Author.js';
import UserList from './components/User.js';


class Home extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'users': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors')
            .then(response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div className='app-wrapper'>
                <h1>Page Home</h1>
                <h3>List of users</h3>
                <UserList users={this.state.users} />
                <h3>Authors</h3>
                <AuthorList authors={this.state.authors} />
            </div>
        );
    }
}
export default Home;