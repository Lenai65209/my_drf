import React from 'react';
import {useLocation} from "react-router-dom";

export const NotFound404 = () => {
    let {pathname} = useLocation()
    return (
        <div>
            <h1> Page not found {pathname}</h1>
        </div>
    )
}

export default NotFound404;