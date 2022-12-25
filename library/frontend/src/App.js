import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import UserList from './components/User.js'

class App extends React.Component {
  
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'users': []
        }
    }

    componentDidMount() {
        const users = [
            {
                'id': '1',
                'username': 'Lena',
                'email': 'email@email.com'
            },
            {
                'id': '2',
                'username': 'Lena1',
                'email': 'email1@email.com'
            }
        ]
        const authors = [
            {
                'first_name': 'Александр',
                'last_name': 'Грин',
                'birthday_year': 1880
            },
            {
                'first_name': 'Александр',
                'last_name': 'Пушкин',
                'birthday_year': 1799
            }
        ]
        this.setState(
            {
                'users': users,
                'authors': authors
            }
        )
    }

    render () {
        return (
                <div>
                    Привет
                    <UserList users={this.state.users} />
                    <AuthorList authors={this.state.authors} />
                </div>
        )
    }
}

export default App;
