class RandomizedSet(object):

    def __init__(self):
        self.nums=[]
        self.hash_table={}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hash_table:
            return False
        self.hash_table[val]=len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # 修复remove方法中的逻辑错误，需要更新hash_table中的索引映射    
        if val not in self.hash_table.keys():
            return False
        last_val=self.nums[-1]
        self.nums[self.hash_table[val]]=last_val
        self.hash_table[last_val]=self.hash_table[val]
        del self.hash_table[val]
        self.nums.pop()
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()