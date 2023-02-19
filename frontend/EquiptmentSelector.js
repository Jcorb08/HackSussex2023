alert("String")
let equiptment = document.querySelectorAll(".equiptment")
for (let index = 0; index < equiptment.length; index++) {
        equiptment[index].addEventListener("click",(e) =>
        {
                let id = e.target.getAttribute("id")
                console.log(id)
                selectequiptment(id) 
        })
}

function selectequiptment(i)
{
        for (let index = 0; index < equiptment.length; index++) {
                equiptment[index].classList.remove("active")
        }
        equiptment[i].classList.add("active")
}
                console.log(id)

console.log(equiptment)