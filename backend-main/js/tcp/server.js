import { createServer } from "net";

const PORT = 3500;

const server = createServer((socket) => {
    console.log("Client connected");

    socket.on("data", (data) => {
        console.log(`Received: ${data.toString()}`);
        const response = `data received by the server: ${data.toString()}`;
        socket.write(response);
        // socket.end()
    });

    socket.on("end", () => {
        console.log("Client disconnected");
    });
});

server.listen(PORT, "127.0.0.1", () => {
    console.log(`Server listening on 127.0.0.1:${PORT}`);
});

