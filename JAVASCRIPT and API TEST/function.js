let accountnumbers=[
    "1441001234567",
    "1441002345678",
    "1441003456789",
    "1441004567891",
    "1441005678912",
    "1441006789123",
    "1441007891234"
]


num="Select account number:\n1) 1441001234567\n2) 1441002345678\n3) 1441003456789\n4) 1441004567891\n5) 1441005678912\n6) 1441006789123\n7) 1441007891234"


function numbers(){
    for(let numbers of accountnumbers){
    }
}
splitnum=num.split("\n")
console.log(splitnum);
// numbers()

function looknumber(){
    for(let num1 of accountnumbers){
    }
}

function getaccountnum(){
    let num1=accountnumbers.find(function(number){
        return number.slice("-3")==="567"
    })
    console.log(`Account Number selected ${num1}`);
}
getaccountnum();







// for (let i = 0; i < accountnumbers.length; i++) {
//     console.log(`${i+1} ${accountnumbers[i]}`);
//     }