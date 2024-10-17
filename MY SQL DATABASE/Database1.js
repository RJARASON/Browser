const mysql=require('mysql')

const con=mysql.createConnection({
    host:"localhost",
    user:"Kodjo",
    password:"945295AZielp",
    database:"workdata"
})

con.connect(function(err){
    con.query("USE workdata",(err,result,field)=>{
        if(err) throw err;
        console.log(result);
    })
    if(err) throw err;
    console.log('Connected!');
})
con.connect(function(err){
    con.query("SELECT * FROM workdata",(err,result,field)=>{
        if(err) throw err;
        console.log(result);
    })
})