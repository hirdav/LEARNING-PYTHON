

# {=====dictionaries=======} 

odi={'run' : '80' , 'wicket' : '3'}
print(odi['run'])

#------------------------------------------------------------#
alien_0 = {'x_position': 0,'y_position': 25,'speed':'medium'}
print(f"Original position : {alien_0['x_position']}")


if alien_0['speed'] == 'slow' : 
    x_increment=1
elif alien_0['speed'] == 'medium' :
    x_increment=2
else :
    x_increment=3

alien_0['x_position']=alien_0['x_position'] + x_increment
print(f"new position : {alien_0['x_position']}")
#---------------------------------------------------------------#
mposition={'mvolume': 13001, 'participants': 68 ,'momentum': 30}
print(f'now the volume of the market  : {mposition["mvolume"]}')
if mposition['mvolume']== 12000 :
    sell_qty=100
elif mposition['mvolume'] >= 13000 :
    sell_qty= 200
else :
    hold=68
mposition['mvolume'] = mposition['mvolume']+sell_qty
print(f"market says to sell : {mposition['mvolume']} qty")
print("---------------------------------------------------------------")

ticker = { 'symbol': 'apple',
          'price': '211',
          'volume': '34212222',
          'momentum' : '20',
          'product' :['phone','watch','desktop']
    
}

ticker['volume'] = 300000
# for i , j in ticker :
if ticker['volume'] ==3000000:
        print(f"sell{ticker['symbol']} for {ticker['momentum']}")
else:
        print (f"{ticker['symbol']} has good product like {ticker['product']}")
print("good trade")

print("---------------------------------------------------------------")
