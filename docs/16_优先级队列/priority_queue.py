# -*- coding:utf-8 -*-

# 第二章拷贝的 Array 代码


class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

#####################################################
# heap 实现
#####################################################


class MaxHeap(object):
    """
    Heaps:
    完全二叉树，最大堆的非叶子节点的值都比孩子大，最小堆的非叶子结点的值都比孩子小
    Heap包含两个属性，order property 和 shape property(a complete binary tree)，在插入
    一个新节点的时候，始终要保持这两个属性
    插入操作：保持堆属性和完全二叉树属性, sift-up 操作维持堆属性
    extract操作：只获取根节点数据，并把树最底层最右节点copy到根节点后，sift-down操作维持堆属性

    用数组实现heap，从根节点开始，从上往下从左到右给每个节点编号，则根据完全二叉树的
    性质，给定一个节点i， 其父亲和孩子节点的编号分别是:
        parent = (i-1) // 2
        left = 2 * i + 1
        rgiht = 2 * i + 2
    使用数组实现堆一方面效率更高，节省树节点的内存占用，一方面还可以避免复杂的指针操作，减少
    调试难度。

    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)  # 维持堆的特性

    def _siftup(self, ndx):
        if ndx > 0:
            parent = int((ndx-1)/2)
            if self._elements[ndx] > self._elements[parent]:    # 如果插入的值大于 parent，一直交换
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)    # 递归

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]    # 保存 root 值
        self._count -= 1
        self._elements[0] = self._elements[self._count]    # 最右下的节点放到root后siftDown
        self._siftdown(0)    # 维持堆特性
        return value

    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # determine which node contains the larger value
        largest = ndx
        if (left < self._count and     # 有左孩子
                self._elements[left] >= self._elements[largest] and
                self._elements[left] >= self._elements[right]):  # 原书这个地方没写实际上找的未必是largest
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)


class PriorityQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self, priority, value):
        entry = (priority, value)    # 注意这里把这个 tuple push进去，python 比较 tuple 从第一个开始比较
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry
        else:
            return entry[1]

    def is_empty(self):
        return len(self._maxheap) == 0


def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())
    assert res == ['purple', 'orange', 'black', 'white']


def test_buildin_PriorityQueue():  # python3
    """
    测试内置的 PriorityQueue
    https://pythonguides.com/priority-queue-in-python/
    """
    from queue import PriorityQueue
    q = PriorityQueue()
    q.put((10, 'Red balls'))
    q.put((8, 'Pink balls'))
    q.put((5, 'White balls'))
    q.put((4, 'Green balls'))
    while not q.empty():
        item = q.get()
        print(item)


def test_buildin_heapq_as_PriorityQueue():
    """
    测试使用 heapq 实现优先级队列，保存一个 tuple 比较元素(tuple第一个元素是优先级)
    """
    import heapq
    s_roll = []
    heapq.heappush(s_roll, (4, "Tom"))
    heapq.heappush(s_roll, (1, "Aruhi"))
    heapq.heappush(s_roll, (3, "Dyson"))
    heapq.heappush(s_roll, (2, "Bob"))
    while s_roll:
        deque_r = heapq.heappop(s_roll)
        print(deque_r)


# python3 没有了 __cmp__ 魔法函数 https://stackoverflow.com/questions/8276983/why-cant-i-use-the-method-cmp-in-python-3-as-for-python-2
class Item:
    def __init__(self, key, weight):
        self.key, self.weight = key, weight

    def __lt__(self, other): # 看其来 heapq 实现只用了 小于 比较，这里定义了就可以 push 一个 item 类
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __str__(self):
        return '{}:{}'.format(self.key,self.weight)


def test_heap_item():
    """
    测试使用 Item 类实现优先级队列，因为 heapq 内置使用的是小于运算法，
    重写魔术 < 比较方法即可实现
    """
    import heapq
    pq = []
    heapq.heappush(pq, Item('c', 3))
    heapq.heappush(pq, Item('a', 1))
    heapq.heappush(pq, Item('b', 2))
    while pq:
        print(heapq.heappop(pq))
