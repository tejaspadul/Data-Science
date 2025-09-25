from collections import deque

# Queue using deque
queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", queue)

# Dequeue
print("Dequeued:", queue.popleft())
print("Queue after dequeue:", queue)

# Peek front
print("Front element:", queue[0])

# Check empty
print("Is empty?", len(queue) == 0)
