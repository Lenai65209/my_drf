import React from 'react';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navibar from './components/Navibar.js';
import Footer from './components/Footer.js';

import Home from './Home.js';
import Users from './Users.js';
import Projects from './Projects.js';
import Todos from './Todos.js';
import { About } from './About.js';
import NotFound404 from './components/NotFound404.js';
import AuthorList from './components/Author.js';
import ArticlesAuthor from './components/ArticlesAuthor.js';
import BookList from './components/Book.js';
import ArticleList from './components/Article.js';

import {
    BrowserRouter as Router,
    Route,
    Routes,
    Link,
    Navigate,
} from "react-router-dom";

class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
            'articles': [],
            'users': [],
            'projects': [],
            'todos': [],
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

        axios.get('http://127.0.0.1:8000/api/books')
            .then(response => {
                const books = response.data
                this.setState(
                    {
                        'books': books
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/article_model')
            .then(response => {
                const articles = response.data
                this.setState(
                    {
                        'articles': articles
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
            <Router>
                <div className='app-wrapper'>
                  <div className='top'>
                    <Navibar />
                    <nav className='app-wrapper-nav'>
                        <li>
                            <Link to='/home'>Home</Link>
                        </li>
                        <li>
                            <Link to='/users'>Users</Link>
                        </li>
                        <li>
                            <Link to='projects'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/todos'>Todo</Link>
                        </li>
                        <li>
                            <Link to='/authors'>Authors</Link>
                        </li>
                        <li>
                            <Link to='/books'>Books</Link>
                        </li>
                        <li>
                            <Link to='/articles'>Articles</Link>
                        </li>
                        <li>
                            <Link to='/about'>About</Link>
                        </li>
                    </nav>
                    <Routes>

                        <Route exact strict path='/home' element={<Home />} />
                        <Route exact strict path='/users' element={<Users />} />
                        <Route exact strict path='/projects/*' element={<Projects />} />
                        <Route exact strict path='/todos' element={<Todos />} />

                        <Route path='/' element={<Navigate to='/authors'/>}/>
                        <Route exact path='/authors'>
                            <Route index element={<AuthorList authors={this.state.authors}/>}/>
                            <Route exact strict path=':authorId' element={<ArticlesAuthor articles={this.state.articles}/>}/>
                        </Route>
                        <Route exact strict path='/books' element={<BookList books={this.state.books}/>}/>
                        <Route exact strict path='/articles' element={<ArticleList articles={this.state.articles}/>}/>
                        <Route exact strict path='/about' element={<About />} />

                        <Route path='*' element={<NotFound404/>}/>
                    </Routes>
                  </div>
                  <div className='footer'>
                      <Footer />
                  </div>
                </div>
            </Router>

        )
    }
}

export default App;
