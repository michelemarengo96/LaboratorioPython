class insieme:
  def __init__ (self, x,y):
    self.x=x
    self.y=y
    self.si=1
    
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.si>=self.y:
        raise StopIteration
    if self.si>=self.x: 
       tmp=self.si
       self.si=(3*self.si)/2
       return tmp

    self.si=(3*self.si)/2
    
  
myes=insieme (5,10)     
        
for s in myes:
  print(s)     