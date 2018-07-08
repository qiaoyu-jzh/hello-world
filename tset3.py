#判断回数
def ispalindrome(n):
    return str(n)==str(n)[::-1]

output = filter(ispalindrome,range(1,1000))
print('1~1000',list(output))