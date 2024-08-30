cars=['swift','ducati','tiago','honda']
 
for car in cars :
   
    if car=='honda':
       print(car.upper())
    else :
       print(car.title())
    if car!='polo':
       print("all the cars are not so good")
    
car=39
if car==3:
   print(car)
else :
   print("thats wrong")


car=39
if car > 3:
   print(car)
else :
   print("thats wrong")

car=39
if car < 3:
   print(car)
else :
   print("thats wrong")

car=39
if car != 3:
   print(car)
else :
   print("thats wrong")

car=39
if car <= 3:
   print(car)
else :
   print("thats wrong")

car=39
if car  >= 3:
   print(car)
else :
   print("thats wrong")

age_2= 78
age_1= 90
if age_2 < 39 :
   print(age_2)
else:
   print("nothing")
if age_1 >= 888:
   print(age_1)
else :
   print("look for something else")
if age_1 >= 88 and age_2 >= 56:
   print(age_2)
else :
   print("look for something else")

#checking whether a value is in a list
mine = ['hirak','kalita','jyoti']
print('jyoti' in mine)
mr= 'boro'
if mr not in mine :
   print(f"please change your name to {mr} ")
else:
   print(mine)

print("is mr=='boro', its allright")
print(mr=='boro')


arjun = 'dream'
print(arjun=='dream')
if arjun!='dream':
   print("poor")
arjun = 'dream big'
print(arjun!='dream big')
if arjun=='dream big':
   print("rich")


god='great'
if god == 'great' :
   print("he will always bless us")
else : 
   print ("he must be resting")

#if-elif-else

speed = 20
if speed < 79 :
   print("You are a simple driver")
elif speed < 100 :
   print("khatro ke khiladi")
elif speed < 220 :
   print ("mout ke samne")
else :
   print ("you dont drive much")

#to show another set of info within if - elif- else

speed = 85
if speed < 79 :
   fine = 0
   print(f"You are a simple driver , so you incure {fine} fine.")
elif speed < 100 :
   fine = 2000
   print(f"khatro ke khiladi, you incure {fine} fine. ")
elif speed < 220 :
   fine = 40000
   print (f"mout ke samne, you incure {fine} fine. ")
else :
   print ("you dont drive much")

#clean version of this above
#here you dont need print the message every time .if any of the message is true
#but here there is different message for each command but if we need just one 
#every line .just print the only true ones.

speed = 85
if speed < 79 :
   fine = 0
   
elif speed < 100 :
   fine = 2000
   
elif speed < 220 :
   fine = 40000

print(f"so you incure {fine} fine.")

  
#testing else if  - elif
man = 'hi',' ola','gbye'
if 'hi' in man : 
   print("hi buddy")
elif 'gbye' in man :
   print( "hey")
# elif 'jo' in man :
   print(" best")
   #here you can observe that placing elif in a true contion did not excuted becuase the previous
   #statement is already true , so thats why it is usefull if only try ot find ture condiiton

#testing else if  - elif
man = 'hi',' ola','gbye'
if 'hi' in man : 
   print("hi buddy")
if 'gbye' in man :
   print( "hey")
elif 'jo' in man :
   print(" best")


#5.3
alien_color='green','yellow','red'
if 'green' in alien_color:
   print("if you have just earned 5 points")
if 'black' in alien_color:
   print(" no use")

#5.4
alien_color='green','yellow','red'
alien_color='yellow'
if alien_color != 'green':
   print("if you have just earned 10 points")
if alien_color != 'yellow' :
   print ("buddy you are genius  and earner 20 points")
else:
   print("----busted-----")

#5.5
   alien_color='yellow'
   alien_color='red'
   alien_color='green'
if alien_color == 'green':
   print("if you have just earned 10 points")
elif alien_color == 'yellow' :
   print ("buddy you are genius  and earned 4.7 points")
elif alien_color == 'red' :
   print ("buddy you just earned 79 points")   
else:
   print("----busted-----")


#5.6
age= 1.6

if age <2 :
   print("this person is a baby")

