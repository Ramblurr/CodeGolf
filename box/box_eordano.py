r=range
s=lambda x:isinstance(x,str)
w=lambda x:reduce(max,[len(i)if s(i)else w(i)+4 for i in x])
z=lambda b,x:''.join(b for i in r(x))
def g(n=1):
 t=[]
 for i in r(n):
  x=raw_input('')
  try:t+=[g(int(x))]
  except:t+=[x]
 return t
o=list.append
def y(c,m):
 f='| ';h=' |';e=z('-',m+2);a='.'+e+'.';b="'"+e+"'";t=[a]
 for i in c:
  if s(i):o(t,f+i+z(' ',m-len(i))+h)
  else:[o(t,f+j+h)for j in y(i,m-4)]
 return t+[b]
x=g()[0];m=w(x);print '\n'.join(y(x,m))
print x
print m