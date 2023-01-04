import React from 'react'


const ArticleItem = ({article}) => {
    return (
        <tr>
            <td>
                {article.name}
            </td>
            <td>
                {article.author}
            </td>
            </tr>
    )
}

const ArticleList = ({articles}) => {
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Author
            </th>
                {articles.map((article_) => <ArticleItem article={article_} />)}
        </table>
    )
}

export default ArticleList;
