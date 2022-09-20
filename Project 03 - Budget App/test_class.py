
class Tester:
    def __init__(self, category):
        self.name = category
        self.str_attrib = ''
        self.num_attrib = 0
    
    def give_str(self):
        print(self.str_attrib)
    
    def give_num(self):
        print(self.num_attrib)
    
    def swap_strs(self, other):
        self_str = self.str_attrib
        other_str = other.str_attrib

        self.str_attrib = other_str
        other.str_attrib = self_str 


# instantiate & check attributes of obj_a
obj_a = Tester('a_object')
obj_a.str_attrib = 'blue'
obj_a.num_attrib = 4

# print(obj_a.name)
obj_a.give_str()
# obj_a.give_num()


print('--------')


# instantiate & check attributes of obj_b
obj_b = Tester('b_object')
obj_b.str_attrib = 'orange'
obj_b.num_attrib = 8

# print(obj_b.name)
obj_b.give_str()
# obj_b.give_num()


# try to swap colors & check that it worked
obj_a.swap_strs(obj_b)
print('NEW obj a color: ' + str(obj_a.str_attrib))
print('NEW obj b color: ' + str(obj_b.str_attrib))
