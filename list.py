def list(*args):
    int_type_list=[i for i in args if type(i) is int]
    print(int_type_list)
list(1,2,3,'a','b','c',4,5,6)