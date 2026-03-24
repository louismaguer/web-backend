/**
 * Same functionality as server3
 * but this time we use a template to render the html
 * which makes it easier to maintain (separation of concerns)
 */

import http from 'http';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { render } from 'ejs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PORT = 9003;
const STATE = {};

// Read template file
const templatePath = path.join(__dirname, 'template.html.ejs');
const template = fs.readFileSync(templatePath, 'utf-8');

const server = http.createServer((req, res) => {
    const clientAddr = req.socket.remoteAddress;
    console.log(`Server received ${req.method} from ${clientAddr} for path ${req.url}`);

    if (req.method === 'GET') {
        // Handle GET request - display current state using template
        res.writeHead(200, { 'Content-Type': 'text/html' });
        
        // Render template with data
        const html = render(template, {
            client: clientAddr,
            path: req.url,
            data: STATE
        });
        
        res.end(html);
    } else if (req.method === 'POST') {
        // Handle POST request
        if (req.url === '/api/register') {
            let body = '';
            req.on('data', chunk => {
                body += chunk.toString();
            });

            req.on('end', () => {
                try {
                    const data = JSON.parse(body);
                    if (typeof data !== 'object' || data === null) {
                        res.writeHead(400, { 'Content-Type': 'text/plain' });
                        res.end('Expected a dictionary');
                        return;
                    }

                    // Update state with new data
                    Object.assign(STATE, data);
                    console.log('Server received data:', data);

                    res.writeHead(200, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify(STATE));
                } catch (error) {
                    res.writeHead(400, { 'Content-Type': 'text/plain' });
                    res.end('Invalid JSON data');
                }
            });
        } else {
            res.writeHead(404);
            res.end();
        }
    } else {
        res.writeHead(405);
        res.end();
    }
});

console.log(`Open this in your browser:\nhttp://localhost:${PORT}/index.html`);
server.listen(PORT); 