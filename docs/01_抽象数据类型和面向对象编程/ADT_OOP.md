# Python 一切皆对象(面向对象编程)


在后面实现新的数据类型时，使用 python 的 class 实现，它包含属性和方法。
属性一般是使用某种特定的数据类型，而方法一般是对属性的操作。后续实例不会使用继承等特性。


# 什么是抽象数据类型 ADT

实际上 python 内置的 list 就可以看成一种抽象数据类型。

ADT: Abstract Data Type，抽象数据类型，我们在组合已有的数据结构来实现一种新的数据类型， ADT 定义了类型的数据和操作。

我们以抽象一个背包(Bag) 数据类型来说明，背包是一种容器类型，我们可以给它添加东西，也可以移除东西，并且我们想知道背包里
有多少东西。于是我们可以定义一个新的数据类型叫做 Bag(data;method).

```py
class Bag:
    """ 背包类型 """
    pass
```


# 实现一个 Bag ADT
视频中我们将使用 python 的 class 来实现一个新的容器类型叫做 Bag。


# 实现 ADT 我们应该注意什么？
- 如何选用恰当的数据结构作为存储？
- 选取的数据结构能否满足 ADT 的功能需求
- 实现效率如何？


# QA：
- python 的魔术方法`__len__` ,方法
- 使用 pytest 运行单元测试，保证我们实现的数据结构和算法是正确的。

# 延伸阅读：

[数据结构与算法--ADT](http://www.atjiang.com/data-structures-using-python-ADT/)

[http://www.nhu.edu.tw/~chun/CS-ch12-Abstract%20Data%20Types.pdf](http://www.nhu.edu.tw/~chun/CS-ch12-Abstract%20Data%20Types.pdf)

[pytest](https://www.jianshu.com/p/932a4d9f78f8)