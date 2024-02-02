from decorator.sample1 import document_init,add_init,add_init_fun2
from namespace.sample1 import print_animal,print_animal_


if "__main__" == __name__:

    test = document_init(add_init)
    test(3,7)
    add_init_fun2(3,6)

    print_animal()
    print_animal_()