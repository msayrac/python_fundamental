# oop with python

#class

liste1 = [1,2,3]
liste2 = [1,2,3]

print(type(liste1))

# class 0> Person (name,surname,birthday,calculateAge())


# instance (object)


# class

class Person:
    #attributes
    pass
    # methods

# object (instance)

p1 = Person()
p2 = Person()

print(p1)
print(p2)

print(type(p1))
print(type(p2))


class Person:
    #attributes

    # class attributes
    adress = "no information"

    # constructor yapıcı metod. Her obje olustugunca calısır. her new lemede calısır
    def __init__(self,name,year):
        # object attributes -> class olustuurulunca inl olması gereken ozellikler
        self.name =name
        self.year = year
        print("init metodu çalıştı. Constructor calıstı")    
    pass
    # instance (self) methods
    def intro(self):
        print(f"Hello there! I am {self.name}")

    def calculateAge(self):
        return 2025-self.year

p1 = Person(name="Ali",year =1980)
p2 = Person(name="Yagmur",year =1990)

# accessing object attributes
print(f"name : {p1.name} year : {p1.year} address : {p1.adress}")
print(f"name : {p2.name} year : {p2.year} address : {p2.adress}")

# updating object attributes
p1.name = "Ahmet"
p1.adress="Kocaeli"
print(f"name : {p1.name} year : {p1.year} address : {p1.adress}")

p1.intro()
p2.intro()

print(f"yaşım : {p1.calculateAge}")
print(f"yaşım : {p2.calculateAge}")


class Circle:
    #class object attribute
    pi = 3.14

# constructor
    def __init__(self,yaricap=1):
        self.yaricap = yaricap

    #methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap

    def alan_hesapla(self):
        return self.pi*(self.yaricap)**2

c1 =Circle() # yaricap=1
c2 = Circle(yaricap=5)

print(f"c1 alan = {c1.alan_hesapla()} c1 çevre = {c1.cevre_hesapla()}")
print(f"c2 alan = {c2.alan_hesapla()} c2 çevre = {c2.cevre_hesapla()}")


# inheritence --> class ların miras alması demektir

# Person -> name, lastname, age ,eat() run(), drink()

# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        print("person Created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")

class Student(Person):    
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname) # Person constructora calısır. Super anlamına geliyor
        self.studentNumber =number
        print("Student Created")

    def who_am_i(self):
        print("I am a student")
    
    def sayHello(self):
        print("Hello I am a student")

class Teacher(Person):
    
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")


p1 = Person("Ali","Yilmaz")
s1 = Student("Çınar","Turan",123)
t1 = Teacher("Murat","Can","Math")


print(p1.firstname + " "+p1.lastname)
print(s1.firstname + " "+s1.lastname+ " "+ str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()

p1.eat()
s1.eat()

s1.sayHello()

t1.who_am_i()


class Movie():

    def __init__(self,title,director,duration):
        self.title = title
        self.director =director
        self.duration = duration
        print("Movie objesi oluşturuldu")
    
    def __len__(self):
        return self.duration

m = Movie("film adi","yönetmen",120)

print(type(m))
print(len(m))

# del m # objeyi siler
# print(m) # obje silindigi icin bulunamadı
































