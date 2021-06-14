# class car():
#     pass
# honda = car() # object
# tata = car()

# honda.modelname = "city"
# honda.yearm = 2021
# honda.price = 10000

# tata.modelname = "bolt"
# tata.yearm = 2021
# tata.price = 600000

# print(honda.yearm)

# class car():
#     def __init__(self, model_name, year_m, price):
#         self.model_name = model_name
#         self.year_m = year_m
#         self.price = price
    

#     def great(self):
#         print("Modelname is " +self.model_name+ ", Year made is " +str(self.year_m) + ", Price is " + str(self.price))

# c1 = car("city", 2021, 100000)
# c2 = car("bolt", 2021, 600000)

# c1.great()
# c2.great()

# class Teacher():
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
    

#     def helloWould(self):
#         print("Her first name is " +self.first_name+ " " +self.last_name+ ", age is " +str(self.age)+ " years old.")


# class Student(Teacher):
#     def __init__(self, first_name, last_name, age, profession):
#         Teacher. __init__(self, first_name, last_name, age)
#         self.profession = profession


#     def detail(self):
#         print("Her first name is " +self.first_name+ " " +self.last_name+ ", age is " +str(self.age)+ " years old and profession is " +self.profession)



# # t1 = Teacher("Hima", "Ritchil", 30)
# # t2 = Teacher("Smith", "Tripura", 28)

# s1 = Student("Rina", "Gomes", 21, "Graphics Designer")

# s1.detail()

# class Person():
#     def __init__(self, name, age, profession):
#         self.name = name
#         self.age = age
#         self.profession = profession




#     def demo(self):
#         print("My name is " +self.name+ ", I am " +str(self.age)+ " years old, profession is " +self.profession)

# class child(Person):
#     def __init__(self, name, age, profession, salary,):
#         Person. __init__(self,name, age, profession)
#         self.salary = salary



#     def great(self):
#         print("My name is " +self.name+ ", I am " +str(self.age)+ " years old, profession is " +self.profession+ ", and I make " +str(self.salary)) 
    


        

# c1 = child("Balwin", 32, "software_engineer", 5000)
# c2 = child("Rina", 12, "web_developer", 10000)

# c1.great()
# c2.great()

# class Balwin():
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

    
#     def hili(self):
#         print("My name is " +self.first_name+ " " +self.last_name+ ", and I am " +str(self.age)+ " years old.")

# class Blancho(Balwin):
#     def __init__(self, first_name, last_name, age, salary):
#         Balwin. __init__(self, first_name, last_name, age)
#         self.salary = salary


#     def Mrinali(self):
#         print("His name is " + self.first_name+ " " +self.last_name+ ", He is " +str(self.age)+ " years old and He makes " +str(self.salary))


# p1 = Blancho("Angkur", "Nokrek", 12, 20000)

# p1.Mrinali()
# age = input('Input your age : ')
# if int(age) == 16:
#     print('Hey youre 16')

# age = input('Input your age : ')

# if int(age) > 16:
#     print('Hey youre 16 ')

heihgt = input()
if str(height) <= 1:
    print('you cannot ride, under 1m')
elif str(height) >= 2:
    print('you cannot ride, over 2m')
else:
    print('you can ride')


