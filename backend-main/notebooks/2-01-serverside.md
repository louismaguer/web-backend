# What is a server?

## Recap from last time

````{div}
:class: center
Classic Client <-> Server architecture with peer-to-peer, three-tier variations, ...
````

`````{div}
:class: columns

````{div}
:class: fifty center
```{image} media/osi-model.excalidraw.svg
```
````

````{div}
:class: fifty center
An OSI model in 7 layers

```{image} media/ip-address.excalidraw.svg
:width: 40%
```
<br>

An HTTP(S) protocol for the web
```{image} media/http-post-request.excalidraw.svg
:class: center
```

`````

---

## What is the role of the server?

````{div}
:class: center
```{image} media/client-server.excalidraw.svg
:width: 60%
```
````

````{div}
:class: center
🥱 Wait and wait and wait ... 🥱
````

And from time to time 🥳 it must process a request!

---

## Serveur et serveur deux choses différentes

**_Attention_** there are two meanings to server ...

````{div}
:class: center
<iframe src="https://giphy.com/embed/xU9TT471DTGJq" width="480" height="365" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

### Le serveur hardware

````{div}
:class: center
```{image} https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1634&q=80
:width: 50%
```
````

````{div}
:class: center
It's the **physical or virtual** machine connected to the network that will receive data packets but will in no case take care of processing this data
````

---

### Le serveur hardware : différents types

````{div}
:class: center
Physical server vs virtual server (VPS)
````

`````{div}
:class: columns

````{div}
:class: fifty center
```{image} media/server-bare-metal.excalidraw.svg
```
````

````{div}
:class: fifty center
```{image} media/server-vps.excalidraw.svg
```
````
`````

Different solutions: On Premise vs Cloud (OVH, Azure, GCP, AWS, ... )

---

## Serveur et serveur deux choses différentes

### The "software" server

````{div}
:class: center
```{image} media/server-app.excalidraw.svg
:width: 65%
```
````

It's the application (in the software sense) that will take care of

````{div}
:class: center
**Receive**, **Process** and **Respond** to HTTP requests (or others for that matter)
````

Different solutions: Nginx (33%), Apache (27%), LiteSpeed (15%), Node.js(4%), IIS (4%), ...

````{div}
:class: smaller
Source: [https://w3techs.com/technologies/overview/web_server](https://w3techs.com/technologies/overview/web_server)
````

---

## Host multiple HTTP(S) servers on the same physical server?

````{div}
:class: center
YES 🎯 just share port 80 🤝
````

````{div}
:class: center
```{image} media/virtual-host.excalidraw.svg
:width: 80%
```
````

````{div}
:class: center
Just configure **Virtual Hosts** at the HTTP server level
````

---

### virtual hosts

Example of nginx config with two different sites on the same physical server


`````{div}
:class: columns

````{div}
:class: fifty center
```{image} media/servername-mines.png
:width: 40%
```
````

````{div}
:class: fifty center
```{image} media/servername-cpp.png
:width: 70%
```
````
`````

````{div}
:class: center
the "routing" between the two sites is done based on the `Host:` Header of the HTTP request
````

---

## A word about serverless

````{div}
:class: center
A traditional server spends its time waiting ... 🥱
````

````{div}
:class: center
**_A serverless is a server that does not wait_**
````

The principle is to break down processing into small **independent tasks** (functions) that will be executed **on demand**

`````{div}
:class: columns

````{div}
:class: fifty center

### Advantages

- No server management
- No fixed cost
- Scalable
````

````{div}
:class: fifty center

### Disadvantages/Difficulties

- Startup time
- Usage cost
- Debugging difficulty
- Stateless
````

`````

Lower cost for providers because they can optimize resource usage

---

## Do all servers do the same thing?

**Two applications**

````{div}
:class: center
Static vs dynamic sites
````

`````{div}
:class: columns

````{div}
:class: fifty center
<iframe src="https://cpp.bmarchand.fr/controlSection.html" width="100%" height="400px" frameBorder="0"></iframe>
````
````{div}
:class: fifty center
<iframe width="100%" height="400px" src="https://xkcd.com"></iframe>
````
`````

---

### Static site

````{div}
:class: center
The HTTP server only does one thing
<br>
**_read files_** html, png, jpg, pdf, .... and **_send the content to the client**

<br>

```{image} media/site-static.excalidraw.svg
:width: 90%
```

<br>see for example [the C++ course site](https://cpp.bmarchand.fr)

````

---

### Dynamic site (basic)

````{div}
:class: center
The HTTP server will have to work **with other services** <br>in order to produce the final result that can be sent to the client

```{image} media/site-dynamic.excalidraw.svg
:width: 90%
```

<br>For example: [a medium e-commerce site](https://vraimentbeau.com)
````

---

### Dynamic site (advanced)

````{div}
:class: center

On the other hand, the architecture behind a dynamic site can also be very very complex

```{image} media/site-cerebro.png
:width: 90%
```


<br>For example: [a development platform](https://rep.minesparis.psl.eu)
````

---

## Free hosting solutions

`````{div}
:class: columns

````{div}
:class: fifty

### Static sites

- Netlify
- Vercel
- Surge
- GitHub Pages (we are there!)
- readthedocs.io (we were there ;)
- GitLab Pages
- ...
````

````{div}
:class: fifty

### Dynamic sites

- Glitch
- Repl.it
- PythonAnywhere
- Vercel (serverless)
- ~~Heroku~~
- ...

````
`````

````{div}
:class: center
Lots of offers on the market, it's up to you to choose the one that suits you best

Attention however&nbsp;: **_Free_** does not mean **_without limit_**

````

---

## The web server: a need for performance 🚀

`````{div}
:class: columns bottom

````{div}
:class: .sixty
```{image} media/performance.excalidraw.svg
:width: 700px
```
````

````{div}
:class: fourty
How to make sure everyone

has a response in a reasonable time?

````
  ⏳️
`````

---

## Technical solutions

````{div}
:class: center
```{image} media/concurrency.excalidraw.svg
:width: 70%
```
````

````{div}
:class: center
Use of task parallelism processes/threads and/or asynchronous programming
````
