from flask import Flask
import redis
import socket

app = Flask(__name__)

# CONNECT TO REDIS
# Host 'redis-db' must match the Service Name in K8s and Docker Compose
cache = redis.Redis(host='redis-db', port=6379)

@app.route('/')
def hello():
    try:
        count = cache.incr('hits')
        return f'<h1>Hello DevOps!</h1> <p>This page has been visited <b>{count}</b> times.</p>'
    except redis.exceptions.ConnectionError:
        return '<h1>Error</h1> <p>Redis is not reachable. Check your Service names!</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)