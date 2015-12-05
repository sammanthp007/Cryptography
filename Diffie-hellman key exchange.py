# implementing the deffie-hellman key exchange

class DiffieHellman(object):
    def __init__(self, prime_modulus, generator):
        self.private_key = 0
        self.modulus = prime_modulus                        # is the prime modulus
        self.generator = generator                          # is the primitive root [modulo self.modulus]
        # self.generator ** self.private_key mod self.modulus = send_encrypted_key

    def set_private_key(self, input_int):
        self.private_key = input_int

    def send_key(self):
        return ((self.generator) ** self.private_key) % self.modulus

    def get_shared_key(self, encrypted_key):
        return (encrypted_key ** self.private_key) % self.modulus

# PROCESS A KEY IS SHARED BETWEEN ALICE AND BOB

# let alice be one entity of the equation
alice = DiffieHellman(17, 3)
# alice sets her private key
alice.set_private_key(23)
# alice sends her encrypted info to share
alice_sent = alice.send_key()

# suppose bob is the other entity who is in the equation
bob = DiffieHellman(17, 3)
# bob sets his private key
bob.set_private_key(55)
# bob sends his info to share
bob_sent = bob.send_key()

# bob takes the encrypted from alice
b1 = bob.get_shared_key(alice_sent)

# alice receives bobs information
a1 = alice.get_shared_key(bob_sent)
# alice has this as common key
print('alice has - ', a1)
# bob has this as common key
print ('bob has - ', b1)

# authentication tactic
print ('If both match, then the program will authenticate. \nAnd because Trudy, an evesdropper, will not have anyones private key, Trudy won\'t be able to get hold of the shared key')
