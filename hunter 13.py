class Stack:
    def __init__(loki):
        loki.items = []
 
    def is_empty(loki):
        return loki.items == []
 
    def push(loki, data):
        loki.items.append(data)
 
    def pop(loki):
        return loki.items.pop()
 
 
s = Stack()
text = input(' ')
 
for character in text:
    s.push(character)
 
reversed_text = ''
while not s.is_empty():
    reversed_text = reversed_text + s.pop()
 
if text == reversed_text:
    print('YES')
else:
    print('NO')
