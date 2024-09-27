#chapter 4

#Looping Through an Entire List
fav_pizza=["mushroom","jalepino","latte"]
for pizza in fav_pizza:
    print(pizza)


fav_pizza=["mushroom","jalepino","latte"]
for pizza in fav_pizza :
    print(f"{pizza}, you ARE selected TO perform in my stomach")
    print(len(pizza))

time_frame=["1 min","2 min","3 min","four miniuts"]
for trade in time_frame :
    print (f"{trade.lower()} is the best time frame to trade in market")
print("nice you just learned market using someones experince")


#excercise 4.1
mangoes= ["haphus","nolbeira","kamruipia"]
for mango in mangoes :
    print(f"i love to eat {mango} in summer")
    print("thats the reason I love summer\n")

print( "nice")

#using the range function
# Using range() to print numbers from 0 to 4
for i in range(5):
    print(i)

#to make a list of numbers with range()
bats= list (range(3,9))
print(bats)

#to skip counting and set the step size to skip
even_number=[]
even_number= list(range(2,25,2))
print(even_number)
# with some defined number 

a=5
z=99
wonder=list(range(a,z,17))
print(wonder)


# Create an empty list to store squared values
squares = []  
for value in range(1, 11):
    # Calculate the square of the current value
    square = value ** 2  
     # Append the square to the 'squares' list
    squares.append(square) 
   
    # Print the list containing the squared values
print(squares)  



#example

adding_up=[]
for math in range (3,9) : 
    added= math*1.67
    adding_up.append(added)

print(adding_up)

#to write it clean
adding_up=[]
for math in range (4,12) :
    adding_up.append(math**3)
print(adding_up)


# min , max , sum 
numbers=[8,3,4,5,6,7,3,3,7,8,1,3,2,4,1,8,9,]
onko = min(numbers)
print(onko)

# more concise way 
adding_up=[math**1.2 for math in range (7,31)]
print (adding_up)


#4.3
for onko in range (1,100000,100) :
    
    print(onko)

#4.4

# number_s=list(range(1,1000000))
# for gonit in number_s :
#     print(gonit)

#max,min,sum

numbs=list(range(1,1000001))
print(min(numbs))
print(max(numbs))
print(sum(numbs))         
    

#4.6 odd number
for numy in range(1,21,2) :
    print(numy)

#4.7
numo=[nomu*3 for nomu in range(3,31)]
print(numo)

#4.8
numo=[nomu**3 for nomu in range(1,11)]
print(numo)

#slicing
retweet=["tu","me","io","op"]
print(retweet[-4:])

#coppying /slicing
retweet=['tu','me','io','op']
someones_tweet=retweet[:]
retweet.append('postos')
someones_tweet.append('post')

print(someones_tweet)
print(retweet)
print(f"{someones_tweet}is mirroring{retweet}")

#4.10

yu=['er','we','tr','ij','ol','lol','ok']
print(yu[3:7])

my_pizza=['kol','aam','gur']
her_pizza=my_pizza[:]
her_pizza.append('kahi')
my_pizza.append('tita')
 
print("my favv pizza are : ")
for my in my_pizza:
    print(my)

print("her fav pizzas are : ")
for my in her_pizza : 
    print(my)
