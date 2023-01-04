import React from 'react'
import {
    Link,
} from "react-router-dom";


const ProjectItem = ({project}) => {
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
        </tr>
    )
}


const ProjectList = ({projects}) => {
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
                {projects.map((project_) => <ProjectItem project={project_} />)}
        </table>
    )
}

export default ProjectList;
