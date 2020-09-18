stock_price = {}
with open("Book1.csv","r") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        price = float(tokens[1])
        stock_price[day] = price

print(stock_price)
print(stock_price['9-Mar'])

class HashTable:
    def __init__(self):
        self.max=100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] =value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None


t = HashTable()
t['6-Mar'] = 130
t.arr
