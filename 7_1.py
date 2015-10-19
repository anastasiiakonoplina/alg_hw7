import random

keys = [int(line.rstrip('\n')) for line in open('1000_keys.txt')]

def hashFunc(k, a, b, p, m):
	res = ((a * k + b) % p) % m
	return res

def collisionNum(keys, a, b, p, m):
	myHash = []
	colnumb = 0
	for key in keys:
		h_key = hashFunc(key, a, b, p, m)
		if h_key in myHash:
			colnumb += 1
		else:
			myHash.append(h_key)
	return colnumb

def test(keys):
	res = []
	result = []
	sizes = [1000, 10000, 100000, 1000000]
	for m in sizes:
		for i in range(1, 100):
			p = random.randint(m, 10 * m)
			a = random.randint(1, p)
			b = random.randint(0, p)
			colnumb = collisionNum(keys, a, b, p, m)
			res.append([str(m), str(p), str(a), str(b), str(colnumb)])
	for item in res:
		result.append(','.join(item))
	result = '\n'.join(result)
	return result

print test(keys)

