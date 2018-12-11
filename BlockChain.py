from Block import Block
from datetime import datetime
from Transaction import Transaction


class BlockChain:
    difficulty = 2

    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.miningReward = 100
        self.chain.append(self.createGenesisBlock())

    def createGenesisBlock(self):
        currTime = str(datetime.now())
        genesisTransaction = []
        genesisBlock = Block(currTime, genesisTransaction)
        genesisBlock.mineBlock(BlockChain.difficulty)
        return genesisBlock

    def getCurrentBlock(self):
        currentBlock = self.chain[-1]
        return currentBlock

    # def addNewBlock(self, sender, receiver, amount):
    #     currentBlock = self.getCurrentBlock()
    #     currTime = str(datetime.now())
    #     newTransaction = Transaction(sender, receiver, amount, currTime)
    #     newBlock = Block(currTime, newTransaction, currentBlock.currentHash)
    #     newBlock.mineBlock(BlockChain.difficulty)
    #     self.chain.append(newBlock)

    def minePendingTransactions(self, minerRewardAddress):
        currTime = str(datetime.now())
        newBlock = Block(currTime, self.pendingTransactions)
        newBlock.mineBlock(BlockChain.difficulty)
        self.chain.append(newBlock)
        self.pendingTransactions = [Transaction(None, minerRewardAddress, self.miningReward)]

    def addTransaction(self, newTransaction):
        self.pendingTransactions.append(newTransaction)
    

    def getBalanceMiner(self, minerAddress):
        balance = 0;
        for block in self.chain:
            for trans in block.transactions:
                if trans.getSenderAddress() == minerAddress:
                    balance -= trans.amount
                if trans.getReceiverAddress() == minerAddress:
                    balance += trans.amount
        return balance
    
    def getAllTransaction(self):
        for trans in self.pendingTransactions:
            print(trans.getSenderAddress())
            print(trans.getReceiverAddress())
            print(trans.getAmount(), "\n")            

    
    def verifyIntegity(self):
        for i in range(1, len(self.chain)):
            prevBlock = self.chain[i-1]
            currBlock = self.chain[i]

            if currBlock.currentHash != currBlock.createHash():
                return False

            if currBlock.previousHash != prevBlock.currentHash:
                return False
        return True

    def displayBlockChain(self):
        for i in range(len(self.chain)):
            print("created: ", self.chain[i].created)
            for t in self.chain[i].transactions:
                print("---Transaction---")
                print("Sender: ", t.getSender())
                print("Receiver: ", t.getReceiver())
                print("Amount: ", t.getAmount())
            print("previousHash: ", self.chain[i].previousHash)
            print("currentHash: ", self.chain[i].currentHash, "\n")
