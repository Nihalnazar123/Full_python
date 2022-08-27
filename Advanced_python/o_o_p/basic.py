# object-oriented programing
# -------------------------
# class- class is used to create blueprint of object
# object- it is a real world entity
# reference- it is used to store object(operations)

class person:
    def read(self):   # the function inside the class is called method        # self is a instance keyword.instance variable is used to point to the current instance
        print('person is reading')
    def walk(self):
        print('person is walking')

# object is needed to access class and object is stored in reference
# we can create many objects with same class
pe=person()
pe.walk()
pe.read()

pe1=person()
pe1.read()
pe1.walk()