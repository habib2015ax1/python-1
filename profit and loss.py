costprice=float(input("enter the cost price of lemonade"))
sellprice=float(input ("enter the sell price of lemonade"))
if sellprice>costprice:
 profit=sellprice - costprice
 print ("you made a profit",profit)
else:
 loss=costprice-sellprice
 print ("you made a loss",loss)