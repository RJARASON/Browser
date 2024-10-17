var mysql = require("mysql");

var con = mysql.createConnection({
  host: "localhost",
  user: "Kodjo",
  password: "945295AZielp",
});

con.connect(function (err) {
  if (err) throw err;
  console.log("Connected!");
});

con.connect(function (err) {
  con.query("USE kodjodb;", function (err, result, fields) {
    if (err) throw err;
    console.log(result);
  });
  con.query("SELECT * FROM joblist;", function (err, result, fields) {
    if (err) throw err;
    console.log(result);
  });
});
