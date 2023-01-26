import React from 'react';
import {useParams} from "react-router-dom";
import axios from 'axios';
import Cookies from 'universal-cookie';
import '../App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import UserList from '../components/User.js';
import ProjectList from '../components/Project.js';
import TodoList from '../components/Todo.js';
import ProjectsFilter from '../components/ProjectsFilter';


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.id}
            </td>
            <td>
                {project.title}
            </td>
            <td>
                {project.repo}
            </td>
            <td>
                {project.users}
            </td>
        </tr>
    )
}

const PartProjects = ({title, projects}) => {
    let {projectTitle} = useParams()
    console.log(projectTitle)
    console.log(title)
    console.log(projects)
    let filter_projects = projects.filter((project)=> String(project.title).includes(String(title))) /* не работает */
    console.log('test1')
    console.log(filter_projects)
    console.log('test2')
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Repo
            </th>
            <th>
                Users
            </th>
                 {title ? (filter_projects.map((project_) => <ProjectItem project={project_} />)) : <h1>enter the text in the search field</h1> }
        </table>
    )
}

export default PartProjects;
