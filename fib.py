
def fib(number) 
   if number==0:
       fib_list=[]
   elif number==1:
       fib_list = [0]
   else:
       fib_list = [0, 1]
       x = 0
       last_index = 1
       while (x<number-2):
        fib_list.append(fib_list[last_index]+fib_list[last_index-1])
        last_index+=1
        x+=1




   return fib_list 


print (fib(20))
