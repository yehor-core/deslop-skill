s = input().split()
n = int(s[0])

st = ['a','b','c','d','e','f','g','h','i','j','k']

#initialize
inis = []

def print_str( arry , num):
   str_a = ''
   for i in range(num):
     #print(arry,i)
     str_a = str_a + st[arry[i]-1]
   print(str_a)

# len = 1 .. 10
def do_number_n( len ):
   global inis
   tsti = 0
   k = len - 1    
   print_str( inis , len)
   while True:
      inis[k] += 1
      for j in range(k,0,-1):
         #print(inis[0:j],j)
         if ( max(inis[0:j]) + 2 ) <= inis[j]  :
         #if ( inis[j-1] + 2 ) <= inis[j]  :
            inis[j-1] += 1
            inis[j] = 1
         #print('test:  {},{},   {}'.format(j,k,inis))
            
      #最後まで行った。
      if inis[0] > 1 :
         return        
      print_str( inis , len)
  
def main():
  global inis
  inis = [1,1,1,1,1,1,1,1,1,1,1]
  #do_number_n(1)
  #return
  for j in range(1,n+1):
  #for j in range(n+1,1,-1):
    #print(j)
    inis = [1,1,1,1,1,1,1,1,1,1,1]
    do_number_n(j)
    
main()
exit()
#loop
i = 0
k = n - 1 
print_str( inis,3 )
while True:
   i += 1
   if i > 10 :
      break
   if ( inis[k-1] + 1 )== inis[k]  :
      inis[k-1] = inis[k-1] + 1 
      inis[k] = 1
   print_str( inis,3 )
   inis[k] = inis[k] + 1
