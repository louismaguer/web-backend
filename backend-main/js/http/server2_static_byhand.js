/**
 * Same functionality as server1: serves static files
 * but this time we do the coding by hand
 */

import http from 'http';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PORT = 9001;

// Content type mapping
const contentTypes = {
    '.html': 'text/html',
    '.js': 'application/javascript',
    '.css': 'text/css',
    'default': 'text/plain'
};

const handle = (req, res) => {
    const clientAddr = req.socket.remoteAddress;
    console.log(`Server received req from ${clientAddr} for path ${req.url}`);

    let filePath = req.url;
    if (filePath === '/') {
        console.log("Hiya, asking for root, let's respond with index.html");
        filePath = '/index.html';
    }

    // Remove leading slash and resolve path
    const localPath = path.join(__dirname, filePath);

    fs.readFile(localPath, (err, content) => {
        if (err) {
            console.error(err);
            res.writeHead(404, { 'Content-Type': 'text/html' });
            res.end('<h1>404: File not found</h1>');
            return;
        }

        const ext = path.extname(localPath);
        const contentType = contentTypes[ext] || contentTypes.default;

        res.writeHead(200, { 'Content-Type': contentType });
        res.end(content);
    });
};

const server = http.createServer(handle);

console.log(`Open this in your browser:\nhttp://localhost:${PORT}/index.html`);
server.listen(PORT); 