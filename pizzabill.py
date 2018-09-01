#Developer: Javid Aslam J
#Co Developer and Tester: Ramesh S
#support and Tester: Mohamed Sajed S  
print("\t\t##### WELCOME TO PIZZA HUT######")
def bill():
  print("-->what do you want?")
  order=int(raw_input("-->1.pizza\n-->2.soft drinks"))
  if(order==1):
    print("-->which type of pizza you wish")
    type=int(raw_input("--> 1. veg \n-->2. nonveg"))
    qty=int(raw_input("-->enter the number of pizzas you want"))
    if(type==1):
      print("-->available varaities")
      varaities=int(raw_input("-->1.cheese pizza \n-->2.mushroom pizza"))
      if(varaities==1):
        print("-->available sizes")
        size=int(raw_input("-->1.small \n-->2.medium \n-->3.large"))
        if(size==1):
          amount=99*qty
          print("-->the bill amount for your small cheese pizza is:",amount)
        elif(size==2):
          amount=199*qty
          print("-->the bill amount for your medium size cheeze pizza is:",amount)
        elif(size==3):
          amount=250*qty
          print("-->the bill amount for your large size cheeze pizza is :",amount)
        else:
          print("-->INVALID OPTION...")
      elif(varaities==2):
        print("-->available sizes")
        size2=int(raw_input("-->1.for small \n-->2.medium \n -->3.lagre"))
        if(size2==1):
          amount=85*qty
          print("-->the bill amount for the small size mushroom pizza is:",amount)
        elif(size2==2):
          amount=180*qty
          print("-->the bill amount for the medium size mushroom pizza is:",amount)
        elif(size2==3):
          amount=235*qty
          print("-->the bill amount for the large size mushroom pizza is:",amount) 
        else:
          print("-->SORRY..!INVALID OPTION...")
      else:
        print("-->SORRY..!INVALID OPTION...")  
    elif(type==2):
      print("-->available varaities ")
      choice=int(raw_input("-->1.cheezy chicken \n-->2.premium chicken delight"))
      if(choice==1):
        size3=int(raw_input("-->1.for small \n-->2.medium \n -->3.lagre"))
        if(size3==1):
          amount=300*qty
          print("-->the bill amount for the small cheezy chicken pizza is:",amount)
        elif(size3==2):
          amount=350*qty
          print("-->the bill amount for the medium cheezy chicken pizza is:",amount)
        elif(size3==3):
          amount=400*qty
          print("-->the bill amount the large cheezy chicken pizza is:",amount)
        else:
          print("Invalid Option")
      elif(choice==2):
        size4=int(raw_input("-->1. small \n-->2.medium \n -->3.lagre"))
        if(size4==1):
          amount=450*qty
          print("-->the bill amount the small premium chicken delight pizza is:",amount)
        elif(size4==2):
          amount=500*qty
          print("-->the bill amount for the medium premium chicken delight pizza is:",amount)
        elif(size4==3):
          amount=550*qty
          print("-->the bill amount for the large premium chicken delight pizza is:",amount)
        else:
          print("INVALID OPTION.....")
      else:
        print("SORRY..!INVALID OPTION")
    else:
      print("-->SORRY..!INVALID OPTION...")      
  elif(order==2):
    print("-->available soft drinks")
    choice2=int(raw_input("-->1.coke \n-->2.pepsi"))
    qty2=int(raw_input("enter the quantity of drink you want in ml:"))
    if(choice2==1):
      amount=0.2*qty2
      print("-->the bill amount for your coke is:",amount)
    else:
      amount=0.2* qty2
      print("-->the bill amount for your pepsi is:",amount)
  else:
    print("-->SORRY...!INVALID OPTION...")    
z="y"
while(z=="y"):
  bill()
  print("do you want to continue:yes/no")
  z=str(raw_input("Enter the choice:(y/n)"))
print("\t*****thank you for your visit *****") 
print("\t    *****come back soon(-_-)*****")
