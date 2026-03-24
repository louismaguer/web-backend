# The Network: Principle

## Infrastructure

First of all, what is a network?

````{div}
:class: center
Well, it's an **infrastructure** that we use to transmit data.
````

In its most elementary version, a network consists of two devices connected to each other, by a network cable for example.

The important point here is that a device connected to the network must have a **network interface**, a component capable of communicating, i.e., sending and receiving a signal.

For example, your laptop has two network interfaces: the RJ45 port and the wifi card. The signal that passes through the network interface is a binary signal.

````{div}
:class: center
**⚠️ The device itself doesn't need to know the meaning of this signal,
<br> because it's a program running behind the network interface that will handle processing the signal in question ⚠️**
````

---

## Small parenthesis

### Supercomputer: a peer-to-peer model

`````{div}
:class: columns

````{div}
:class: thirty
```{image} media/cluster1.jpg
```
````

````{div}
:class: thirty
```{image} media/cluster2.jpg
```
````

````{div}
:class: rows thirty

```{iframe} https://www.youtube.com/embed/4r6frld1UNE?autoplay=1&mute=1&loop=1&controls=0&playlist=4r6frld1UNE
```

```{iframe} https://www.youtube.com/embed/90-kA3wYuoM?autoplay=1&mute=1&loop=1&controls=0&playlist=90-kA3wYuoM
```
````

`````

---

## High Performance Computing

````{div}
:class: center
Divide and conquer
````

`````{div}
:class: columns

````{div}
:class: thirty
```{figure} media/aube_dd.png
domain decomposition
```
````

````{div}
:class: thirty
```{figure} media/dd.png
Each subdomain "sent" <br> to a computing machine
```
````

````{div}
:class: thirty
```{figure} media/dd_zoom.png
Each subdomain "exploded" by packet of elements <br>for integration of the behavior law
```
````

`````

At the level of each subdomain:

- Distributed algebraic operations
- Resolution of local problems (DD solvers)

but let's close the parenthesis, we're not here to talk about HPC but about networks!

---

## Different network qualities

Network quality, a little thing that matters depending on the application 🚀

<!-- <button onclick="plot_network()"> xxx no longer working - click me 📈 </button> 

````{div}
:class: center
<div id="plot_network"></div>
````
-->

Generally we talk about three qualities:

- **Bandwidth**: the amount of data that can be transmitted per unit of time (in bits per second, bps)
- **Latency**: the time needed for a data packet to reach its destination
- **Reliability**: the probability that data is transmitted without error

````{div}
:class: center
⏳️ In large simulations, communication time can represent 20% of computation time 💣
````

---

## OSI Model

``````{div}
:class: columns

`````{div}
:class: fifty
````{div}
:class: center
```{image} media/osi-model.excalidraw.svg
```
````
`````

````{div}
:class: fifty
<br>

**O**pen **S**ystem **I**nterconnexion
<br><br>

**Standard** established <br>by the ISO committee in 1984
<br><br>

**Objectives**:
<br>

```{div}
:class: center
standardize communications<br> between devices on a network
```
<br><br>

```{admonition} Note on layers 5 and 6
:class: warning admonition-small
These layers were in that original model, but are often ignored in favor of the TCP/IP model, which has only 4 layers
(Link, Internet, Transport, Application).
```

````

``````

---

## Addressing

````{div}
:class: center
Associate with each interface of each machine on a network a unique address<br />
unique as in, there's no other machine on the world with the same address
````

<br>

This address can be _temporary_ or _fixed_.  
Also in many modern setup, an interface can have _several addresses_.

<br>

This is what we call the IP address, for _Internet Protocol_.  
The IP (v4) address of a network interface is written as a combination of four numbers between 0 and 255.

````{div}
:class: center
```{image} media/ip-address.excalidraw.svg
:width: 30%
```
````

`````{div}
:class: smaller

so there are two parts: the network address (often on 24 bits) and the host address (often on 8 bits)  
when we need to write the address of a network we write it like this the number of bits of the network address
````{div}
:class: center
```{image} media/ip-address-subnet.excalidraw.svg
:width: 20%
```
````
`````

---

### IPv6 Addresses

**in 2011** was predicted **the exhaustion 💣 of available IP addresses**!...

2<sup>32</sup> = 4,294,967,296 that is about 1/2 address per person on earth  
(of course some people have more than others 😅)

Therefore the **IPv6** protocol was implemented (the old protocol was **v4**)

The principle is simple: go from an address on **32 bits** to an address on **128 bits**  
for example (in hex) `2001:0db8:0000:85a3:0000:0000:ac1f:8001`  
In fact we have so many addresses that we can give an IP address to every grain of sand on earth 🏖  ️

