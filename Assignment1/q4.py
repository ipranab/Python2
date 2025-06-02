How does Python enforce access control to class attributes, and what is the difference
between public, protected, and private attributes?

Ans:
    Python enforces access control to class attributes by strict naming convention rather than strict
    access modifiers. 

    Difference between public, protected and private attributes are:- 
        ->Public: These are accessible everywhere from inside and also from outside of the class 
                    on the python program denoted by (name).
        ->Protected: These are intended to be accessed only withing class and subclass.These are denoted
                        by _(single underscore) . Eg- (_name).
        ->Private: These attributes are intended only to be accessed within class. These are denoted
                    by __ (double underscore). Eg- (__name).
