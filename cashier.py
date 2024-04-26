from functions import makeBill

'''__________main__________'''

buyingData = {}
enterDetails = True
while enterDetails:
    details = input('Press A to add product and Q to quit: ')
    if details == 'A':
        product = input('Enter product: ')
        Quantity = int(input('Enter quantity: '))
        buyingData.update({product: Quantity})
    elif details == 'Q':
        enterDetails = False
    else:
        print('Please select a correct option')

membership = input('Enter customer membership: ')
makeBill(buyingData, membership)