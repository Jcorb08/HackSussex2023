//alert("String")
let submit = document.querySelectorAll(".submit")
for (let index = 0; index < submit.length; index++) {
        submit[index].addEventListener("click",(e) =>
        {
                let id = e.target.getAttribute("id")
                console.log(id)
                selectsubmit(id) 
        })
}

function selectsubmit(i)
{
        for (let index = 0; index < submit.length; index++) {
                submit[index].classList.remove("active")
        }
        submit[i].classList.add("active")
}
                console.log(id)

console.log(submit)