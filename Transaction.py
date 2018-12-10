class Transaction:
    def __init__(self, sender, receiver, amount, txnDateTime):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.txnDateTime = txnDateTime

    def getSender(self):
        return self.sender

    def getReceiver(self):
        return self.receiver

    def getAmount(self):
        return self.amount

    def getTransactionDateTime(self):
        return self.txnDateTime