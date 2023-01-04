import React from 'react';
import {useParams} from "react-router-dom";
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

const ProjectsFilter = ({projects}) => {
    let {projectId} = useParams()
    console.log(projectId)
    console.log('test')
    let filter_projects = projects.filter((project)=> String(project.id).includes(String(projectId))) /* не работает */
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
                {filter_projects.map((project_) => <ProjectItem project={project_} />)}
        </table>
    )
}

export default ProjectsFilter;
