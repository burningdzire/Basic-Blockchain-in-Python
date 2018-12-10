from HashGenerator import HashGenerator
from BlockChain import BlockChain

bc = BlockChain()
bc.addNewBlock("Ben", "Gwyen", 225)
temp = bc.chain[-1].transaction.getReceiver()
print(len(bc.chain))