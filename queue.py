class Queue(object):
    """
        循环队列
        默认队列容量为4，可在实例化时自定义
    """
    
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.index = -1
        self.head = 0
        self.tail = 0
        self.queue = []
        self.length = 0
        
        
    # 计数，返回长度
    def count(self):
        return self.length
    
    # 判满
    def full(self):
        if self.count() == self.capacity:
            return True
        return False
    
    # 判空
    def empty(self):
        if self.count() == 0:
            return True
        return False
    
    # 清除队列
    def clear(self):
        self.head = 0
        self.tail = 0
        self.queue = []
        self.length = 0
        
    
    
    # 插入队尾
    def put_in(self, value):
        if self.full():
            return False
        self.queue.append(value)
        self.tail = (self.tail + 1) % self.capacity
        self.length += 1
        return True
    
    # 冒出队头
    def get_out(self):
        if self.empty():
            return False
        frist = self.queue[0]
        del(self.queue[0])
        self.head = (self.head + 1) % self.capacity
        self.length -= 1
        return frist
    
    
    # 实现迭代
    def __iter__(self):
        self.index = -1
        return self
        
    def __next__(self):
        self.index += 1
        if self.index == self.length:
            raise StopIteration
        
        return self.queue[self.index]
            
        
        

