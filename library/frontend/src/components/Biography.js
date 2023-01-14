import React from 'react'


const BiographyItem = ({biography}) => {
    return (
        <tr>
            <td>
                {biography.text}
            </td>
            <td>
                {biography.author}
            </td>
        </tr>
    )
}


const BiographyList = ({biographies}) => {
    return (
        <table>
            <th>
                Text
            </th>
            <th>
                Author
            </th>
                {biographies.map((biography_) => <BiographyItem biography={biography_} />)}
        </table>
    )
}

export default BiographyList;
