#两个装饰器。
def makeBold(fun):
    print('----a----')

    def inner():
        print('----1----')
        print('<b>'+fun()+'<b>')
        return '<b>' + fun() + '</b>'

    return inner


def makeItalic(fun):
    print('----b----')

    def inner():
        print('----2----')
        print('<i>' + fun() + '</i>')
        return '<i>' + fun() + '</i>'

    return inner


@makeBold
@makeItalic
def test():
    print('----c----')
    print('----3----')
    print('hello python decorator')
    return 'hello python decorator'


test()
'''
ret = test()
print(ret)
'''