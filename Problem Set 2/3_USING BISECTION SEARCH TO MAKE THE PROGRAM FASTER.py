monthlyInterestRate = float(annualInterestRate / 12) 
delta = 0.01
tmpBal = balance
upperbond = balance*(1+monthlyInterestRate)**12/12.0
lowerbond = balance/12.0
stop = False
while stop == False:
    balance = tmpBal
    lowestPayment = (upperbond + lowerbond)/2.0
    for i in range(1,13):
        minMonthlyPay = lowestPayment 
        unpaidBalance = balance - minMonthlyPay
        balance = unpaidBalance *(1 + monthlyInterestRate)
    if balance > delta:
        lowerbond = lowestPayment
    elif balance < -delta:
        upperbond = lowestPayment
    else:
        stop = True
print 'Lowest Payment: %.2f' %lowestPayment