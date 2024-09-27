#List

cricket = ['sachin','dravid','yuvi','agarkar','munaf','balaji']
print(cricket[4])
print(cricket[-1])

# using f stirng
cricket = ['sachin','dravid','yuvi','agarkar','munaf','balaji']
age = [7,8,10,11,12,14,15]
sondesh= f"my first admiration towards {cricket[1].title()} at the  {age[4]}"
print(sondesh)

#changing value in a list

cricket=['ODI','test','t20']
print(cricket)
cricket[0]='test'
cricket[2]='test'
print(cricket)

#changing the value
family=['maa','deta','bro']
print(family)
family[2]='bhai'
print(family)

#adding in the list 
family.append('bade bhai')
print(family)
#calling out
print(family[-1])

#adding string to the blank list
fam=[]
fam.append('hirak')
fam.append('pk')
fam.append('dk')
fam.append('hk')
print(fam)

#to insert a new element
fam=['i','o','9']
fam.insert(2,'57')
print(fam)
#to delete an element form list
del fam[1]
print(fam)
#to remove a unknow indexed element of a list
fam.remove('9')
print(fam)


#assingment
#3.4 , making a guest list 
invite_party= ['devi','raj','yuji','lee']
day= "monday"
print(f"Hey {invite_party[0].title()},I am hosting a party inviting you to  come this {day} .")
print(f"Hey {invite_party[1].title()},I am hosting a party inviting you to come this {day} .")
print(f"Hey {invite_party[2].title()},I am hosting a party inviting you to come this {day} .")
print(f"Hey {invite_party[3].title()},I am hosting a party inviting you to come this {day} .")
print(f"{invite_party[0].title()} could not make it,so Invited a new guest.")
invite_party[0]="ELon"

#3.5
print(f"Hey {invite_party[0].title()},I am hosting a party inviting you to  come this {day} .")
print(f"Hey {invite_party[1].title()},I am hosting a party inviting you to come this {day} .")
print(f"Hey {invite_party[2].title()},I am hosting a party inviting you to come this {day} .")
print(f"Hey {invite_party[3].title()},I am hosting a party inviting you to come this {day} .")

#new_party= f"So this is my new arrangement {second}"
#print()
#print(f"so the invited guest will be {invite_party}")

#add new guest
invite_party.insert(0,'joe')
invite_party.insert(2,'black')
invite_party.append('marrie')

print(f"so here is your new guest to {invite_party}")
print(f"Hey {invite_party[0].title()},I am hosting a party inviting you to  come this {day} .")
print(f"Hey {invite_party[1].title()},I am hosting a party inviting you to come this {day} .")
print(f"Hey {invite_party[2].title()},I am hosting a party inviting you to come this {day} .")
print(f"Hey {invite_party[3].title()},I am hosting a party inviting you to come this {day} .")
print(f"Hey {invite_party[4].title()},I am hosting a party inviting you to come this {day} .")
print(f"Hey {invite_party[5].title()},I am hosting a party inviting you to come this {day} .")
print(f"Hey {invite_party[6].title()},I am hosting a party inviting you to come this {day} .")

# 3.5  shrinking guest list
party_next_time= invite_party.pop()
print(f"Hi {party_next_time},sorry I have to attend you next time.")
party_next_time= invite_party.pop()
print(f"Hi {party_next_time},sorry I have to attend you next time.")
party_next_time= invite_party.pop()
print(f"Hi {party_next_time},sorry I have to attend you next time.")
party_next_time= invite_party.pop()
print(f"Hi {party_next_time},sorry I have to attend you next time.")

print(f"Hey {invite_party[0]}, we are gonna have a blast")
print(f"Hey {invite_party[1]}, we are gonna have a blast")

#3.6
del invite_party[0]
del invite_party[1]
print (invite_party)


#Sorting a list
aesthetic= ['long','short','height']
aesthetic.sort()
print(aesthetic)

#list in reverse
aesthetic= ['long','short','height']
aesthetic.sort(reverse=True)
print(aesthetic)


stock_list=['apple','ril','tamo']
print(stock_list.index('tamo'))



from collections import deque 


queue = deque(['apple','mango', 'banana'])

queue.append('cashew')
queue.append('almond')
queue.popleft()
queue.popleft()


queue.extend('7')
queue.rotate(-4)
queue.extendleft('6')
queue.reverse()
print(queue)


message = input("Tell me something, and I will repeat it back to you: ")
print(message)


