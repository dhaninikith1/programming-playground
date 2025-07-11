class ChainingDict:
    def __init__(self, capacity):
        #Initial Capacity of the Map
        self.capacity = capacity

        #Building the chain lists depending on the capacity initialization
        self.currentDict = [[] for _ in range(capacity)]

        #Current map size
        self.size = 0

        #Resizing factor, if the map capacity exceeds
        self.resizeFactor = 0.7

    #Computes the cash for a given key
    def _findHash(self, key):
        return hash(key) % self.capacity
    
    #Resizes the map to a new capacity so we avoids keys landing on the same buckets
    def resize(self):
        #Making a copy of the current dictionary
        old_dict = self.currentDict

        #Increasing the capacity
        self.capacity = self.capacity * 2

        #Initializing the new Dictionary
        self.currentDict = [[] for _ in range(self.capacity)]

        #Resetting the Size 
        self.size = 0

        for bucket in old_dict:
            for (k,v) in bucket:
                self.putItemInDict(k,v)

    
    def putItemInDict(self, key, value):

        if(self.size / self.capacity) >= self.resizeFactor:
            self.resize()

        currentKeyHash = self._findHash(key)

        #where we are going to store the key, value in the table
        bucketToStore = self.currentDict[currentKeyHash]

        #Now we need to check if that bucket already has a same key
        #if key exists we update it, cause there cannot be duplicate keys
        for i, (Currentkey, Currentvalue) in enumerate(bucketToStore):
            if Currentkey == key:
                bucketToStore[i] = (key, value)
                return

        bucketToStore.append((key,value))
        self.size += 1

    def getItemfromDict(self, key):
        #we first find the hash for this key
        currentKeyHash = self._findHash(key)

        #if exists in the map fetch its bucket
        currentBucket = self.currentDict[currentKeyHash]

        #if the length of the bucket is zero then the key does not
        #exist in the Map and we return
        if len(currentBucket) == 0:
            return
        
        #if it exists we then loop over the bucket and check for the same key
        #then return its value
        for i, (k,v) in enumerate(currentBucket):
            if k == key:
                return v
    
    def removeItemFromDict(self, key):
        #Find the hash for the key
        currentKeyHash = self._findHash(key)

        #Find its bucket
        currentBucket = self.currentDict[currentKeyHash]

        #loop through the bucket and if the key matches
        # we delete that key and return 
        for i, (k, v) in enumerate(currentBucket):
            if k == key:
                del currentBucket[i]
                self.size -= 1
                return
    
    def printDict(self):
        return str([item for bucket in self.currentDict for item in bucket])
        
if __name__ == "__main__":
    dict = ChainingDict(2)
    dict.putItemInDict("apple", 10)
    dict.putItemInDict("banana", 20)
    dict.putItemInDict("apple", 99)  # update value
    dict.putItemInDict("grape", 30)
    dict.putItemInDict("lemon", 40)

    print(dict.printDict())