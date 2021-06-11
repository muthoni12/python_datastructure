'''

Given a list of three exclusive prices and the TAX rate,
write a function that takes a list of exclusive prices and TAX rate as parameter.
then calculate the VAT amount and inclusive prices of each value in the list.
Return a list of inclusive prices and a list of VAT amount.
The exclPrices = [100, 70, 80]

'''

def calculateVAT(excl, taxRate):
    VAT = []
    incl = []

    breadVAT = excl[0] * taxRate
    VAT.append(breadVAT)
    incl.append(excl[0] + breadVAT)

    VAT.append(excl[1] * taxRate)
    incl.append((excl[1] * taxRate) + excl[1])

    VAT.append(excl[2] * taxRate)
    incl.append((excl[2] * taxRate) + excl[2])

    return [incl, VAT]

print(calculateVAT([100, 200, 50], 0.16))

'''
The shorter method - using a FOR LOOP
'''

def calculateVAT(excl, rate):
    vatAmount = []
    incl = []
    for price in excl:
        vat = price * rate
        vatAmount.append(vat)
        incl.append(price + vat)

    return [incl, vatAmount]

print(calculateVAT([100, 200, 50], 0.16))


'''

Write a function that takes a list of YOB and the CY as parameters,
then calculate and return a list containing the ages of each YOB provided in the parameters

'''

def calculateAge(CY, YOB):
    Age = []

    girlAge = CY - YOB[0]
    Age.append(girlAge)

    Age.append(CY - YOB[1])
    
    Age.append(CY - YOB[2])

    return [Age]

print(calculateAge(2021, [1994, 2000, 2002]))

'''
using for loop
'''

def calculateAge(CY, YOB):
    Age = []
    for year in YOB:
        age = CY - year
        Age.append(age)

    return [Age]

print(calculateAge(2021, [1994, 2000, 2002]))

