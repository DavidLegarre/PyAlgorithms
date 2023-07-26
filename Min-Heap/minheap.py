import sys

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize+1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    
    def parent(self, pos):
        # This function returns the position of the parent
        return pos//2


    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        return pos*2 > self.size

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
