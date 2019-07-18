class QueueError(Exception):
    pass

class SQueue:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems==[]

    def enqueue(self,val):
         self._elems.append(val)
         print(val)
    def dequeue(self):
        if not self.is_empty():
            raise QueueError("Queue is empty")

        return self._elems.pop(0)





st=SQueue()
st.enqueue(1)
st.enqueue(2)
st.enqueue(3)
st.enqueue(4)
st.enqueue(5)
# while not st.is_empty():
# print(st._elems)


