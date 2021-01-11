from __future__ import annotations

P = 23
G = 5


class Internet:
    def __init__(self):
        self.seen_values = []

    def receive(self, value: int):
        print(f'Internet seen value {value}')
        self.seen_values.append(value)


class Person:
    def __init__(self, name: str, secret_number: int, internet: Internet):
        self.name = name
        self.received_half_key: int = 0
        self.secret_number = secret_number
        self.internet = internet
        self.secret_key: int = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def generate_half_key(self) -> int:
        return pow(G, self.secret_number) % P

    def send_half_key(self, recipient: Person):
        half_key: int = self.generate_half_key()
        print(f'Half key {half_key} sent to {recipient.name} by {self.name}')
        self.internet.receive(half_key)
        recipient.receive_half_key(half_key)

    def receive_half_key(self, half_key: int):
        print(f'{self.name} received half key {half_key}')
        self.received_half_key = half_key

    def compute_secret_key(self):
        self.secret_key = pow(self.received_half_key, self.secret_number) % P
        print(f'{self.name} secret key is {self.secret_key}')

