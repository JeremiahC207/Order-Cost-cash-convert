Price=input("What is the price of your meal in USD? ")
Tip=input("what percent are you tipping?(use a decimal) ")
Tipmath = float(Tip) + 1
Endprice = float(Tipmath) * int(Price)
print(str(Endprice)+" In USD")
Cashtype=input("What money type are you paying in(its case sensitive)(USD, EURO, YEN, CAD )? ")
Cashtype=str(Cashtype)
if Cashtype==("USD"):
  print(Endprice)
elif Cashtype==("EURO"):
  Endprice = 0.82289 * int(Endprice)
  print(Endprice)
elif Cashtype==("YEN"):
Endprice = 108.72 * int(Endprice)
  print(Endprice)
elif Cashtype==("CAD"):
  Endprice = 1.20975 * int(Endprice)
  print(Endprice)