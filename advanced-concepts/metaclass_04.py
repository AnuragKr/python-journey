class PersonMeta(type):
    """A person metaclass"""
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
    
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and
                callable(subclass.name) and
                hasattr(subclass, 'age') and
                callable(subclass.age))
    
class PersonSuper:
    """A person superclass"""
    def name(self) -> str:
        pass

    def age(self) -> int:
        pass

class Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass."""
    pass

class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__"""
    pass

class Friend:
    """Built implicitly from Person
    Friend is a virtual subclass of Person since both required methods exist.
    Person not in Friend.__mro__"""
    def name(self):
        pass

    def age(self):
        pass

print(Employee.__mro__)

print(Friend.__mro__)

print(issubclass(Employee, Person))

print(issubclass(Friend, Person))

# Informal Interface useful for small projects and where low number of 
# programmers are working
# Not useful for larger applications