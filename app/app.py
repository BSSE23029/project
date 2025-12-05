import os
from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis (Host will be defined in env vars later)
redis_host = os.environ.get('REDIS_HOST', 'localhost')
try:
    cache = redis.Redis(host=redis_host, port=6379)
    cache.ping()
    redis_connected = True
except:
    redis_connected = False

@app.route('/')
def hello():
    if redis_connected:
        count = cache.incr('hits')
        return f'<h1 style="color:blue;">DevSolutions v2</h1><p>Page viewed {count} times.</p>'
    return '<h1 style="color:green;">DevSolutions v1</h1><p>Redis not connected (Standalone Mode).</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)