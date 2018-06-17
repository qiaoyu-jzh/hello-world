#计算薪酬变动
beginsal=float(input("ur beginning salary:"))
upsal=beginsal*1.1
nextsal=upsal*0.9
change=(nextsal-beginsal)/beginsal*100
print("Nes salary:${0:,.2f}".format(nextsal))
print("Change:{0:.2f}%".format(change))