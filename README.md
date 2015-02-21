## Redis to Python objects

A small module mapping python lists and dictionaries to redis hashes and lists using the [redis-py](https://github.com/andymccurdy/redis-py) library.  Redis stores everything as strings, but this module lets you use redis hashes and lists (almost) as if they're regular python dicts and lists.