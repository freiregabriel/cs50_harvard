from time import sleep
# will never overflow unless the machine runs out of memory
i = 1
while True:
    print(i)
    i *= 2
    sleep(.5)