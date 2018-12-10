from HashGenerator import HashGenerator
from BlockChain import BlockChain

def printBlock(newBlock):
    print("index: ", newBlock.index)
    print("created: ", newBlock.created)
    print("transaction Sender: ", newBlock.transaction.getSender())
    print("transaction Receiver : ", newBlock.transaction.getReceiver())
    print("transaction Amount : ", newBlock.transaction.getAmount())
    print("currentHash: ", newBlock.currentHash)
    print("previousHash: ", newBlock.previousHash, "\n")

bc = BlockChain()
printBlock(bc.getCurrentBlock())
bc.addNewBlock("Ben", "Gwyen", 225)
printBlock(bc.getCurrentBlock())
bc.addNewBlock("Hello", "Delhi", 1050)
printBlock(bc.getCurrentBlock())

print(bc.verifyIntegity())