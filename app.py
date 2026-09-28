import random
import math


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def generate_prime():
    while True:
        number = random.randint(10, 1000)

        if is_prime(number):
            return number


def generate_keys():
    p = generate_prime()

    q = generate_prime()

    while q == p:
        q = generate_prime()

    n = p * q

    phi = (p - 1) * (q - 1)

    e = 2

    while not (1 < e < phi and math.gcd(e, phi) == 1):
        e += 1

    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


def encrypt(message, public_key):
    e, n = public_key

    ciphertext = []

    for character in message:
        number = ord(character)
        encrypted_number = pow(number, e, n)
        ciphertext.append(encrypted_number)

    return ciphertext


def decrypt(ciphertext, private_key):
    d, n = private_key

    message = ""

    for encrypted_number in ciphertext:
        number = pow(encrypted_number, d, n)
        message += chr(number)

    return message


people = {}

for person in ["A", "B", "C"]:
    public_key, private_key = generate_keys()

    people[person] = {
        "public": public_key,
        "private": private_key
    }


while True:
    person = input("Who are you? ").upper()

    while person not in people:
        print("Invalid person.")
        person = input("Who are you? ").upper()

    while True:
        print()
        print(f"--- {person} ---")
        print("1. Send")
        print("2. Receive")
        print("3. Log out")
        print("4. Exit program")

        choice = input("Choice: ")

        if choice == "1":
            receiver = input("Send to: ").upper()

            while receiver not in people:
                print("Invalid recipient.")
                receiver = input("Send to: ").upper()

            message = input("Message: ")

            public_key = people[receiver]["public"]

            encrypted = encrypt(message, public_key)

            print("Encrypted:", encrypted)

        elif choice == "2":
            sender = input("From whom? ").upper()

            while sender not in people:
                print("Invalid sender.")
                sender = input("From whom? ").upper()

            encrypted_input = input("Encrypted text: ")

            ciphertext = [int(x) for x in encrypted_input.split(",")]

            private_key = people[person]["private"]

            message = decrypt(ciphertext, private_key)

            print("Decrypted:", message)

        elif choice == "3":
            break

        elif choice == "4":
            exit()

        else:
            print("Invalid choice.")