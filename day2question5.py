class Poly:
    def __init__(self,*values):
        self.values=list(values)
    def __add__(self,other):
        max_len=max(len(self.values),len(other.values))
        a_value=[0]*(max_len-len(self.values))+self.values
        b_value=[0]*(max_len-len(other.values))+other.values
        result=[a+b for a,b in zip(a_value,b_value)]
        return Poly(*result)
