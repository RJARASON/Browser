//this is my first time using JAVASCRIPT [7:45PM,26th September, 2023| in Visual Studio code]
//I watch a video on youtube.

const inputbox=document.getElementById("inputbox");
const listcontainer=document.getElementById("list-container");

function AddTask(){
    if(inputbox.value===''){
        alert("Please, You must enter something!")
    }
    else{
        let li=document.createElement("li");
        li.innerHTML=inputbox.value;
        listcontainer.appendChild(li);
        let span=document.createElement("span")
        span.innerHTML="\u00d7"
        li.appendChild(span);
    }
    inputbox.value="";
    saveData();
}

listcontainer.addEventListener("click", function(e){
    if(e.target.tagName==="li"){
        e.target.classlist.toggle("checked");
        saveData();
    }
    else if(e.target.tagName==="SPAN"){
        e.target.parentElement.remove();
    }
}, false);

function saveData(){
    localStorage.setItem("data",listcontainer.innerHTML);
}
function showTask(){
    listcontainer.innerHTML=localStorage.getItem("data");
}
showTask();

function printtask(){
    prompt("Do you want to print?")
    alert("Print Accepted!")
    console.info(li);
    print(listcontainer);
}
