#Nailah Pierre
#4/5/24
#M03 Lab - Case Study: Lists, Functions, and Classes

# this programs asks for input from the user and then displays them. this is done using classes

class Vehicle(): #the vehicle class that asks for the type of car
  def __init__(self):
    self.vehicleType = input("What type of vehicle do you have?: ") 
    


        
class Automobile(Vehicle): # the automobile class that asks for the specifics of the vehicle
  def __init__(self):
    super().__init__() #Automoblie will inherit the attributes from the Vehicle class using this piece of code 
    
    self.year = input("What year was your car made?: ") 
    self.make = input("Who is the maker of your car?: ")
    self.model = input("What is the model of your car?: ")
    self.doors = input("How many doors does your car have?: ")
    self.roof = input("What type of roof does your car have?: ")

  def displayVehicle(self):  #this prints out the values that were inputed
    print(
      "Vehicle type: ", self.vehicleType, "\n",
      "Year: ", self.year, "\n",
      "Make: ", self.make, "\n",
      "Model: ", self.model, "\n",
      "Number of doors: ", self.doors, "\n",
      "Type of roof: ", self.roof)



car1 = Automobile() # this runs the Automoblie class and associates it with the variable car1
car1.displayVehicle() # this runs the code that will print out the values that were inputed