// function to send a post request to a specified endpoint with specified data
function PostReq(endpoint, data){
    // ../ just means we go up one level in the directory tree to the parent directory
    fetch(`../${endpoint}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(_ => window.location.reload()) // reloads the page to display changes
}

// event is triggered when all html elements are loaded
window.addEventListener("DOMContentLoaded", ()=>{
    // gets all elements with the entry class
    document.querySelectorAll(".entry").forEach(entry => {
        const message = entry.querySelector("#message"),
            id = entry.querySelector("#id")  
        
        // this event will be triggered when the div is unfocused, and will send the post request
        message.onchange = ()=> PostReq("update", {
            "id": id.innerHTML,
            "message": message.value
        })
    })
})

window.onmouseup = (e)=> {
    const entry = e.target.closest(".entry"), // this gets the table row element
        div = document.getElementById("delete") 

    // hide the delete button if we didnt click on any entry, or if we clicked on the textbox
    if (e.target.id=="message" || !entry)
        document.getElementById("delete").style.display = "none"
    
    else{
        // show the delete button
        div.style.display = "block"
        // position it at our cursor
        ;[div.style.left, div.style.top] = [`${e.clientX}px`, `${e.clientY}px`]

        // update the entry we clicked on
        div.entry = entry
    }
}

function DeleteEntry(){
    // make a post request with the posting id
    PostReq("delete", { 
        "id": document.getElementById("delete").entry.querySelector("#id").innerHTML 
    })
}