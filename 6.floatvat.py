taxRate = 1.2
pricePaid = input("How much was your item? ")
print("Your item plus VAT is " + str(round(taxRate * float(pricePaid),2)))