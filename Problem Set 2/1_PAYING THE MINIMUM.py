monthlyInterestRate = float(annualInterestRate / 12)
paid = 0 
for i in range(1,13):
    minMonthlyPay = balance * monthlyPaymentRate 
    unpaidBalance = balance - minMonthlyPay
    balance = unpaidBalance *(1+monthlyInterestRate)
    paid = paid + minMonthlyPay
    print 'Month: %d' %i
    print 'Minimum monthly payment: %.2f' %minMonthlyPay
    print 'Remaining balance: %.2f' %balance
print 'Total paid: %.2f' %paid
print 'Remaining balance: %.2f' %balance