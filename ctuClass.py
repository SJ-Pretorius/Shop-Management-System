class ctuStock:
#Objects for shop names, locations, amount of customers, amount of sales, amount of returns
    def __init__(self,shopName, shopLocation, customers, sales, returns):
        self.shopName=shopName
        self.shopLocation=shopLocation
        self.customers=int(customers)
        self.sales=int(sales)
        self.returns=int(returns)

#Name check function which returns 0 if parameter supplied is blank
    def nameCheck(name):
        if name != '':
            passed = 1
        else:
            passed = 0
        return passed

#Location check which returns 1 if supplied paramater is Free State, Gauteng, KZN or Limpopo
    def locationCheck(loc):
        if loc == 'Free State' or loc == 'Gauteng' or loc == 'KZN' or loc == 'Limpopo':
            passed = 1
        else:
            passed = 0
        return passed