import math


class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def parent(self, i):
        return math.floor((i - 1) / 2)

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        if not self.heap:
            return None

        minimum = self.heap[0]

        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)

        return minimum

    def search(self, value):
        return self.heap.index(value)

    def _heapify_up(self, index):
        parent_index = self.parent(index)

        while index > 0 and self.heap[index] < self.heap[parent_index]:
            # Swap the element with its parent
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index],
            )

            # Move to the parent index for the next iteration
            index = parent_index
            parent_index = self.parent(index)

    def _heapify_down(self, index):
        while True:
            left_child = self.left_child(index)
            right_child = self.right_child(index)
            smallest = index

            if (
                left_child < len(self.heap)
                and self.heap[left_child] < self.heap[smallest]
            ):
                smallest = left_child

            if (
                right_child < len(self.heap)
                and self.heap[right_child] < self.heap[smallest]
            ):
                smallest = right_child

            if smallest != index:
                # Swapp the element with the smallest child
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )
                # Move to the smallest child index for the next iteration
                index = smallest
            else:
                break


if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(8)
    min_heap.insert(2)

    print(min_heap)
    print(min_heap.extract())
    print(min_heap)
