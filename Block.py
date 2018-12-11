from HashGenerator import HashGenerator
from datetime import datetime


class Block:
    def __init__(self, index, created, transaction, previousHash=""):
        self.index = index
        self.created = created
        self.transaction = transaction
        self.previousHash = previousHash
        self.temp = 0
        self.currentHash = self.createHash()

    def createHash(self):
        return HashGenerator(str(self.index) + self.created + self.transaction.getSender() + self.transaction.getReceiver() + self.previousHash + str(self.temp))

    def mineBlock(self, difficulty):
        while (self.currentHash[0:difficulty] != "0"*difficulty):
            self.temp += 1
            self.currentHash = self.createHash()
