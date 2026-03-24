// client.js
import { connect } from "net";

const PORT = 3500;
const HOST = "127.0.0.1";

const client = connect(PORT, HOST, () => {
    console.log("Connected to server");

    const message = "Hello server";
    console.log(`Sending: ${message}`);
    client.write(message);
});

let receivedData = "";

client.on("data", (data) => {
    receivedData += data.toString();
});

client.on("end", () => {
    console.log(`Received from server:\n>>>\n${receivedData}\n<<<`);
    client.end();
});

client.on("error", (err) => {
    console.error(`Connection error: ${err.message}`);
});

