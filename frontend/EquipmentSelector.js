//alert("String")
let equipment = document.querySelectorAll(".equipment")
for (let index = 0; index < equipment.length; index++) {
        equipment[index].addEventListener("click",(e) =>
        {
                let id = e.target.getAttribute("id")
                console.log(id)
                selectequipment(id) 
        })
}

function selectequipment(i)
{
        for (let index = 0; index < equipment.length; index++) {
                equipment[index].classList.remove("active")
        }
        equipment[i].classList.add("active")
}
                console.log(id)

console.log(equipment)