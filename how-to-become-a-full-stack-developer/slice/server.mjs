import { createServer } from "node:http";
import { readFile } from "node:fs/promises";

const skills = [
  { name: "HTML", stage: 1 },
  { name: "CSS", stage: 1 },
  { name: "JavaScript", stage: 2 },
  { name: "Node.js", stage: 3 },
];

const server = createServer(async (req, res) => {
  if (req.url === "/api/skills") {
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(skills));
  } else if (req.url === "/") {
    res.writeHead(200, { "Content-Type": "text/html" });
    res.end(await readFile(new URL("index.html", import.meta.url)));
  } else {
    res.writeHead(404).end("Not found");
  }
});

server.listen(3000, () => console.log("Listening on http://localhost:3000"));
