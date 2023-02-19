alert("String")
let equiptment = document.querySelectorAll(".equiptment")
for (let index = 0; index < equiptments.length; index++) {
        equiptments[index].addEventListener("click",(e) =>
        {
                let id = e.target.getAttribute("id")
                console.log(id)
                selectequiptment(id) 
        })
}

function selectequiptment(i)
{
        for (let index = 0; index < equiptments.length; index++) {
                equiptments[index].classList.remove("active")
        }
        equiptments[i].classList.add("active")
}
                console.log(id)

console.log(equiptments)