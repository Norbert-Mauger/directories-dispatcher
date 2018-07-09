import os
import time


def create_subdirs(dir):
    start = time.time()
    files = (file for file in os.listdir(dir)
     if os.path.isfile(os.path.join(dir, file)))

    for filename in files:

        print(os.path.join(dir, filename))
        prefix = filename[:2]
        try:
            os.stat(dir + prefix)
        except:
            os.mkdir(dir + prefix)

        os.rename(dir+filename, dir + prefix + "/" + filename)
        continue

    end = time.time()
    return "all files moved in subdirs in {0:.2f} seconds".format(end - start)





