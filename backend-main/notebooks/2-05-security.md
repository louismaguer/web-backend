# Security and Web

## A small security point 🔒

What difference between

````{div}
:class: center
HTTP and HTTP**S** ❓  
Yes yes it's the **S** of **S**ecure 😓
````

Roughly:

````{div}
:class: center
Wrapping the HTTP protocol in an encryption layer <br>
 to guarantee user security
```{image} media/https.jpg
:width: 35%
```
````

---

## HTTP a not safe thing?

`````{div}
:class: columns

````{div}
:class: sixty
***So yes basic HTTP is not secure***
````

````{div}
:class: fourty
```{div}
:class: center
<iframe src="https://giphy.com/embed/1FMaabePDEfgk" height="50" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
```
````
`````

`````{div}
:class: columns

````{div}
:class: fifty
```{div}
:class: center
<iframe src="https://giphy.com/embed/dZA4cLPCvSs1s5aCm7" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
```
````

````{div}
:class: fifty
***It's not very serious in many cases***  
But modern browsers are starting to be very strict on the subject
````

`````

---

## The risk of HTTP

<br>

`````{div}
:class: columns
````{div}
:class: fifty
```{image} media/http-not-safe.excalidraw.svg
:width: 100%
```
````

````{div}
:class: fifty
```{image} media/https-safe.excalidraw.svg
:width: 100%
```
````
`````

````{div}
:class: center
The principle is therefore to enclose the HTTP request and the information it contains  
in an encrypted message
````

---

## Encryption principles

In practice encryption works with a public key/private key system

````{div}
:class: center
```{image} media/timeline-tls.excalidraw.svg
```
````

---

## Certification Authority (CA)

````{div}
:class: center
**Trusted third party** <br>who will generate certificates allowing encryption and authentication of correspondents' identity
````

Possible to generate your own certificates yourself but they are not considered valid by standard clients (knowing that web browsers have a list of trusted CAs)

Open source software mainly uses the ***OpenSSL*** library

```{image} media/logos/openssl.svg
:width: 20%
```

<br><br>
To generate certificates for free there is the **Let's Encrypt** initiative
```{image} media/logos/lets-encrypt.svg
:width: 20%
```

```{div}
:class: smaller
in practice, a certificate is valid for a finite duration, of the order of 1 year, so it must be renewed regularly
```

---

## And now is it finished?

````{div}
:class: center
<iframe src="https://giphy.com/embed/I1nwVpCaB4k36" width="400" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

## Cookies 🍪

Let's take a snack break 🤤

````{div}
:class: center
<iframe src="https://giphy.com/embed/3o6MbitgftpbGFP3B6" width="480" height="362" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

````{div}
:class: center
It's part of these little ***hidden*** things in HTTP headers
````

---

## Concretely what is it?

 ````{div}
:class: center
An HTTP 🍪 is data that a server sends to a client
````

`````{div}
:class: columns

````{div}
:class: fifty
```{image} media/cookie1.excalidraw.svg
:width: 100%
```
````

````{div}
:class: fifty
```{image} media/cookie2.excalidraw.svg
:width: 100%
```
````
`````

````{div}
:class: center
stored on the client (in the browser) <br> and that the client **sends back again** to the server at each new request
````

````{div}
:class: center
```{image} media/cookie3.excalidraw.svg
:width: 40%
```
````

````{admonition} How does it work in concrete terms
:class: dropdown smaller

- the server sends a response to the client with a `Set-Cookie` header containing the cookie information
  ```http
  Set-Cookie: sessionId=abc123; Expires=Wed, 21 Oct 2021 07:28:00 GMT; Path=/; Secure; HttpOnly
  ```
- the client (browser) stores the cookie and associates it with the server's domain
- for each subsequent request to the same server, the client automatically includes the cookie in the request
  ```http
  Cookie: sessionId=abc123
  ```
- now, this is subject to security considerations, like CORS, but that's the general idea
````

---

## What interest?

Cookies are there to enrich HTTP.

### The problem

````{div}
:class: center
HTTP = stateless protocol
````

Basically impossible for an HTTP server to know if two requests come from the same client or not 😵‍💫

````{div}
:class: center
How to stay authenticated then?
````

---

### The solution

````{div}
:class: center
Cookies 🍪 because it leaves crumbs
````

Concretely we will be able to store:

````{div}
:class: center
A session ID, user preferences (light/dark theme, language, ...)
````

---

## Setting cookies

Nothing simpler, in the server response header just add
<br>
````{div}
:class: center
`Set-Cookie: <name>=<value>; <attributes...>`
````

Cookie Attributes

- `Expires`: lifetime (date/time)
- `Max-Age`: lifetime (seconds)
- `Domain`: domain names for which the cookie is sent back
- `Path`: particular path for which the cookie is sent back
- `Secure`: if set, we only send the cookie on https, and not http
- `HttpOnly`: if set, we cannot access the cookie via JavaScript
- `SameSite`: defines if we send the cookie in *cross-site requests*

For example, go to <https://www.mat.minesparis.psl.eu> and find the `PHPSESSID` cookie

---

### The gory details

`````{div}
:class: smaller

````{div}
more details here on MDN, notably
  - [in terms of lifetime, regarding `Expires` and `Max-Age`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#removal_defining_the_lifetime_of_a_cookie)
  - [in terms of *scope* regarding `Domain` and `Path`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#define_where_cookies_are_sent)
  - [in terms of security, regarding `HttpOnly` and `Secure`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#security)
````

```{admonition} and *Third-Party Cookies* ?
:class: warning dropdown smaller

