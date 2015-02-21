import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


class Rlist():
    def __init__(self, lname):
        self.lname = lname
        self.alist = []
        if self.exists():
            self.alist = self.get()

    def __repr__(self):
        return "Rlist(%r)" % (self.alist)

    def exists(self):
        result = False if r.exists(self.lname) is 0 else True
        return result

    def get(self, start=0, end=-1):
        f = r.lrange(self.lname, start, end)
        for i in range(len(f)):
            f[i] = f[i].decode('utf-8')
            f[i] = int(f[i]) if f[i].isdigit() else f[i]
        return f

    def append(self, thing):
        r.rpush(self.lname, thing)
        self.alist.append(thing)
        return True

    def delete(self):
        r.delete(self.lname)
        return True


class RDict():
    def __init__(self, hname):
        self.name = hname
        if self.exists():
            for k, v in r.hgetall(self.name):
                self[k] = v

    def __repr__(self):
        temp = {}
        for k, v in self.__dict__.items():
            if k is not 'name':
                temp[k] = v
        return "RDict(%s)=%r" % (self.name, temp)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        self.__dict__[key] = value
        return True

    def exists(self):
        result = False if r.exists(self.name) is 0 else True
        return result

    def set(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        for key, value in kwargs.items():
            r.hset(self.name, key, value)
        return True

    def pop(self, key):
        value = r.hget(self.name, key).decode('utf-8')
        if value.isdigit():
            value = int(value)
        r.hdel(self.name, key)
        delattr(self, key)
        return value

    def get(self, key):
        value = r.hget(self.name, key).decode('utf-8')
        if value.isdigit():
            value = int(value)
        r.hget(self.name, key)
        return value

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            r.hset(self.name,key,value) 
        return True

    def delete(self):
        r.delete(self.name)
        return True

    def keys(self):
        keys = r.hkeys(self.name)
        for i,j in enumerate(keys):
            keys[i] = j.decode('utf-8')
        return keys
    
    def values(self):
        values = r.hvals(self.name)
        for i,j in enumerate(values):
            values[i] = j.decode('utf-8')
        return values


# for testing
if __name__ == "__main__":
    list_name = "try2"
    x = Rlist(list_name)
    print(x)
    x.append(4)
    print(x)
    test.append(5000)
    test.delete()
    test = RDict('dell')
    result = test.pop('adolfo')
    print(test['adolfo'])
    test.update(boss="adolfo")
    test.delete()
    print(test)
    print(test.keys())
    print(test.values())
    test['boss'] = 5
    print(test)
    test.delete()
    print(test.boss)
    print(test.get())
