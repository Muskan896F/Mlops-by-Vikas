# initiate a class
class employee:
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 1000
        self.designation = "Software Engineer"
        print("Attributes/data have been initialized")

    def travel(self,destination):
        print("This travel method was caled manually")
        print(f"Employee is now travelling to {destination}")

# create an obj/instance of the class
sam = employee()

#print(sam.salary)

#print(sam.id)
#sam.travel("New York")
print(type(sam))