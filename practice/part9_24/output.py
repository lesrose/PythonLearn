# x = int(input('input first number'))
# y = int(input('input second number'))
# sum = x + y
# print("sum=%d" % (sum)

# name = input('input your name')
# x = int(input('input your ch '))
# y = int(input('input your math '))
# z = int(input('input your en '))
name='sada'
x=98
y=56
z=78
sum = x + y + z
print("name:{},ch:{},math:{},en:{},sum:{},avg:{}".format(name, x, y, z, sum, sum / 3))
print(f"name:{name},ch:{x},math:{y},en:{z},sum:{sum},avg:%.3f" % (sum / 3))
print(f"name:{name},ch:{x},math:{y},en:{z},sum:{sum},avg:%d" % (sum / 3))
print("name:{},ch:{},math:{},en:{},sum:{},avg:{:.0f}".format(name, x, y, z, sum, sum / 3))
