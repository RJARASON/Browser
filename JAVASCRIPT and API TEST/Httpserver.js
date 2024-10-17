const http = require("http");
const https=require('https')

async function http(){
  const server = http.createServer((req, res) => {
    if (req.url === "/") {
      res.statusCode = 200;
      res.setHeader("Content-Type", "text/plain");
      res.end("Http server\n");
    } else if (req.url === "/about") {
      res.statusCode = 200;
      res.setHeader("Content-Type", "text/html");
      res.end(`<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Simulation</title></head><style>body{background-color: #5b5b5b;}#sim{background-color: #202020;border-radius: 15px;width: 80vh;height: 570px;margin: 10px 420px;}</style><body><div id="sim"></div></body></html>`);
    } else {
      res.statusCode = 404;
      res.setHeader("Content-Type", "text/html");
      res.end("404 Not Found\n");
    }
  });
  
  const PORT = 3000;
  server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/about`);
  });
}

async function https(){
  const server = https.createServer((req, res) => {
    if (req.url === "/") {
      res.statusCode = 200;
      res.setHeader("Content-Type", "text/plain");
      res.end("Https server\n");
    } else if (req.url === "/about") {
      res.statusCode = 200;
      res.setHeader("Content-Type", "text/html");
      res.end(`<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Simulation</title></head><style>body{background-color: #5b5b5b;}#sim{background-color: #202020;border-radius: 15px;width: 80vh;height: 570px;margin: 10px 420px;}</style><body><div id="sim"></div></body></html>`);
    } else {
      res.statusCode = 404;
      res.setHeader("Content-Type", "text/html");
      res.end("404 Not Found\n");
    }
  });
  
  const PORT = 3000;
  server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/about`);
  })
}