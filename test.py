import math
for i in range(360):
    x = math.cos(math.radians(i))
    y = math.sin(math.radians(i))
    print(math.atan2(y, x))

    


