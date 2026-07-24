class FreqStack:

    def __init__(self):
        self.freq={}
        self.group={}
        self.maxfreq=0
        

    def push(self, val: int) -> None:
        f=self.freq.get(val,0)+1
        self.freq[val]=f
        self.maxfreq=max(self.maxfreq,f)
        if f not in self.group:
            self.group[f]=[]
        self.group[f].append(val)


    def pop(self) -> int:
        k=self.group[self.maxfreq].pop()
        self.freq[k]-=1
        if not self.group[self.maxfreq]:
            self.maxfreq-=1
        return k
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()