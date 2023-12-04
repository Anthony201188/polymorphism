""" Exercise(Polymorphism - Negator):
Write a class called Negator
  use @singlesipatchmethod on the neg method
if you use int  as argument return the negative value of this integer
if you use bool  return the oppsite boolean
if you use str return an empty string """
from functools import singledispatchmethod

class Negator:

    @singledispatchmethod
    def neg (self, arg):
        raise NotImplementedError (f"cannot negate a {type(arg)}")
    
    @neg.register
    def _(self, arg:int):
        print(arg * -1)
    
    @neg.register
    def _(self, arg:bool):
        print(not arg)
    
    @neg.register   
    def _(self, arg:str):    
       self.arg = arg
       arg = ""
       print(arg)


obj = Negator()
obj.neg(1) #--> -1
obj.neg(True) #--> False
obj.neg('Hello') #--> ''


    