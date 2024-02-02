class duck:
    def __init__(self,input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter',self.hidden_name)
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter',input_name)
        self.hidden_name = input_name
    name = property(get_name,set_name)

don =duck('test')
don.name = 'doll'