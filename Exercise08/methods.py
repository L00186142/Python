'''
Script: oo1.py
By: NM
Purpose: Methods for creating and modifying
Date: 26CT23
'''
class my_object():
    def __init__(self, attr1, attr2=True):
         self.attr1 = attr1
         self.attr2 = attr2
    def my_method1(self):
            if self.attr2:
                print(f"Good morning {self.attr1}")
            else:
                print(f"No greeting {self.attr1}")

    my_object.my_method1()


    def my_method2(self, my_name:str):
        if self.attr2:
            print(f"Good morning {my_name}")
        else:
            print(f"No greeting {my_name}")


    my_object.my_method2(“Slartibartfast”)
                         

if __name__ == '__main__':
    object = methods()
    object.my_method1()
    object.my_method2()