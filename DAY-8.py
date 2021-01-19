''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

n = int(input())
s = str(int(n))
d = len(s)
sum = 0
t = n
while n>0:
    r = n%10
    sum = sum + pow(r,d)
    n//=10
if t == sum:
    print(True)
else:
    print(False)
