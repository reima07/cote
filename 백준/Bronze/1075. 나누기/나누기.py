import sys

N = int(input())
F = int(input())


if (N//100*100)%F == 0:
    print("00")
elif (F-(N//100*100)%F) < 10:
    print(f"0{F - (N//100*100)%F}")
else:
    print(F - (N//100*100)%F)