import React from 'react'


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.users}
            </td>
        </tr>
    )
}


const TodoList = ({todos}) => {
    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Text
            </th>
            <th>
                Users
            </th>
                {todos.map((todo_) => <TodoItem todo={todo_} />)}
        </table>
    )
}

export default TodoList;

