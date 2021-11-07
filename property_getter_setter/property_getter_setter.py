class test:

    def __init__(self):

        self.optimizer = None

    @property
    def optimizer(self):
        return self.__optimizer

    @optimizer.setter
    def optimizer(self,val):
        self.__optimizer = val
        
    
