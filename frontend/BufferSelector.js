//alert("String")
let buffer = document.querySelectorAll(".buffer")
for (let index = 0; index < buffer.length; index++) {
        buffer[index].addEventListener("click",(e) =>
        {
                let id = e.target.getAttribute("id")
                console.log(id)
                selectbuffer(id) 
        })
}

function selectbuffer(i)
{
        for (let index = 0; index < buffer.length; index++) {
                buffer[index].classList.remove("active")
        }
        buffer[i].classList.add("active")
}
                console.log(id)

console.log(buffer)