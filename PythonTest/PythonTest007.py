# import random
#
# a=0;b=0;c=0
#
# while 1:
#     playerStr = input("请输入[0剪刀 1石头 2布 9结束]")
#     player = int(playerStr)
#     mac = random.randint(0, 2)
#
#     if player == 9:
#         print("胜利局数：%d，失败局数：%d，平局数：%d"%(a,c,b))
#         exit()
#     if (player == 0 and mac == 2) or (player == 1 and mac == 0) or (player == 2 and mac == 1):
#         print("你赢了")
#         a+=1
#     elif player == mac:
#         print("平局,要不要再来一局")
#         b+=1
#     else:
#         print("你输了")
#         c+=1


i=987

print(i/100)

print(i//100)

print(i%100)

print((i//10)%10)

