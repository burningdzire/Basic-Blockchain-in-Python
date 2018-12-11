from HashGenerator import HashGenerator
from datetime import datetime
import json


class Block:
    def __init__(self, created, transaction, previousHash=""):
        self.created = created
        self.transactions = transaction
        self.previousHash = previousHash
        self.temp = 0
        self.currentHash = self.createHash()

    def createHash(self):
        transactionsToJsonString = json.dumps(
            [t.__dict__ for t in self.transactions])
        return HashGenerator(self.created + transactionsToJsonString + self.previousHash + str(self.temp))

    def mineBlock(self, difficulty):
        while (self.currentHash[0:difficulty] != "0"*difficulty):
            self.temp += 1
            self.currentHash = self.createHash()
