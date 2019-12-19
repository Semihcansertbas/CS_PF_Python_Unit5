import math  # import module math to use sqrt method

def my_sqrt(a):
    x = 1
    while True:
        y = (x + a/x)/2.0  
        if y == x:
            break
        x = y
    return x

def test_sqrt():
    for a in range(1, 26): #values from 1 to 25
        v1 = my_sqrt(a)
        v2 = math.sqrt(a)
        diff = abs(v1-v2)
        print("a = ", a, " | my_sqrt(a) = ", v1, " | math.sqrt(a) = ", v2, " | diff = ", diff)
    
def main():
    test_sqrt()

if __name__ == "__main__":
    main()
