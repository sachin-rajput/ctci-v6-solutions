class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None
        
    class Node(object):
        
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # this would O(1)
        if key not in self.map:
            return -1
        
        # this would O(1) to retreive requested Node by key
        selectedNode = self.map.get(key)
        self.remove(selectedNode)
        self.setHead(selectedNode)
        return selectedNode.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            # this would O(1) to retreive requested Node by key
            old = self.map.get(key)
            old.value = value #update the value attribute
            #remove old from tail and add to head
            self.remove(old)
            self.setHead(old)
        else:
            newNode = self.Node(key, value)
            
            if len(self.map) >= self.capacity:
                del self.map[self.tail.key]
                self.remove(self.tail)
                self.setHead(newNode)
            else:
                self.setHead(newNode)
            self.map[key] = newNode
            
    
    def remove(self, n):
        if (n.prev != None):
            n.prev.next = n.next
        else:
            self.head = n.next
        
        if (n.next != None):
            n.next.prev = n.prev
        else:
            self.tail = n.prev
    
    def setHead(self, n):
        n.next = self.head
        n.prev = None
        
        if (self.head != None):
            self.head.prev = n
        
        self.head = n
        
        if self.tail == None:
            self.tail = self.head
        
    def printNode(self, n):
        print("Key: ",n.key," Value: ", n.value)


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)

cache.printNode(cache.head)
cache.printNode(cache.tail)

print(cache.get(1))    # returns 1

cache.printNode(cache.head)
cache.printNode(cache.tail)

cache.put(3, 3)   # evicts key 2

cache.printNode(cache.head)
cache.printNode(cache.tail)

print(cache.get(2))       # returns -1 (not found)

cache.put(4, 4)    # evicts key 1
print(cache.get(1))      # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))     # returns 4