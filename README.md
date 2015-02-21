## Redis to Python objects

This module allows you to create objects that are (pretty much) python dictionaries and lists, which are stored in redis behind the scenes, using the [redis-py](https://github.com/andymccurdy/redis-py) library.  Redis stores everything as strings, but this module lets you use redis hashes and lists (almost) as if they're regular python dicts and lists.

