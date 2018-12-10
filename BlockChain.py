from Block import Block
from datetime import datetime
from Transaction import Transaction

class BlockChain:
    def __init__(self):
        self.chain = []
        self.chain.append(self.createGenesisBlock())

    def createGenesisBlock(self):
        currTime = str(datetime.now())
        genesisBlock = Transaction("TempSender", "TempReceiver", 100, currTime)
        return Block(0, currTime, genesisBlock)

    def getCurrentBlock(self):
        currentBlock = self.chain[-1]
        return currentBlock

    def addNewBlock(self, sender, receiver, amount):
        currentBlock = self.getCurrentBlock();
        currTime = str(datetime.now())
        newTransaction = Transaction(sender, receiver, amount, currTime)
        newBlock = Block(currentBlock.index+1, currTime, newTransaction, currentBlock.currentHash)
        self.chain.append(newBlock)
