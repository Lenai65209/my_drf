import React from 'react';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import AuthorList from './components/Author.js';
import UserList from './components/User.js';
import Navibar from './components/Navibar.js';
import Footer from './components/Footer.js';

// import Home from './Home.js';
import { Users } from './Users.js';
import { About } from './About.js';

import {
    BrowserRouter as Router,
    Route,
    Routes,
    Linc
} from "react-router-dom";

class App extends React.Component {

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

            <div>
                <Router>
                    <Navibar />
                    <Routes>
                        <Route exact path='/' component={App} />
                        <Route exact strict path='/users' component={Users} />
                        <Route exact strict path='/about' component={About} />
                    </Routes>
                    <UserList users={this.state.users} />
                    <AuthorList authors={this.state.authors} />
                </Router>
                <Footer />
            </div>
        )
    }
}

export default App;
