import React from 'react';
import {useParams} from "react-router-dom";


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

const ArticleAuthor = ({articles}) => {
    let {authorId} = useParams()
    console.log(authorId)
    console.log('test')
    /* Пример с урока работает 50 на 50 ). Повторила просто так. Какой-то странный поиск.
    Как будто чего-то не хватает. С проектами решение работает, projectId ищу в project.id*/
    let filter_articles = articles.filter((article)=> article.author.includes(parseInt(authorId)))
    console.log('test1')
    console.log(filter_articles)
    console.log('test2')
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Author
            </th>
                {filter_articles.map((article_) => <ArticleItem article={article_} />)}
        </table>
    )
}

export default ArticleAuthor;
