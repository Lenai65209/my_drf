import React from 'react'


class TodoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {projects: [], text: '', users: ''}
    }
    handleProjectChange(event)
    {
        if(!event.target.selectedOptions){
            this.setState({
                "projects":[]
            })
            return;
        }
        let projects = []
        for(let option of event.target.selectedOptions){
            projects.push(option.value)
        }
        console.log(projects)
        this.setState({"projects": projects})
    }
    handleTextChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }
    handleUserChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createTodo(this.state.projects, this.state.text, this.state.users)
        event.preventDefault()
    }
    render() {
    return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <h1>'Only for authorized users'</h1>
            <select name="projects" multiple onChange={(event)=>this.handleProjectChange(event)} >
            {this.props.projects.map((project) => <option value={project.id}>{project.title} {project.repo}</option>)}
            </select>
            <div className="form_group">
                <label htmlFor="text"></label>
                <input type="text" name="text" placeholder="text"
                    value={this.state.text} onChange={(event)=>this.handleTextChange(event)} />
            </div>
            <select name="users" onBlur= {(event)=>this.handleUserChange(event)}>
            {this.props.users.map((user) => <option value={user.id}>{user.username}</option>)}
            </select>
            <input type="submit" value="Submit" />
        </form>
        );
    }
}
export default TodoForm