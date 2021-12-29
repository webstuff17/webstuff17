#p_python_OOP.py

print('p_python_OOP.py')

'''
class Person :
    'We can use this to document what the class is all about - A PERSON'
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'Hello my name is {self.name} and I\'m {self.age} years old.' )

person_object = Person('Jane','22')
person_object.introduce()
print(person_object.age)

#You can also use the following four functions. Try them out in your code editor:

hasattr(person_object, 'age') # Returns True if 'age' exists
getattr(person_object, 'age') # Returns value of 'age' attribute
setattr(person_object,'age',19) # Sets attribute 'age' to 19, for example
print(person_object.age)
delattr (person_object, 'age') # Deletes the attribute 'age'
setattr(person_object,'age',100)
print(person_object.age)


print(Person.__doc__)
'''
#Now that you know the basics of writing classes and creating instances from them,
#let’s try to apply what you have learned to a little scenario:
#You are writing a medical app that assesses people’s daily nutritional intake.
#As part of your app, you need to create a class: Patient. This class has these attributes:
#Sugar intake (measured in grams)
#Fat intake (measured in grams)
#Salt intake (measured in milligrams)
#The class also needs a function to check if the patient is healthy.
#The app uses these nutritional guidelines to define a healthy daily intake:
#Sugar: no more than 37.5 g per day
#Fat: no more than 77 g per day
#Salt: no more than 2300 mg per day

################################ CLASS ###########################################
class Patient:
    ''' This class is to assess a patients diet and assess if it is healthy
         *Sugar intake (measured in grams)
         *Fat intake (measured in grams)
         *Salt intake (measured in milligrams)'''
    threshold_sugar = 37.5   #set class attribute values
    threshold_fat = 77
    threshold_salt = 2300
    def __init__ (self, name, sugar, fat, salt):
        self.name = name
        self.sugar = sugar
        self.fat = fat
        self.salt = salt

    def check_diet(self):
        self.check_sugar()
        self.check_fat()
        self.check_salt()

    def check_sugar(self):
        if self.sugar > Patient.threshold_sugar:
            print('Sugar intake exceeds 37.5g per day')
            return True
        else: return False

    def check_fat(self):
        if self.fat > Patient.threshold_fat:
            print('Fat intake exceeds 77g per day')
            return True
        else: return False

    def check_salt(self):
        if self.salt > Patient.threshold_salt:
            print('Salt intake exceeds 2300mg per day')
            return True
        else: return False

############################### TEST CLASS #########################################

#ptest = Patient('Jane',100,88,3000)
#print(ptest.name, ptest.sugar, ptest.fat, ptest.salt, '\n')
#ptest.check_diet()
#print('\n',Patient.__doc__)

################################## FUNCTIONS #######################################

def input_number(which_num):
    check_val=False
    try:
        num_ip = float(input(f'Enter {which_num} number: ')) #check input can be converted to a number
        #return num_ip, True
    except:
        print('Please enter a number')
        num_ip = None
        check_val = True
    return num_ip, check_val


##################################### MAIN #########################################
print('\n',Patient.__doc__, '\n')
p=[]
x=int(input('Enter number of patients to assess: '))
for i in range(x):
    #print('p'+str(i))
    #p[i]='p'+str(i)
    p.append('p_'+str(i+1))
    print(i, p[i])

    p_name = input('Please enter patients name: ')
    #enter sugar intake
    check_value=True
    while check_value:
        sugar_num, check_value = input_number('Sugar intake daily in g')
        #print('debugA', first_num, check_value)
    #enter fat intake
    check_value=True
    while check_value:
        fat_num, check_value = input_number('Fat intake daily in g')
    #enter fat intake
    check_value=True
    while check_value:
        salt_num, check_value = input_number('Salt intake daily in mg')

    p[i]= Patient(p_name,sugar_num, fat_num, salt_num)
    print(p[i].name, p[i].sugar, p[i].fat, p[i].salt, '\n')
    p[i].check_diet()

#####################################################################################
