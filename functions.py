
def getPrice(product, Quantity):
    priceData = {
        'Biscuit': 3,
        'Chicken': 5,
        'Egg': 1,
        'Fish': 3,
        'Coke': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 3
    }
    subTotal = priceData[product]* Quantity
    print(product + ':$' + str(priceData[product]) + ' x ' + str(Quantity) + ' = ' + str(subTotal))
    return subTotal

def getDiscount(billAmount, membership):
    discount = 0
    if billAmount >= 25:
        if membership == 'Gold':
            billAmount = billAmount * 0.80
            discount = 20
        elif membership == 'Silver':
            billAmount = billAmount * 0.90
            discount = 10
        elif membership == 'Bronze':
            billAmount = billAmount * 0.95
            discount = 5
        print(str(discount) + '% off for ' + membership + ' ' + 'membership on total amount: $' + str(billAmount))
    else:
        print('No discount on amount less than $25')
    return billAmount

def makeBill(buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    billAmount = getDiscount(billAmount, membership)
    print('The total amount after discount is $' + str(billAmount))




