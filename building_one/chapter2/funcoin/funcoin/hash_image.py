from hashlib import sha256

file = open("./image/random.jpg", "rb")
hash = sha256(file.read()).hexdigest()
print(hash)

