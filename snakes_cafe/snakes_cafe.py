cafeMenu=['wings', 'cookies', 'spring rolls', 'salmon', 'steak', 'meat tornado', 'a literal garden', 'ice Cream', 'cake', 'pie', 'coffee', 'tea', 'unicorn tears']
print(
    """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
    """
)
orderArray=[]
orderNames=[]
def orderingOperator():
    
    order=input('>')
    if order.lower() in cafeMenu:
        orderArray.append(order)
        if order not in orderNames:
            orderNames.append(order)
        print(f'** {orderArray.count(order)} order of {order} have been added to your meal **')
        orderingOperator()
    elif order.lower()=='quit':
        print('**Your order**')
        for x in orderNames:
            print(f'{orderArray.count(x)} order of {x} ')
        print('**Thank you for visiting our Cafe**')
        print('**We are working on your order**')
    elif order.lower() not in cafeMenu:
        print('**Your order is not in our menu**')
        orderingOperator()

orderingOperator()