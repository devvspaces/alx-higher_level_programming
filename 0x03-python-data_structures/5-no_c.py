#!/usr/bin/python3

def no_c(my_string):
    return "".join([x for x in my_string if x.lower() != 'c'])

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))