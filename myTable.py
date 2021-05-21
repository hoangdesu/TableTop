# Test run code

from TableTop import *

myTable = TableTop(["ID", "Name", "Class"])
myTable.add_row([1, 'Hoang', 10])
myTable.add_row([2, 'Brian Nguyen', 7])
myTable.add_row([3, 'Nguyen Quoc Hoang', 69])
myTable.add_row([4, 'Brian Hoang Quoc Nguyen aka "hoangdesu"', 900000])
myTable.add_row([5, 'Tèo', 1])
myTable.add_row([6, 'Hoang Nguyen', 3])
myTable.add_row([7, 'Doroke', 2])
myTable.add_row([8, 'TableTop', 4])
myTable.add_row([9, 'Python', 12])
myTable.add_row([10, 'JavaScript', 5])

print(myTable)
        