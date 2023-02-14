import React from 'react'


class BookForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {name: '', authors: []}
    }
    handleChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }
    handleAuthorChange(event)
    {
        if(!event.target.selectedOptions){
            this.setState({
                "authors":[]
            })
            return;
        }
        let authors = []
        for(let option of event.target.selectedOptions){
            authors.push(option.value)
        }
        console.log(authors)
        this.setState({"authors": authors})
    }

    handleSubmit(event) {
        this.props.createBook(this.state.name, this.state.authors)
        event.preventDefault()
    }
    render() {
    return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <h1>'Only for authorized users'</h1>
            <div className="form_group">
                <label htmlFor="name"></label>
                <input type="text" name="name" placeholder="name"
                    value={this.state.name} onChange={(event)=>this.handleChange(event)} />
            </div>
            <select name="authors" multiple onChange={(event)=>this.handleAuthorChange(event)} >
            {this.props.authors.map((author) => <option value={author.id}>{author.first_name} {author.last_name}</option>)}
            </select>
            <input type="submit" value="Submit" />
        </form>
        );
    }
}
export default BookForm