# RSA Communication Simulator

A simple Python project I made to understand how RSA encryption works.

## What is RSA?

RSA (Rivest–Shamir–Adleman) is a public-key encryption technique based on the difficulty of factoring large numbers.

RSA uses two keys:

* **Public key** — `(e, n)`
* **Private key** — `(d, n)`

Each person in this project has their own public and private key.

## How RSA Works

First, two prime numbers `p` and `q` are chosen.

```text
n = p × q

φ(n) = (p-1)(q-1)
```

Then `e` is chosen such that:

```text
1 < e < φ(n)
gcd(e, φ(n)) = 1
```

`d` is calculated such that:

```text
ed ≡ 1 (mod φ(n))
```

The keys are:

```text
Public Key  = (e, n)
Private Key = (d, n)
```

Encryption:

```text
c = m^e mod n
```

Decryption:

```text
m = c^d mod n
```

The mathematical reason decryption gives back the original message is based on Euler's theorem.

## Project

The program simulates communication between three people:

```text
A
B
C
```

A person can:

1. Send a message
2. Receive a message
3. Log out
4. Exit the program

When sending a message, the receiver's **public key** is used for encryption.

When receiving a message, the receiver's **private key** is used for decryption.

## Example

```text
A sends a message to B

Message

B's Public Key

Encrypted Message

B's Private Key

Original Message
```

## Note

This is an **educational implementation** of RSA.

It uses small primes and basic textbook RSA, so it is **not suitable for real-world secure communication**.

The purpose of this project is to understand the mathematics and implementation of RSA.
