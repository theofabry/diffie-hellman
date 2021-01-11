from classes import Internet, Person, P, G

# Diffie-Hellman algorithm (simplified) example
if __name__ == '__main__':
    # Internet sees all traffic going between Alice and Bob
    internet: Internet = Internet()

    # Alice and Bob have a secret number they never share
    alice: Person = Person(name='Alice', secret_number=6, internet=internet)
    bob: Person = Person(name='Bob', secret_number=15, internet=internet)

    # They send their "half-keys" through the internet
    alice.send_half_key(bob)
    bob.send_half_key(alice)

    # With small values of P, an attacker could find secret numbers!
    for i in range(0, P):
        if pow(G, i) % P == alice.generate_half_key():
            print(f'Brute-forced Alice secret number! It is {i}')
        if pow(G, i) % P == bob.generate_half_key():
            print(f'Brute-forced Bob secret number! It is {i}')

    # Alice and Bob should have the same secret key
    alice.compute_secret_key()
    bob.compute_secret_key()
