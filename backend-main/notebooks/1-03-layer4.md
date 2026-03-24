# The Transport Layer 🚗

> We know how to navigate, how do we communicate now
>
> ➡️ We need the 4th layer of the OSI model

---

## Layer 4

> specification of how to send data <br>
> from server A to client B and vice versa.

`````{div}
:class: columns

````{div}
:class: thirty
Different established protocols&nbsp;:

- TCP
- UDP
- ...

````
````{div}
:class: seventy
**⚠️ Attention ⚠️**
````{div}
:class: center
The transport layer only defines the ***way*** two applications communicate
<br>
but does not specify the ***content*** of these communications
````
`````

---

## A server == an application?

Knowing the server's IP doesn't allow you to communicate with the application on that server yet
<br>

````{div}
:class: center
❓ By the way, can there be only one network application on a server or can we put several ❓
````

`````{div}
:class: columns

````{div}
:class: seventy-five
We can have several applications on the same server, and fortunately 🥳

The choice of the application we will talk to involves the notion of **_port_**

```{div}
:class: center
port = service entry door 🚪
```

```{div}
:class: center
$2^16$ = 65,536 ports per IP address  
(but of course we don't run that many applications on a server)
```
````

````{div}
:class: twenty-five
```{image} media/address-ports-bound.excalidraw.svg
```
````

`````

---

## Network packet anatomy

and here is what a packet looks like

```{image} media/packet-layers.excalidraw.svg
```

<br>

```{admonition} vocabulary
:class: dropdown
to be precise, in general we call *packet* level 3 and beyond  
when as here we include level 2 we generally speak of "frame"
```

---

## Standard ports

`````{div}
:class: columns

````{div}
:class: fifty

On a machine we have 2<sup>16</sup> = 65,536 ports
````

````{div}
:class: fifty
Some standardized ports:

service | port
-|-
SSH | 22
SMTP | 25
DNS | 53
HTTP | 80
HTTPS | 443
... | ...
````
`````

---

## TCP/IP

### Principle

````{div}
:class: center
**T**ransmission **C**ontrol **P**rotocol
````

is **the** historical protocol (Bob Kahn and Vinton Cerf, September 1973), which owes its longevity to its robustness and reliability.

````{div}
:class: center
Today when you browse the web<br>most exchanges that take place between your browser and websites are based on TCP
````

<br>
The principle of TCP is very simple and breaks down into three steps:

- connection establishment
- data transfer
- connection termination

---

### TCP/IP: open

`````{div}
:class: columns

````{div}
:class: fourty
```{image} media/tcp-handshake.excalidraw.svg
```
````

````{div}
:class: sixty
The connection of a client to a TCP server breaks down into three steps

```{div}
:class: center
___three way handshake___
```

in the following way:

- 1️⃣ Client: Hello server can you hear me&nbsp;?
  <br><br>
- 2️⃣ Server: Yes I hear you and you?
  <br><br>
- 3️⃣ Client: Yes it's good I hear you
  <br><br>

````
`````

---

### TCP/IP: close

`````{div}
:class: columns

````{div}
:class: fourty

```{image} media/tcp-close.excalidraw.svg
```
````

````{div}
:class: sixty
Closure in 4 steps
<br><br>

- 1️⃣ Client: I'm done
  <br><br>
- 2️⃣ Server: Ok noted
  <br><br>
- 3️⃣ Server: me too I have nothing more to tell you
  <br><br>
- 4️⃣ Client: Ok see you next time
````
`````

---

## Let's see how it really works

```{div}
:class: center
let's go see the `python/tcp` folder of the course
```

---

## TCP a rich thing 🤑

TCP takes care of 
- retransmissions in case of packet loss,
- ordering packets in case they arrive in the wrong order, 
- and flow control to avoid congestion, etc..
  
````{div}
:class: center
✅ the connection is extremely reliable and there is little chance of having misses
````

However this reliability is not free 💰️
````{div}
:class: center
❌ it is accompanied by a relatively high cost in terms of exchanges
````

That's why there's an alternative to TCP 😯

---

## UDP

The UDP protocol (User Datagram Protocol) is complementary to the TCP protocol. Created by David Reed in 1980.

Use cases:

````{div}
:class: center
Fast data transmission and reception of the whole  - **not imperative**
````

````{div}
:class: center
TCP = very reliable but slow

*vs*
<br>

UDP = fast but unreliable
````

UDP applications are numerous, essentially **everything streaming**, for example:

````{div}
:class: center
```{image} media/udp-applications.excalidraw.svg
```
````
