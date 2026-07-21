import random

class RandomizedSet:

    def __init__(self):
        self.num_list = []
        self.num_dict = {}
        

    def insert(self, val: int) -> bool:
        if val in self.num_dict:
            return False
        self.num_dict[val] = len(self.num_list)
        self.num_list.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val in self.num_dict:
            last_val = self.num_list[-1]
            val_index = self.num_dict[val]

            self.num_list[val_index] = last_val
            self.num_dict[last_val] = val_index
            self.num_list.pop()
            self.num_dict.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.num_list)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()