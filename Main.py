from HashGenerator import HashGenerator
from BlockChain import BlockChain
from Transaction import Transaction

bc = BlockChain()
bc.addTransaction(Transaction("Mohit", "Rohit", 100))
bc.addTransaction(Transaction("Rohit", "Vishal", 150))
bc.getAllTransaction()
bc.minePendingTransactions("Mohit")
print(bc.getBalanceMiner("Mohit"))
bc.minePendingTransactions("Mohit")
print(bc.getBalanceMiner("Mohit"))