Finally regarding [`SameSite`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies#controlling_third-party_cookies_with_samesite), a rather thorny subject, that of [*third-party cookies*](https://developer.mozilla.org/en-US/docs/Web/Privacy/Guides/Third-party_cookies); what is it about?

  You go to `https://the-shop.com` which puts a cookie on you
  <br>
  a little later you consult `https://other-site.com` 
  <br>which makes an **indirect** request (e.g. a `fetch()` or an `<img>`)
  to `https://the-shop.com`
  <br>
  should we send the first cookie?
```

`````

---

## Some rules to follow

````{div}
:class: center
```{image} media/logos/cnil.svg
:width: 30%
```

<https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies>
````

- Internet users must be informed and give their consent before the deposit of certain cookies
  - ❌ Advertising tracking / social networks
  - ✔️ Cookie to say we refuse cookies [example](https://cpp.bmarchand.fr), shopping cart, authentication, ...
- Collect consent
  - Refuse button as visible as the accepted one
  - Possibility to choose cookies
  - Ease of withdrawal of consent

```{div}
:class: smaller
see also the GDPR:
<https://www.economie.gouv.fr/entreprises/reglement-general-protection-donnees-rgpd>
```

---

## Let's add a Cookie to our server

````{div}
:class: center
let's go to the `python/cookies` folder of the course
````

````{div}
run this code on your computer and look for cookies in the headers  

```{div}
:class: smaller
note that on Chrome, you can also inspect cookies in the browser via   
`DevTools > Application > Cookies`
```

```{admonition} You see too much?
:class: dropdown smaller

if you join the server on `localhost`, you might see a lot..  
well, much more than what the server puts itself  
how do you think this happens?

<details><summary>answer</summary>

the cookie is - roughly - <b>attached to a hostname</b>; so all cookies that will have been set by a server you have already joined via <code>localhost</code>, even which have nothing to do with this one, will be sent back in the request by the browser

</details>
```
````

---

## HTTP + 🍪 sufficient to do everything?

````{div}
:class: center
<br><br>

<iframe src="https://giphy.com/embed/XymaJlgorUL8vOfF88" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

---

## But why?

`````{div}
:class: columns
````{div}
:class: twenty
```{image} media/timeline-http.excalidraw.svg
:width: 100%
```
````

````{div}
:class: eighty

HTTP operation very rigid: **question/answer** oriented
<br>
**Impossible** for the server to be **at the origin** of the exchange: quite limiting actually 😮‍💨
<br><br>
forces Patrick to always ask if there is anything new for him...
````
`````

`````{div}
:class: columns

````{div}
:class: fifty
```{image} media/limitation1.excalidraw.svg
:width: 100%
```
````

````{div}
:class: fifty
```{image} media/limitation2.excalidraw.svg
:width: 100%
```
````

`````

---

## Websockets

````{div}
:class: center
In 2011, revolution: arrival of Websockets 🤯
````

`````{div}
:class: columns

````{div}
:class: sixty
<br><br>
```{div}
:class: center
**bi-directional** connection between client and server
<br>sometimes referred to as a *full-duplex* connection
<br>allows the server to ***push*** information to the client without the client having to ask for anything 😲
```
its short name: `ws` (or `wss` for the secure version)
````

````{div}
:class: fourty center
```{image} media/timeline-ws.excalidraw.svg
:width: 80%
```
````

`````

---

## How ws works

Very simply actually!

````{div}
:class: center
First step we establish a connection to a WebSocket server <br> i.e. <br>
`ws://my-super-server.com` or `wss://my-super-server.com`
````

````{div}
:class: center
Once the connection is established <br><br>
We simply need to keep on listening for particular events
````

Four types of events

````{div}
:class: center
`onopen` 📖, `onclose` 📕, `onerror` 🚨, `onmessage` 📥
````

And we attach an action to each event type

---

## For example&nbsp;:

See in the `python/raw-websockets` folder:

`````{div}
:class: columns smaller

````{div}
:class: fifty
the "ping-pong" protocol (actually "ping-gnip"):

- `ws-server.py`: a WebSocket server in Python
- `ws-client.py`: a WebSocket client in Python
- `ws-client.js`: a WebSocket client in JavaScript

it works but it has little interest  
let's say it has the merit of showing how it works
````

````{div}
:class: fifty
the "countdown" protocol, same logic:

- `python ws-server2.py` for the server
- `python ws-client2.py 3` will last 3 seconds
- `node ws-client2.js 3` same but in JS

this time it's more interesting, the client **sends to the server a number of
seconds**, and the server responds by counting down to 0
```` 
`````

````{div}
:class: smaller
⚠️ You see the keyword `await` that you don't know in Python 🐍  
It's related to asynchronous programming. For more details I encourage you to take a tour on the Mooc

```{div}
:class: center
*Python: from fundamentals to advanced language concepts*
```
````

---

## In practice

We'll see websockets again:

- after we've covered FastAPI, and we'll see [how to define websocket endpoints
  in FastAPI](/websockets#label-websockets)
- and in a more realistic example, a complete app that deals with notes  
  see step 11 in https://backend-fastapi-notes.info-mines.paris/scrollycoding

---

## In the next episode

`````{div}
:class: columns

````{div}
:class: fifty center
<iframe src="https://giphy.com/embed/xTiTnBdvZgewvjTBAs" width="400" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
````

````{div}
:class: fifty
```{div}
:class: center
<iframe src="https://giphy.com/embed/RbSmVaVGptW03Wjw3a" width="480" height="400" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
```
````
`````

````{div}
:class: center
An overview of the **FastAPI Framework** <br>
which will simplify your life for all Web developments
````
