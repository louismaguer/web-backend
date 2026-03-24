// client.js
import { connect } from "net";
import { stdin, stdout } from "process";
import readline from "readline";

const PORT = 3000;
const HOST = "127.0.0.1";

const client = connect(PORT, HOST, () => {
    console.log("Connected to chat server");
});

const rl = readline.createInterface({
    input: stdin,
    output: stdout
});

client.on("data", (data) => {
    console.log(`\n${data.toString()}`);
    rl.prompt();
});

client.on("end", () => {
    console.log("Disconnected from server");
    process.exit(0);
});

client.on("error", (err) => {
    console.error(`Connection error: ${err.message}`);
});

rl.setPrompt("You: ");
rl.prompt();

rl.on("line", (line) => {
    if (line.toLowerCase() === "exit") {
        client.end();
        rl.close();
    } else {
        client.write(line);
    }
});