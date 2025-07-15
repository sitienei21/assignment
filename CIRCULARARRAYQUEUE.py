class CIRCULARARRAYQUEUE:
    """
    A CIRCULAR QUEUE IMPLEMENTATION USING AN ARRAY.

    Think of the array as a circular road: once you reach the end,
    you wrap around to the beginning.
    """

    DEFAULT_CAPACITY = 10  # Max initial slots

    def _init_(self):
        self._data = [None] * CIRCULARARRAYQUEUE.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def _len_(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        item_to_dequeue = self._data[self._front]
        self._data[self._front] = None  # Helps garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return item_to_dequeue

    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # Double the capacity

        back_index = (self._front + self._size) % len(self._data)
        self._data[back_index] = element
        self._size += 1

    def _resize(self, new_capacity):
        old_data = self._data
        self._data = [None] * new_capacity
        current_index = self._front

        for i in range(self._size):
            self._data[i] = old_data[current_index]
            current_index = (current_index + 1) % len(old_data)

        self._front = 0


class Empty(Exception):
    """Custom exception raised when queue operations are invalid on an empty queue."""
    def _init_(self, message="Queue is empty"):
        super()._init_(message)


if __name__ == "_main_":
    queue = CIRCULARARRAYQUEUE()

    print("QUEUES USING CIRCULAR ARRAYS")
    print(f"The initial queue size is: {len(queue)}")
    print(f"Is queue empty? {queue.is_empty()}")

    print("\nEnqueueing people into the queue:")
    elements_to_enqueue = ['Alice', 'Bob', 'William', 'Dorothy', 'Jessica']
    for person in elements_to_enqueue:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    print(f"\nPerson at the front of the line: {queue.first()}")

    print("\nServing people from the front of the queue:")
    for i in range(3):
        served = queue.dequeue()
        print(f"Served: {served}. Queue size is now: {len(queue)}")

    print("\nAdding more people to test wrap-around behavior:")
    more_people = ['Frank', 'Linda', 'Ford']
    for person in more_people:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    print(f"\nPerson currently at the front: {queue.first()}")
    print(f"Total people still in queue: {len(queue)}")

    print("\nInternal State:")
    print(f"Front index: {queue._front}")
    print(f"Array contents: {queue._data}")