# other crypto & hashing technos

## Scope

A super-brief introduction to some other cryptographic techniques that you might
encounter in the wild

Typically private/public key cryptography is strong but expensive, so we also
need symmetric key cryptography for efficiency; a common pattern is to use
strong cryptography to establish a shared secret, and then use symmetric key
cryptography for the actual data exchange

in this part we'll cover

- Diffie-Hellman key exchange: a way to agree on a symmetric key
- AES: a symmetric key encryption algorithm
- SHA: a family of hash functions; these are also used all over the place and are not just for cryptography

---

## Diffie-Hellman Key Exchange

a method for two parties to establish a shared secret over an insecure channel  
typically used to *agree on a symmetric key* for further communication

`````{div}
:class: columns
````{div}
:class: sixty
based on simpler math:
- choose a large prime $p$ and a base $g$ for everyone to see
- then Alice and Bob choose their own private keys $a$ and $b$
- they both compute the same value:  
  $(g^a)^b = (g^b)^a = g^{ab} \mod p$

usage:  
- agree on a shared (symmetric) secret key,  
  e.g. once the TLS handshake is done
````
  ````{div}
:class: fourty
```{image} media/diffie-hellman.png
:width: 100%
```
````
`````

````{div}
:class: smaller
image from https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
````

---

## symmetric key cryptography - AES

As mentioned above, public key cryptography is expensive, so we also need
symmetric key cryptography for efficiency  

With a symmetric key, as the name suggests, the same key is used by both ends (Alice and Bob) to encrypt and decrypt messages

In this respect the most common algorithm is AES (Advanced Encryption Standard)  
See the gory details [here in wikipedia](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)

---

## SHA - Secure Hash Algorithm(s)

### Hash functions: why ?

- a hash function allows to create a fixed-size output (hash) from an arbitrary-size input
- it is expected to have several "good" properties:
  - deterministic: the same input always produces the same output
  - fast to compute: given an input, the hash should be computed quickly
  - pre-image resistant: given a hash, it should be hard to find an input that produces it
  - collision resistant: it should be hard to find two different inputs that produce the same hash
  - avalanche effect: a small change in input should produce a large change in output

### Usages

- actually, in computer science, they are **all over the place**
- you know of at least two tools that use them extensively:
  - `Python` - for hash tables, dictionaries, sets, etc..
  - `git` - for commit hashes, object storage, etc..
- and so many other places....

````{div}
:class: smaller
  for example: imagine: you want to spot **all the duplicated files** in a large directory tree - like, in all your computer  
  and the drive contains **1 million files**; how would you go about doing that ?
````

---

## a menagerie of hash functions

- historically: MD5 
  - widely used, but now considered broken
  - collision attacks are easy to find
  - output on 128 bits
- SHA-1
  - also considered broken - possible to generate collisions...
  - but **still heavily used** (git, TLS, etc..)
  - output on 160 bits
- **SHA-2**
  - SHA-256, SHA-512, etc..
  - widely used and considered secure
  - we will focus on this one
- SHA-3
  - a newer standard, based on a different construction (Keccak)
  - also considered secure

````{div}
:class: smaller
  SHA1 and SHA2 were designed by the NSA and for that reason are often considered, ahem, suspicious... esp. after the Snowden revelations
````

---

### SHA-2 (early 2000's)

- mostly 2 variants: SHA-256 and SHA-512 (gives the number of bits in the output)
- the details can be found e.g. [here in wikipedia](https://en.wikipedia.org/wiki/SHA-2)

but the general idea is as follows:
- a series of "rounds" of operations are performed
  - with each round mixing the input bits
  - to produce the input for the next round
- each round shuffles its input around, using a series of logical operations (in no particular order):
  - use of constants to initialize the state, as in e.g.  
    ✔ *first 32 bits of the fractional parts of the cube roots of the first 64 primes 2..311*
  - use of constants derived from the input, as in e.g.  
    ✔ *append K '0' bits, where K is the minimum number >= 0 such that (L + 1 + K + 64) is a multiple of 512*
  - bitwise AND, OR, XOR, NOT
  - rotate and shift operations

````{div}
:class: smaller
  I must say that implementing any of these algorithms in a low-level language could be a very good coding exercise, even if possibly  tedious at times 😉
````

---

## an example in Python code

- the `hashlib` module is part of the standard library
- the input must be of type `bytes` (use `.encode()` to convert a string)
- the result is of type `HASH`, and is commonly observed though the `.hexdigest()` method that yields a hexadecimal string

````{div}
:class: tiny-code

```python
In [1]: import hashlib

In [2]: # SHA-256 outputs 256 bits i.e. 64 hexa digits
   ...: hashlib.sha256(b"Pour tester la fonction de hachage SHA-256").hexdigest()
Out[2]: '99e7bfb9a23b5c8df17bc938120279585cf0de126aa84a7b7130ba2be67404ec'

In [3]: # regardless of the input size, be it small...
   ...: hashlib.sha256(b"tout petit").hexdigest()
Out[3]: '110af6c99fcf455de0db64a28c633d0b0e5341073c6ff3dfc73d9349703a595e'

In [4]: # or very large
   ...: hashlib.sha256(b"tres grand" * 1000).hexdigest()
Out[4]: '7a4b3b4472bc8edbba508efb0c458e7aa174b13ba5554004b801ce2d7780b7bb'

In [5]: # with almost the same input, we get .. something completely different
   ...: #                ↓ the only change is P becomes p
   ...: hashlib.sha256(b"pour tester la fonction de hachage SHA-256").hexdigest()
Out[5]: 'f02c78cd3b6a88379f5d0ace98539f3ceab86b59948248426de7ffdfe9777782'


In [6]: # SHA-1 yields shorter outputs, 160 bits only, i.e. 40 hexa digits
   ...: hashlib.sha1(b"Pour tester la fonction de hachage SHA-1").hexdigest()
Out[6]: '8d80362c01520158006bf2beef38d5ae08489570'
```

````

