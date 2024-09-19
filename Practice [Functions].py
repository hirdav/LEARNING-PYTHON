r = (4,6,7,3,4)

yu = len(r)//1
print (yu)

def greet (person_name):
    a=1 
    if a==10 :
        print("yo")
    else :
        print ("no")
    print ("hello"+" " +person_name + '!')

greet("john")


def made (a,v) :
    results= a+v 
    print ("this function add values of two values")
    return results
i= "8.9"
p="op"
print(f" {i}  and {p} is {made(i,p)}")


def made(a, v):
    results = str(a) + v  # Convert the number to a string and concatenate
    print("This function concatenates a number and a string.")
    return results

i = 8.9
p = "op"

print(f"{i} and {p} is {made(i, p)}")


def sum_all(*args):
    result=0
    for i in args :
        result += i
    return result
    

print (sum_all(7,2.3,2,2,0,4,21,3.3))

