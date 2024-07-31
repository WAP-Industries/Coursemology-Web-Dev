function PostReq(endpoint, data){
    fetch(`../${endpoint}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(_ => window.location.reload())
}

window.addEventListener("DOMContentLoaded", ()=>{
    document.querySelectorAll(".entry").forEach(entry => {
        const message = entry.querySelector("#message"),
            id = entry.querySelector("#id")  

        message.onchange = ()=> PostReq("update", {
            "id": id.innerHTML,
            "message": message.value
        })
    })
})

window.onmouseup = (e)=> {
    const entry = e.target.closest(".entry"),
        div = document.getElementById("delete") 

    if (e.target.id=="message" || !entry)
        document.getElementById("delete").style.display = "none"
    
    else{
        div.style.display = "block"
        ;[div.style.left, div.style.top] = [`${e.clientX}px`, `${e.clientY}px`]

        div.entry = entry
    }
}

function DeleteEntry(){
    PostReq("delete", { 
        "id": document.getElementById("delete").entry.querySelector("#id").innerHTML 
    })
}