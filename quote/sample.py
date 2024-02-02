class quote:
    def __init__(self, person, words) -> None:
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words+ '.'
    
class Questionquote(quote):
    def says(self):
        return self.words + '?'
class Exclamationquote(quote):
    def says(self):
        return self.words + '!'


hunter = quote('Jason','hello world')
print(hunter.who() , 'says', hunter.says())

hunter1 = Questionquote('Jason','hello world')
print(hunter1.who() , 'says', hunter1.says())

hunter2 = Exclamationquote('Jason','hello world')
print(hunter2.who() , 'says', hunter2.says())