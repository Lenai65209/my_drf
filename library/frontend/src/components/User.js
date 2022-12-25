import React from 'react'


const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.id}
            </td>
            <td>
                {user.username}
            </td>
            <td>
                {user.email}
            </td>
            </tr>
    )
}


const UserList = ({users}) => {
    return (
        <table>
            <th>
                id
            </th>
            <th>
                username
            </th>
            <th>
                email
            </th>
                {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}


export default UserList;