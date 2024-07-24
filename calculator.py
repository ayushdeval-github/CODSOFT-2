
while True:
  print("enter the number")
  a=input()
  b=input()
  def add(a,b):
    return int(a) + int(b)
  def sub(a,b):
    return int(a) - int(b)
  def mul(a,b):
    return int(a) * int(b)
  def div(a,b):
    if b==0:
      return "cannot be divide"
    else:
      return int(a) / int(b)
  print("choose the operation")
  print("1.add")
  print("2.sub")
  print("3.mul")
  print("4.div")
  choose= input("enter the choose (1/2/3/4):")
  if choose =="1":
    print(a,"+",b,"=",add(a,b))  
  elif choose =="2":
    print(a,"-",b,"=", sub(a,b))
  elif choose =="3":
    print(a,"*",b,"=",mul(a,b))
  elif choose =="4":
    print(a,"/",b,"=",div(a,b))
  else:
    print("invalid")
  another_calculation=input("do you want to perform another calculation? (yes/no):") 
  if another_calculation== "no":
    break
  
  
  