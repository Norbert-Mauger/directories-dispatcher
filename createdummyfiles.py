import hashlib
import random as rand
import time
import string


def hexrandom(minint, maxint):
    x = str(rand.randint(int(minint), int(maxint)) + int(round(time.time() * 1000)))
    reval = hashlib.sha1(x.encode()).hexdigest()

    return reval


def create_dummy_files(num_files, dir):
    n = 1100000
    val = ''.join(rand.choices(string.ascii_uppercase + string.digits, k=n))

    start = time.time()
    for i in range(0, num_files):
        filename = hexrandom(0, 99999999999)
        print(filename)
        fh = open(dir+filename+'.txt', "w")
        slength = rand.choices([10, 100, 1024], [50, 40, 10])
        content = val[:slength[0] * 1024]
        fh.write(content)
        fh.close()
    end = time.time()
    return "{0} created in {1:.2f} seconds".format(num_files, end - start)





