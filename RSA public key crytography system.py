# implementing the RSA algorithm

# magical equation, Eulers equation : (m ** phi(n)) % n == 1 
# mixes modular exponentiation and phi function
# working:
# our encryption is basically:
# for a message, we encrypt by raising the message to given power in a specific modular arithematic
# and since in a modular arithematic, if the given message is primitve root of the base of modular arithematic, then we cannot simply determing what the number was because it could be anything as numbers rotate around the modular base and there is equal probablity of getting all number
# hence our encryption: encrypted message = message ** e
# and our only way of decryption is if there exists a d such that: encrypted message ** d = message
# or,                                                               message ** e ** d = message ** (e * d) = message
# now, using euler's theorem: 
#       (message ** phi(n)) % n = 1                 this is a proven theorem, you can try if you want to
# or,   ((message) ** (k * phi(n)) % n = 1 ** k = 1
# or,   ((message) * ((message) ** (k * phi(n)))) % n = message * 1 = message
# or,   ((message) ** (k * phi(n)) + 1)) % n = message
# 
# which is congruent to the equation we are looking for i.e. ((message) ** (e * d)) % n = message

#hence:
# d = (k*phi(n) + 1) / e

# in words: in a modular arithematic, a raise to power is reversible only if the phi(modularbase) is known 

class Admin(object):
    def __init__(self):
        self.private_key = 0
        self.public_key1 = 3
        self.prime1 = 2
        self.prime2 = 2
        self.public_key2 = 4
        self.phi_num = 1

    def phi_prime(self, prime_num):
        return ((prime_num - 1))

    def send_public_key(self, prime_num1, prime_num2, e):
        # get two very large prime numbers
        self.prime1 = prime_num1
        self.prime2 = prime_num2
        # multiply two very large prime numbers to get a n
        modulus = self.prime1 * self.prime2
        # get the phi value of n
        self.phi_num = (self.phi_prime(self.prime1) * self.phi_prime(self.prime2)) % modulus
        # calculate the decryption key or the private key
        self.private_key = int((2 * self.phi_num + 1) / e) % modulus
        # set the value of the exponent
        self.public_key1 = e
        self.public_key2 = modulus
        return self.public_key1, self.public_key2

    def get_message(self, encrypted):
        return (encrypted ** self.private_key) % self.public_key2

class User(object):
    def __init__(self, public_key1, public_key2):
        self.message = 0
        self.public_key1 = public_key1
        self.public_key2 = public_key2

    def send_message(self, message):
        return ((message) ** self.public_key1) % self.public_key2

# amazon sends public keys
amazon = Admin()
pub1, pub2 = amazon.send_public_key(53, 59, 3)

# shopper uses the public keys to send encrypted message
shopper = User(pub1, pub2)
encrypted_msg = shopper.send_message(89)

# amazon decrypts the message
message = amazon.get_message(encrypted_msg)
print (message)