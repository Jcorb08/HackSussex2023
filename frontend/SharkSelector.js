//alert("String")
let sharks = document.querySelectorAll(".shark")
for (let index = 0; index < sharks.length; index++) {
        sharks[index].addEventListener("click",(e) =>
        {
                let id = e.target.getAttribute("id")
                console.log(id)
                selectshark(id) 
        })
}

function selectshark(i)
{
        for (let index = 0; index < sharks.length; index++) {
                sharks[index].classList.remove("active")
        }
        sharks[i].classList.add("active")
}
                console.log(id)

console.log(sharks)