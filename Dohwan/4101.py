def big():
    while(True):
        num1, num2 = map(int,input().split())
        if num1 == 0 and num2 == 0:
            break
        else:
            if num1 > num2:
                print("Yes")
            else:
                print("No")

big()