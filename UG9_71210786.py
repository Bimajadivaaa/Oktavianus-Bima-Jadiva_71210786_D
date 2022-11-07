class Node:
    def __init__(self,data,priority):
        self._data = data
        self._priority = priority
        self._next = None
class PriorityQueueSortedList:
    def __init__(self):
        self._data = []
    def peek(self):
        print(self._data[0])
    def add(self, n, p):
        if len(self._data):
            temp = 0
            while self._data[temp][1] < p:
                temp = temp + 1
            self._data.insert(temp, (n, p))
        else:
            self._data.append((n, p))
    def update(self, p, n):
        temp = 0
        while self._data[temp][1] != p:
            temp = temp + 1
        self._data[temp] = (n, p)
    def remove(self):
        del self._data[0]
    def removePriority(self, p):
        print("Data Prioritas Tertinggi: ", end="")
        temp = 0
        while self._data[temp][1] != p:
            temp = temp + 1
        del self._data[temp]
    def printIsiQueue(self):
        print("Isi semua Queue: ", end="")
        for i in self._data[:-1]:
            print("{}," .format(i), end=" ")
        print("{}" .format(self._data[-1]))
sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()