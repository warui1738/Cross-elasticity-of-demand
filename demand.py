#  A program that deals with demand
# getting cross elasticity of demand

def crossElastcityofDemand():
  '''This is a program that gets the cross elasticity of two products requires the  // change in quantity demanded of product x//the original quantity of product x  //change in price of product y//the original price of product y''' 
  # PRODUCT X
  newQuantityFx= int(input("Please enter the new quantity of product x:" ))
  originalQuantityFx = int(input("Please enter the original  quantity of product x:" ))
  changeQuantityFx = newQuantityFx - originalQuantityFx
  
  #PRODUCT Y
  newPRICEFy = int(input("Please enter the new price of product y:" ))
  originalPRICEFy = int(input("Please enter theoriginal price of product y:" ))

  changePriceyFy = newPRICEFy - originalPRICEFy

  CED = changeQuantityFx/originalQuantityFx  * changePriceyFy/originalPRICEFy

  print("The cross elasticity of the two goods are {}".format(CED))
  if CED  >= 0:
    print("The two goods are substitutes")
  elif CED <= 0:
    print("The two goods are complimentary")
  else:
    print("The two goods  are  independent")


# crossElastcityofDemand()
def changeofBaseFormula():
  '''
  This is a program that changes the base formola in q logarithimic situations ===>
  LOG-b[N] =  LOG-a[N]/LOG-a[b] //where  a is the new base
  '''
  import math
  logbase = int(input("Please enter the initial base:"))
  logNumber = int(input("Please enter the number of the log:"))
  print("The log you want to conVert is=\n LOG-{}[{}]".format(logbase,logNumber))
  newbase = int(input("Please enter the new base you want:"))
  
  x = math.log(logNumber,newbase) / math.log(logbase,newbase)
  print(changeofBaseFormula.__doc__)
  print("The converted log is \n LOG-{}[{}]".format(newbase,x))
changeofBaseFormula()