elif age <= 4 :
   print("this person is a toddler")

elif age <= 13 :
   print("this person is a kid")

elif age <= 20 :
   print("this person is a teenager")

elif age >= 65 :
   print("this person is a elderly person")

else : 
   print("you are not born yet")

#using for loop with condition
requested_match= ['test','t20','odi']

for game in requested_match:
   if game == 'odi':
      print("today is not the day for odi")
   else :
      print(f"alas {requested_match}  !!!")
print("\ntry to curate the pitch")

requested_toppings = ['mushrooms', 'green peppers',
                     'extra cheese']
for requested_topping in requested_toppings:
 if requested_topping == 'green peppers':
   print("Sorry, we are out of green peppers right now.")
 else:
   print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")


requested_match= ['test','t20','odi']

for game in requested_match:
   if game == 'odi':
       print("today is not the day for odi")
   else :
       print(f"alas {requested_match}  !!!")  # here you can see that the loop printed the whole list like and array  
print("\ntry to curate the pitch")            # because I mistakenly add the list not the temporary variable


requested_match = ['test', 't20', 'odi']

for game in requested_match:
    if game == 'odi':
        print("today is not the day for odi")
    else:
        print(f"alas {game} !!!")

print("\ntry to curate the pitch")



requested_game= []   #its an empty list as the user request is confirmed so it does help in user fornt requests
if requested_game:
   for gome in requested_game : 
      print(f"adding a new game {gome}")
   print ("\nfinished the gome")
else :
   print(" aaj kuch nai khelna")


requested_game= ['deuce ball']   #when the user rquest somehting the loop get started 
if requested_game:
   for gome in requested_game : 
      print(f"adding a new game  with {gome}")
   print ("\nthen finished the gome")
else :
   print("aaj kuch nai khelna")


available_games =['t20','odi','test','ipl']
country_game=['ipl','khokho','kabaddi']

for popular in available_games :
      if popular in country_game : 
         print (f"this is the most clebrated {popular}")
      else : 
         print (f"this games will take time to most celebrated  {popular}")

print("n\this is the real tuth")



available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] #user requested command 
for requested_topping in requested_toppings: #creat a temporary variable to run the loop
   if requested_topping in available_toppings:
      print(f"Adding {requested_topping}.")
else:
   print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")


exchange=['tata elexi', 'tata power', 'trent' , 
          'tata investmennt']
zerodha= ['tata motors', 'ttml','tata consumer']
#the aim of the program is if any of those those cos is not listed in exchange , i ll not buy the co
for zero in zerodha:
   if zero in exchange :
      print (f"place an order for :  {zero}")
   else:
      print (f"order rejected for {zero}")

print("\nSee the order book for trades")
#thats what i wnated

#5-8
user_name = ('designer','devpops', 'admin')
for usn in user_name :
   if  usn == 'admin' :
      print(f"HI {usn}, check for the status ")
   else :
      print(f"hellow {usn}")
#5.9
user_name = []
for usn in user_name :
   if  usn == 'admin' :
      print(f"HI {usn}, check for the status ")
   else :
      print(f"hellow {usn}")

print("\nwe neeed to find more user")

#5-10
curent_users=['test','odi','ipl','t10','sky']
curent_users=['test','odi','ipl','t10','SKY']
new_user= ['sachin','dravid','virat','rohit','ajankya','sky']
for n1 in new_user:
   if n1 in curent_users:
      print(f"{n1}need to enter a new user name")
   else:
      print("user name is available")

#5-11
mathamate=list(range(1,10))
for matts in mathamate :
   if matts ==1 :
      print(f"{matts}st")
   elif matts ==2 :
      print(f"{matts}nd")
   elif matts ==3 :
      print(f"{matts}rd")
   elif matts ==4:
      print(f"{matts}th")
   elif matts ==5:
      print(f"{matts}th")
   elif matts ==6:
      print(f"{matts}th")  
   elif matts ==7:
      print(f"{matts}th")
   elif matts ==8:
      print(f"{matts}th")
   elif matts ==9:
      print(f"{matts}th")      