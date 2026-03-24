// server.js
import { createServer } from "net";

const PORT = 3001;
const contacts = {
    "Jean Dupond": "jean.dupond@fake.com",
    "John Doe": "john.doe@fake.com"
};

const server = createServer((socket) => {
    console.log("Client connected");

    socket.on("data", (data) => {
        const request = JSON.parse(data.toString());
        console.log("Received:", request);

        let response = { status: false, msg: "", data: {} };

        switch (request.cmd) {
            case "help":
                response.status = true;
                response.msg = "Available commands: help, list, add";
                break;
            case "list":
                response.status = true;
                response.msg = "The list of all registered contacts";
                response.data = contacts;
                break;
            case "add":
                if (request.args && request.args.name && request.args.mail) {
                    contacts[request.args.name] = request.args.mail;
                    response.status = true;
                    response.msg = `${request.args.name} added to contacts`;
                } else {
                    response.msg = "Invalid arguments for add command";
                }
                break;
            default:
                response.msg = `Command ${request.cmd} unknown`;
        }

        socket.write(JSON.stringify(response));
        console.log("Sent:", response);
        socket.end();
    });
});

server.listen(PORT, "127.0.0.1", () => {
    console.log(`Server listening on 127.0.0.1:${PORT}`);
});
