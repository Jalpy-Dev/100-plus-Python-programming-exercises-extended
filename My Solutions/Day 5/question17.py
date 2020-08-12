# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
#
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
#
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
#
# 500

account_total = 0
trans_log = []

print('Please enter logs (D, W): \n')

while True:
    transaction = input('Log: ')
    if transaction:
        trans_log.append(transaction)
    else:
        break

for log in trans_log:
    if 'D' in log:
        account_total += int(log[2:])
    if 'W' in log:
        account_total -= int(log[2:])

print(f'Total: {account_total}')
