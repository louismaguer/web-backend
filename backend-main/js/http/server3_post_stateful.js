/**
 * This server is stateful, it keeps the data in a global variable STATE.
 * - one can record var=value using a POST request to /api/register
 * - a GET (on any path) will display the current state as HTML
 */

import http from 'http';

const PORT = 9002;
const STATE = {};

const server = http.createServer((req, res) => {
    const clientAddr = req.socket.remoteAddress;
    console.log(`Server received ${req.method} from ${clientAddr} for path ${req.url}`);

    if (req.method === 'GET') {
        // Handle GET request - display current state
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(`
            <h1>GET request</h1>
            <ul>
                <li>client=${clientAddr}</li>
                <li>path=${req.url}</li>
                <li>data_saved=${JSON.stringify(STATE)}</li>
            </ul>
        `);
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
    } 
    else if( req.method === "DELETE"){
        if (req.url === '/api/delete_all') {
            Object.keys(STATE).forEach(key => {
                delete STATE[key];
            });
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(STATE));
        }
        else if(  req.url.startsWith('/api/delete/')) {
            const key = req.url.split('/').pop();
            delete STATE[key];
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(STATE));
        }
        else {
            res.writeHead(404);
            res.end();
        }
    }
    else {
        res.writeHead(405);
        res.end();
    }
});

console.log(`Open this in your browser:\nhttp://localhost:${PORT}/index.html`);
server.listen(PORT); 