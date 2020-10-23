#iterator
class Topten:
    def __init__(self) -> None:
        self.num = 1
    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration

value = Topten()
for i in value:
    print(i)