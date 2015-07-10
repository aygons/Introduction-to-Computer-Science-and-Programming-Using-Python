monthlyInterestRate = float(annualInterestRate / 12) 
lowestPayment = 0
tmpBal = balance
while balance > 0:
    balance = tmpBal
    lowestPayment = lowestPayment + 10
    for i in range(1,13):
        minMonthlyPay = lowestPayment 
        unpaidBalance = balance - minMonthlyPay
        balance = unpaidBalance *(1 + monthlyInterestRate)
print 'Lowest Payment: %d' %lowestPayment