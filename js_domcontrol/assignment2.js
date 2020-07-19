const divs = document.querySelectorAll('div')

const onClick = function(event){
    let clicked = event.target
    let parent = clicked.parentElement

    //change color
    clicked.style.background = "blue"
    if(parent.tagName === "DIV"){
        parent.style.background = "red"
    }

    //set other divs to default color
    divs.forEach(function(div){
        if(div !== clicked && div !== parent){
            div.style.background = "white"
        }
    })

}

divs.forEach(function(div){
    div.addEventListener('click', onClick)
})