class insieme:
  def __init__ (self, x,y):
    self.x=x
    self.y=y
    self.base=1
    
    
  def __iter__(self):
    return self
  
  def __next__(self):
    w=self.base**2
    self.base+=1
    if w>self.y:
        raise StopIteration
    self.base+=1
    return w
    
    
  
myes=insieme (1,30)     
        
for s in myes:
  print(s)     