#计算公司净收入
rev=float(input('Enter revenue:'))
exp=float(input('Enter expense:'))
val=rev-exp
print("Net income: ${0:,.2f}".format(val))