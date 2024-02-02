# can hide self.__name 

class duck:
    def __init__(self,input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter',self.__name)
        return self.__name
    @name.setter
    def name(self,input_name):
        print('inside the getter',input_name)
        self.__name = input_name

        