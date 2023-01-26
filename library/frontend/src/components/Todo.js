import React from 'react'


const TodoItem = ({todo, deleteTodo}) => {
    return (
        <tr>
            <td>
                {todo.id}
            </td>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.users}
            </td>
            <td>
                {todo.active ? "active" : "deleted"}
            </td>
            <td>
                <td><button onClick={()=>deleteTodo(todo.id)} type='button'>Delete</button></td>
            </td>
        </tr>
    )
}


const TodoList = ({todos, deleteTodo}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Project
            </th>
            <th>
                Text
            </th>
            <th>
                Users
            </th>
            <th>
                Active
            </th>
            <th>
                'Only for authorized users'
            </th>
                {todos.map((todo_) => <TodoItem todo={todo_} deleteTodo={deleteTodo} />)}
        </table>
    )
}

export default TodoList;

