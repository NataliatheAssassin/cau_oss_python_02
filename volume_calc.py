print("가로:", end="")
x = float(input())
#print("")

print("세로:", end="")
z = float(input())
#print("")

print("높이:", end="")
y = float(input())
#print("")

volume = x * z * y
print("박스의 부피는", end="\n")
print(round(volume, 1), end="")
print("입니다.")