<br>

Currently deployed **but partially** - mainly, but not only, in the network core at operators

And why not everywhere, you might ask?  
well notably, the need for IPv6 is less important than expected thanks notably to NAT  
we'll talk about it again...

---

## Interconnection

### Local network

````{div}
:class: center
```{image} media/connection-local.excalidraw.svg
:width: 60%
```
````

---

### Remote network

````{div}
:class: center
```{image} media/connection-remote.excalidraw.svg
:width: 60%
````

---

## To summarize:

````{div}
:class: center
interconnection which actually constitutes **the third layer** of the OSI model
````

manages three elements:
<br>

- Routing
  ````{div}
  :class: center
  path between two machines in different networks, <br>path passing through gateways (routers)<br>these famous machines having interfaces in two distinct networks.
  ````

- Relaying
  ````{div}
  :class: center
  takes care, once the route is determined, <br>of transmitting the information from machine A to machine B
  ````

- Flow control
  ````{div}
  :class: center
  an optional but nevertheless essential functionality <br> which allows to decongest the entire network (in the broad sense). <br>A bit like Waze for data transit
  ````

---
(my-ip-address)=

## By the way: what is my IP?

`````{div}
:class: columns

````{div}
:class: fourty
How do I <br>find out my IP?
````

````{div}
:class: sixty
to start I clone the course (if not already done)  
on github: `ue22-p25/backend`  
and I go to the `python/ip-address` folder
````

`````

`````{div}
:class: columns
````{div}
:class: fitfy

a small code to ask an external site

```{literalinclude} ../python/ip-address/my-public-ip.py
```

````

````{div}
:class: fitfy
or to ask my OS(*)

```{literalinclude} ../python/ip-address/my-local-ip.py
```


````

`````

`````{div}
:class: columns

````{div}
:class: fifty

and I get (try it!)
```{code}
:linenos:
:emphasize-lines: 2
$ python my-public-ip.py
Public IP: 138.96.202.10
```
````

````{div}
:class: fifty
.. and it can be different! what is this mystery?
```{code}
:linenos:
:emphasize-lines: 2
$ python my-local-ip.py
Outgoing IP: 10.1.1.15
```
````

`````

(*) from the terminal, use: `ipconfig` on Windows, `ifconfig` on MacOS, `ip address show` on Linux

---

### NAT (Network Address Translation)

`````{div}
:class: columns

````{div}
:class: sixty-five
a little bird told me that:

- you will all have **the same public address**
- but for the second one you each have a **different local address**

in fact there are two types of IP addresses:

- public: those that are visible on the network, and which are unique
- private: those that are used **only** in a local network

````

````{div}
:class: thirty-five
<br><br>
reserved **private** addresses:

- `192.168.0.0/16` <br> 2<sup>16</sup> = 65,536 adresses

- `172.16.0.0/12` <br> 2<sup>20</sup> = 1,048,576 adresses

- `10.0.0.0/8` <br> 2<sup>24</sup> = 16,777,216 adresses
````
`````

````{div}
:class: center
```{image} media/nat-routing.excalidraw.svg
:width: 125%
```
````

---

## Domain names in all this!

Remembering IP addresses is still not super 🤯!

````{div}
:class: center
For example imagine that you had to remember `91.134.82.158` [^oasis-ip]
<br/>to know the classrooms .... <strike>we wouldn't see you often!</strike>
````

[^oasis-ip]: this is the IP address of `oasis.minesparis.psl.eu`

--

For this in the Internet infrastructure there is a magic thing, the:

````{div}
:class: center
**DNS** = **D**omain **N**ame **S**ystem
````

Basically it's the service that makes the association between a domain name and an IP address.

---

### DNS from the terminal

`````{div}
:class: columns

````{div}
:class: fifty

```bash
# several utilities to make DNS queries

$ nslookup oasis.minesparis.psl.eu
Server:		192.168.0.1
Address:	192.168.0.1#53

Non-authoritative answer:
Name:	oasis.minesparis.psl.eu
*Address: 91.134.82.158
```

````

````{div}
:class: fifty
```bash
$ host oasis.minesparis.psl.eu
*oasis.minesparis.psl.eu has address 91.134.82.158
```

```bash
$ dig @8.8.8.8 oasis.minesparis.psl.eu A +noall +answer

; <<>> DiG 9.10.6 <<>> @8.8.8.8 oasis.minesparis.psl.eu A +noall +answer
; (1 server found)
;; global options: +cmd
*oasis.minesparis.psl.eu. 161	IN	A	91.134.82.158
```
````

`````
