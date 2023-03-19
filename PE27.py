eq_value=[]
max_a=0
max_b=0
max1=0
for a in range(-999,1000):
  for b in range(0,1001):
   if a**2<4*b:
      s=0
      x=0
      while True:
        eq =x**2+a*x+b
        score=0
        for i in range(1, eq+1):
         if eq==1 or eq==0:
           break
         else:
          if eq%i ==0:
           score+=1
        if score==2:
           s+=1
           
        else:
           break
        
        x+=1
      if s>max1:
        max1=s
        max_a=a
        max_b=b
      eq_value.append(s)
      
     
print(max_a,max_b)  
print(max(eq_value))
