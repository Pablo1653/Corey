class Employee:

    def __init__(self,first,last):
        self.first= first
        self.last= last
        
    @property #property decorator is used to make a method behave like an attribute#The property decorator allows us to define Class methods that we can access like attributes. This allows us to implement getters, setters, and deleters.
    def email(self):
        return '{}.{}@email'.format(self.first,self.last)

    @property #property decorator is used to make a method behave like an attribute  
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    @fullname.setter #setter decorator is used to set the value of a property
    def fullname(self,name):
        first,last = name.split(' ')
        self.first= first
        self.last= last

    @fullname.deleter #deleter decorator is used to delete a property
    def fullname(self):
        print('Deleting fullname...')
        self.first = None
        self.last = None

emp_1 = Employee('John','Smith')

emp_1.fullname = 'Corey Schafer' # This will call the setter method for fullname, which will update the first and last name of emp_1 to 'Corey' and 'Schafer' respectively.

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname # This will call the deleter method for fullname, which will set the first and last name of emp_1 to None.