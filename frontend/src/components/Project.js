import React from 'react'
import {
    Link,
} from "react-router-dom";


const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>
                {project.id}
            </td>
            <td>
                <Link to={`/projects/${project.id}`}>{project.title}</Link>
            </td>
            <td>
                {project.repo}
            </td>
            <td>
                {project.users}
            </td>
            <td>
                <td><button onClick={()=>deleteProject(project.id)} type='button'>Delete</button></td>
            </td>
        </tr>
    )
}


const ProjectList = ({projects, deleteProject}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Title
            </th>
            <th>
                Repo
            </th>
            <th>
                Users
            </th>
            <th>
                'Only for authorized users'
            </th>
                {projects.map((project_) => <ProjectItem project={project_} deleteProject={deleteProject} />)}
        </table>
    )
}

export default ProjectList;
