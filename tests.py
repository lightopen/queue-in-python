from queue import Queue

q = Queue(3)

print("==========================")
print(q.head)
print(q.tail)
print(q.count())
print(q.capacity)
print(q.full())
print(q.empty())
for i in q:
    print(i)

q.put_in(3)

print("==========================")
print(q.head)
print(q.tail)
print(q.count())
print(q.capacity)
print(q.full())
print(q.empty())
for i in q:
    print(i)
    
q.put_in('aaa')

print("==========================")
print(q.head)
print(q.tail)
print(q.count())
print(q.capacity)
print(q.full())
print(q.empty())
for i in q:
    print(i)
    
    
q.put_in([1,2,2])


print("==========================")
print(q.head)
print(q.tail)
print(q.count())
print(q.capacity)
print(q.full())
print(q.empty())
for i in q:
    print(i)
    
H = q.get_out()

print("==========================")
print(H)
print(q.head)
print(q.tail)
print(q.count())
print(q.capacity)
print(q.full())
print(q.empty())
for i in q:
    print(i)
    
    
q.put_in([1,2,2])


print("==========================")
print(q.head)
print(q.tail)
print(q.count())
print(q.capacity)
print(q.full())
print(q.empty())
for i in q:
    print(i)
    