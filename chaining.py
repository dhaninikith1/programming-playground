class ChainingDict:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _findHash(self, key):
        return hash(key) % self.capacity
    
    def putItemInDict(self, key, value):
        currentKeyHash = self._findHash(key)

        #where we are going to store the key, value in the table
        bucketToStore = self.table[currentKeyHash]

        #Now we need to check if that bucket already has a same key
        #if key exists we update it, cause there cannot be duplicate keys

        for i, (Currentkey, Currentvalue) in enumerate(bucketToStore):
            if Currentkey == key:
                bucketToStore[i] = (key, value)
                return

        bucketToStore.append((key,value))

    def getItemfromDict(self, key):
        #we first find the hash for this key
        currentKeyHash = self._findHash(key)

        #if exists in the map fetch its bucket
        currentBucket = self.table[currentKeyHash]

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
        currentBucket = self.table[currentKeyHash]

        #loop through the bucket and if the key matches
        # we delete that key and return 
        for i, (k, v) in enumerate(currentBucket):
            if k == key:
                del currentBucket[i]
                return
    
    def printDict(self):
        return str([item for bucket in self.table for item in bucket])
        
if __name__ == "__main__":
    dict = ChainingDict(2)
    dict.putItemInDict("apple", 10)
    dict.putItemInDict("banana", 20)
    dict.putItemInDict("apple", 99)  # update value
    dict.putItemInDict("grape", 30)
    dict.putItemInDict("lemon", 40)

    print(dict.printDict())