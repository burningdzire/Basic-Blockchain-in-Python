from datetime import datetime
from HashGenerator import HashGenerator
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


class Transaction:

    def __init__(self, senderAddress, receiverAddress, amount):
        self.senderAdress = senderAddress
        self.receiverAddress = receiverAddress
        self.amount = amount
        self.txnDateTime = str(datetime.now())

    def createHash(self):
        return HashGenerator(self.senderAdress + self.receiverAddress + self.amount + self.txnDateTime)

    def getSenderAddress(self):
        return self.senderAdress

    def getReceiverAddress(self):
        return self.receiverAddress

    def getAmount(self):
        return self.amount

    def getTransactionDateTime(self):
        return self.txnDateTime
