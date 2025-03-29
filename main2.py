class Computer(object):
    """docstring for Computer."""
    def __init__(self, max_price):
        super(Computer, self).__init__()
        
        self.__max_price = max_price
        
    def sell(self):
        return self.__max_price
    
    def set_max_price(self, change):
        self.__max_price+=change
        
        return self.__max_price
        
cp = Computer(130000)
print(cp.sell(), cp.set_max_price(-89)) # Output: 130000 129911