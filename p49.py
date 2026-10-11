import redis
r = redis.Redis(host='localhost', port=6379, db=0)

r.set('006', 'behrang mohajer')
print(r.get('006'))
