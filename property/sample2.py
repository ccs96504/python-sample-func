class duck:
    def __init__(self,input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter',self.hidden_name)
        return self.hidden_name
    @name.setter
    def name(self,input_name):
        print('inside the setter',input_name)
        self.hidden_name = input_name

