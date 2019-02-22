import bcrypt
from sys import argv
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
MAX_LEN = 4
def main():
    if len(argv) < 2 or len(argv) > 2:
        print("Usage: python ./brute_force.py hash")
    
    hash_ = argv[1].encode("utf-8")
    print(hash_)
    # print(bcrypt.hashpw(hash_, bcrypt.gensalt(12)))
    brute_force(MAX_LEN, hash_)

def brute_force(max_len, hash):
    result = " " * (max_len + 1)
    salt = hash[:7]
    found = False
    for i in range(max_len + 1):
        if i == 0:
            continue
        found = generate_and_compare(result, hash, salt, 0, 4, i)
        if found:
            break


def generate_and_compare(result, hash_, salt, idx, minDepth, maxDepth):
    found = False
    for i in range(len(alphabet)):
        result = result[:idx] + alphabet[i] + result[idx + 1:]
        print(result)
        # result[idx] = alphabet[i]
        if idx == maxDepth - 1:
            if idx < minDepth:
                continue
            hashed = bcrypt.hashpw(result.encode('utf-8'), hash_)
            if hashed == hash_:
                print(f"Found: {result}")
                found = True
                return found
        else:
            found = generate_and_compare(result, hash_, salt, idx + 1, minDepth, maxDepth)
        if found:
            break
    return found

if __name__ == "__main__":
    main()