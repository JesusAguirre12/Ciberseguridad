from functools import reduce

'''
reduce(...)
        reduce(function, iterable[, initial], /) -> value

        Apply a function of two arguments cumulatively to the items of an iterable, from left to right.

        This effectively reduces the iterable to a single value.  If initial is present,
        it is placed before the items of the iterable in the calculation, and serves as
        a default when the iterable is empty.

        For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
        calculates ((((1 + 2) + 3) + 4) + 5).

'''
def safeXor(a,b): # in case of none input
    if a is None: return b
    if b is None: return a
    if a==b: return not a
    return None

from functools import reduce
flag = b"01"
print(len(flag))
iv = [True, True, False, True, True, True, None, True, True, False, False, False, None, False, True, True, None, True, True, True, True, False, True, None, False, None, None, None, False, None, False, True, True, True, True, False, False, False, False, False, None, True, True, None, None, False, None, None, False, True, True, False, None, None, None, None, False, False, False, False, False, False, None, None, True, None, True, None, True, False, None, True, False, False, None, None, True, None, True, None, None, True, None, False, None, True, False, True, None, True, None, False, False, False, True, False, False, True, False, False, None, True, False, False, False, True, None, False, True, None, False, None, False, True, True, None, False, True, True, False, None, None, True, True, False, True, None, True, True, True, True, True, False, None, True, None, None, None, None, None, True, None, True, True, True, False, None, False, True, True, True, False, None, True, None, True, True, False, None, None, False, False, False, False, False, None, False, True, None, None, True, True, True, False, False, True, None, None, True, False, True, False, None, True, True, False, False, True, None, True, True, False, None, True, True, True, None, True, True, False, False, True, False, False, None, True, None, False, True, False, False, True, False, False, None, False, True, False, None, None, True, None, True, False, True, None, None, True, None, False, True, True, None, True, False, None, False, False, None]
'''
1
2
8
13
26
104
728
364
80
91
8744
3851
3280
59048
'''
op=0
for _ in range(len(flag)):
   iv = iv[1:] + [reduce(safeXor,iv)] 
   
initial = iv

for _ in range(2**20):
   iv = iv[1:] + [reduce(safeXor,iv)]
   op+=1
   if(initial == iv):
       break   

print(op)
