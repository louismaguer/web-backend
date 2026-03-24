// server.js
import { createServer } from "net";

const PORT = 3000;
const clients = new Set();

const server = createServer((socket) => {
    console.log("Client connected");
    clients.add(socket);

    socket.on("data", (data) => {
        console.log(`Received: ${data.toString()}`);
        const message = `Client says: ${data.toString()}`;
        clients.forEach(client => {
            if (client !== socket) {
                client.write(message);
            }
        });
    });

    socket.on("end", () => {
        console.log("Client disconnected");
        clients.delete(socket);
    });
});

server.listen(PORT, "127.0.0.1", () => {
    console.log(`Server listening on 127.0.0.1:${PORT}`);
});