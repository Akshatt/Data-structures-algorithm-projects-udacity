from collections import defaultdict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.kvdict = defaultdict()
        self.Keyqueue = []
        self.cache_size = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.kvdict.get(key):
            self.Keyqueue.remove(key)
            self.Keyqueue.append(key)
            return self.kvdict[key]
        else:
            return -1
            
    def set(self, key, value):
        # Set the value of key. If key is in queue, then remove it and append it again.
        #If the cache is at capacity remove the oldest item. 
        if key in self.Keyqueue:
            self.Keyqueue.remove(key)
            
        elif len(self.Keyqueue) >= self.cache_size:
            del self.kvdict[self.Keyqueue.pop(0)]
        
        self.kvdict[key] = value
        self.Keyqueue.append(key)            

our_cache = LRU_Cache(5)

our_cache.set(1, 10);
our_cache.set(2, 20);
our_cache.set(3, 30);
our_cache.set(4, 40);
print("Setting 10 for 1")
print("Setting 20 for 2")
print("Setting 30 for 3")
print("Setting 40 for 4")

# Test Case 1 -- Element is present in the Cache and by calling get function it becomes most recently used.

print("Get value for key 1")
#Should return 10
print(our_cache.get(1)) # returns 1

print("Get value for key 2")
#Should return 20                   
print(our_cache.get(2))       # returns 2


# Test Case 2 -- Element is not present in the Cache. 

print("Get value for key 9")
#Should return -1 because 9 is not present in the cache     
print(our_cache.get(9))



our_cache.set(5, 50) 
print("Setting 50 for 5")
our_cache.set(6, 60)
print("Setting 60 for 6")


#Test Case 3 -- Element was removed from the Cache as it was LRU and cache capacity was full. 

print("Get value for key 3")
#Should return -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))      



