import React from 'react'


class LoginForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {username: '', password: ''}
    }
    handleChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }
    handleSubmit(event) {
        this.props.get_token(this.state.username, this.state.password)
        event.preventDefault()
    }
    render() {
    return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <input type="text" name="username" placeholder="username"
                    value={this.state.username} onChange={(event)=>this.handleChange(event)} />
            <input type="password" name="password" placeholder="password"
                    value={this.state.password} onChange={(event)=>this.handleChange(event)} />
            <input type="submit" value="Login" />
        </form>
        );
    }
}
export default LoginForm