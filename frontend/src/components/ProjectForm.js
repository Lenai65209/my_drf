import React from 'react'


class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {title: '', repo: '', users: []}
    }
    handleTitleChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }
    handleRepoChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }
        handleUserChange(event)
    {
        if(!event.target.selectedOptions){
            this.setState({
                "users":[]
            })
            return;
        }
        let users = []
        for(let option of event.target.selectedOptions){
            users.push(option.value)
        }
        console.log(users)
        this.setState({"users": users})
    }

    handleSubmit(event) {
        this.props.createProject(this.state.title, this.state.repo, this.state.users)
        event.preventDefault()
    }
    render() {
    return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <h1>'Only for authorized users'</h1>
            <div className="form_group">
                <label htmlFor="title"></label>
                <input type="text" name="title" placeholder="title"
                    value={this.state.title} onChange={(event)=>this.handleTitleChange(event)} />
                <label htmlFor="repo"></label>
                <input type="text" name="repo" placeholder="repo"
                    value={this.state.repo} onChange={(event)=>this.handleRepoChange(event)} />
            </div>
            <select name="users" multiple onChange={(event)=>this.handleUserChange(event)} >
            {this.props.users.map((user) => <option value={user.id}>{user.username}</option>)}
            </select>
            <input type="submit" value="Submit" />
        </form>
        );
    }
}
export default ProjectForm