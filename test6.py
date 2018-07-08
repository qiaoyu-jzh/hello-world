#返回函数
def createCounter():
    def f1():
        n=1
        while True:
            yield n
            n=n+1
    it=f1()
    def f2():
        return next(it)
    return f2


createA=createCounter()
print(createA(),createA(),createA())
'''#当下一次调用时，变量值改变，可以使用
 1.容器s[]
 2.生成器 如上
 3.nonlocal 关键词，可以改变 变量值
 4.声明global。
 '''
