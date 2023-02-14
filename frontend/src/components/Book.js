import React from 'react'


const BookItem = ({book, deleteBook}) => {
    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name}
            </td>
            <td>
                {book.authors}
            </td>
            <td>
                <td><button onClick={()=>deleteBook(book.id)} type='button'>Delete</button></td>
            </td>
            </tr>
    )
}


const BookList = ({books, deleteBook}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Name
            </th>
            <th>
                Authors
            </th>
            <th>
                'Only for authorized users'
            </th>
                {books.map((book_) => <BookItem book={book_} deleteBook={deleteBook}/>)}
        </table>
    )
}

export default BookList;
