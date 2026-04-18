from abc import ABC, abstractmenthod

class Absclass(ABC):
    
    def print(self,x):
        print("passed value:", x)

    @abstractmenthod
    def task(self):
        print("we re inside absclass task")

class test_class(Absclass):
        def task(self):
            print("we are inside test_class task")
test_obj = test_class()
test_obj.task()
test_obj.print(100)
    