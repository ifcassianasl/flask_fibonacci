import redis
import json
from flask import Flask
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379, db=0)


@app.route('/')
def home():
    return 'Enter a index number'


@app.route('/<int:fibonacci_index>')
def find_fibonacci(fibonacci_index):
    if cache.exists('fibonacci_sequence'):
        fibonacci_sequence = json.loads(cache.get('fibonacci_sequence'))
    else:
        fibonacci_sequence = []

    if(len(fibonacci_sequence) <= fibonacci_index):
        for i in range(len(fibonacci_sequence), fibonacci_index + 1):
            next_number = fibonacci_sequence[i-2] + fibonacci_sequence[i - 1] if len(
                fibonacci_sequence) > 1 else i + 1

            fibonacci_sequence.insert(i, next_number)

    cache.set('fibonacci_sequence', json.dumps(fibonacci_sequence))

    return json.dumps(fibonacci_sequence[fibonacci_index])


if __name__ == '__main__':
    app.run(debug=True)