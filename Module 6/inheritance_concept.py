# base class or parent class

class BaseClass:
    # It's the parent class, from here BaseClass will share the all common attributes to child classes.
    pass

# Derived class
class DerivedClass(BaseClass):
    # It's a child class here child will receive all common attributes from BaseClass.
    pass

""" 
1. Simple inheritance: parent class --> child class (Gadget --> Phone) (Gadget --> Laptop)
2. Multi-level inheritance: Grandpa --> Parent --> Child (vehicle --> BUS --> A/C BUS)
(Vehicle --> Track --> PickUp)
3. Multiple inheritance: Student(Family, Sports, School)
4. Hybrid inheritance: Grandpa --> Father, Uncle, Aunty --> Child(Father, Uncle)
"""