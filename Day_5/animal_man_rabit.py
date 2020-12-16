class Animal(object):

    def __init__(self , age , name = ""):
        self.age = age
        self.name = name

    def __str__(self):
        return '<ANIMAL>' + str(self.name) + ':' + str(self.age)

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_name(self , name):
        self.name = name



class Man(Animal):

    def __init__(self , age , name , has_moustache):
        Animal.__init__(self , age)
        self.set_name(name)
        self.has_moustache = has_moustache

    def __str__(self):
        if(self.has_moustache == True):
            mous = 'With a moustache!'
        else:
            mous = 'Without a moustache! Grow One!'
        return '<MAN>' + str(self.name) + ':' + str(self.age) + ':' + mous

    def get_moustache(self):
        return self.has_moustache


firstMan = Man(64 , 'Oliver' , True)
print(firstMan)

