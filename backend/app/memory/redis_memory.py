
import redis

r = redis.Redis(host="localhost", port=6379)

def save_memory(user, data):
    r.set(user, data)

def get_memory(user):
    return r.get(user)
