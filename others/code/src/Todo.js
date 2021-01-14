import React from 'react'

export default function Todo({
    todo,
    toggleTodo
}) {
    function handleTodoCLick() {
        toggleTodo(todo.id)
    }
    return ( <
        div >
        <
        label >
        <
        input type = "checkbox"
        onChange = {
            handleTodoCLick
        }
        checked = {
            todo.complete
        }
        /> {
            todo.name
        } <
        /label> <
        /div>		
    )
}