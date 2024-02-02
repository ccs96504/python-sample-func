def document_init(func):
    def new_function(*args, **kwargs):
        print('func_name:', func.__name__)
        print('args:',args)
        print('kwarfs',kwargs)
        result = func(*args,**kwargs)
        return result
    return new_function

def add_init(a,b):
    return a+b



'''
    test = document_init(add_init)
    test(3,6)

    ---
    func_name: add_init
    args: (3, 6)       
    kwarfs {}
'''


@document_init
def add_init_fun2(a,b):
    return a+b


'''

    add_init(3,6)
    ---
    func_name: add_init
    args: (3, 6)       
    kwarfs {}
'''