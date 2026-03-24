# Data Encoding

Is layer 4 sufficient, or do we need something else?

<br>

````{div}
:class: center
With TCP or UDP we can do our data transfers between applications
````

<br>

````{div}
:class: center
In your opinion is it all good then or do we need something else?
````
<br><br>

---

````{div}
:class: center
🔎 Let's look at a concrete example 🔎
````

`````{div}
:class: columns

````{div}
:class: seventy
```{div}
:class: center
the folder `python/tcp-awkward-api`
<br>or<br>
[https://replit.com/@BasileMarchand/tcpexample?v=1](https://replit.com/@BasileMarchand/tcpexample?v=1)
<br>or<br>
[http://bit.ly/3YpoKDR](http://bit.ly/3YpoKDR)
<br>or<br>
```
````

````{div}
:class: thirty
<img src="media/qrcode/tcp_qrcode.png" width="65%">
````
`````

---

## A lock 🔒

````{div}
:class: center
Nothing standard in my data exchanges 😵‍💫

<br>

```{div}
:class: center
I created my own logic 

<br> but it's <strike>maybe</strike> certainly not in the eyes of others.
```

<br>

```{div}
:class: center
A bit of standardization wouldn't hurt ...
```

````

---

## By the way: data transfer ...

````{div}
:class: center
The big question that can arise is <br><br><br>in what format is it relevant to exchange data ❓
````

<br>
The OSI model does not really specify a data format other than saying it is binary 🤨
<br><br>
Layer 6 specifies things a bit in reality but it gives a fairly broad spectrum actually
<br>

````{div}
:class: center
😩 How do we do if we want to transmit <br><br> a packet of structured but heterogeneous data?
````

For example, a person's information:

````{div}
:class: center
Name, First name, Date of birth, number of children, ...
````

---

## JSON Serialization

````{div}
:class: center
<img src="media/serialization-json.excalidraw.svg" width="90%">
````

---

### Via Python 🐍 it's easy!

`````{div}
:class: columns

````{div}
:class: fifty
```python
import json
data = dict(name="jean", age=1)
serialized = json.dumps(data)
# serialized is now a string
```
````

````{div}
:class: fifty
```python
import json
serialized = '{"name": "jean", "age": 1}'
data = json.loads(serialized)
# data is now a dictionary
```
````
`````

---

## High level: layer 7 of the OSI model

This is where concrete things begin 🥳

<br>

````{div}
:class: center
***Layer 7 = Application layer***
````

<br>
Each "category" of application then specifies:

````{div}
:class: center
How communications are made between the client and the application
<br><br>
message format, expected content, ...
````

`````{div}
:class: columns
````{div}
:class: fifty
We talk about protocol, for example:

- File transfer 📂: (S)FTP, rsync
- Messaging ✉️: SMTP, POP, IMAP
- Remote sessions: telnet, SSH
- and...
````
````{div}
:class: fifty
<img src="https://media1.tenor.com/m/qRpNbT_IhBAAAAAd/appurajosh-appu.gif" height="200px">
````
`````
