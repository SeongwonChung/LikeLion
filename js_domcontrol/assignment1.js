const text = document.querySelector("#text")
const withspace = document.querySelector('#withspace')
const nospace = document.querySelector('#nospace')

const lengthCheck = function() {
    let input = text.value

    withspace.textContent = input.length
    nospace.textContent = input.replace(/ /g,"").length 
    /*
     / ... / 는 정규식 형태
    / /g 의 g는  전역검색 flag 
    */
}

//조건문활용
const colorChange = function() {
    let input = text.value

    if (input.length > 50) {
        withspace.classList.add("over50")
    }
    
    if (input.replace(/ /g, "").length > 50) {
        nospace.classList.add("over50")
    }
}

text.addEventListener('keyup', lengthCheck)
text.addEventListener('keyup', colorChange)