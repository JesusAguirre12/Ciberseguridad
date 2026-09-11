cards = """
7 10 3 9 5 9 5 K 6 K 6 6
6 K 7 J 6 3 9 5 5 A 9 K
7 9 8 2 6 K 9 4 6 K 6 6
5 4 9 2 7 7 8 6 3 9 4 9
"""

mapping = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 0
}

#nota juntamos i e i+1 porque por ejemplo e = 101 en ord
#al pasarlo a base 13 nos queda 7 10, y que pasa, si decodearamos ese conjunto de letras directamente nos da cualquier cosa
#analizando, nos damos cuenta que la conversion es facil de modelar

#en este tipo de problemas es mejor probar primero toda la cadena y si no tiene mucho sentido el resultado pensar en caracter por caracter

seq = cards.split()
print(seq)
nums = [mapping[x] for x in seq]
print(nums)
out = bytearray()

for i in range(0, len(nums), 2):
    value = nums[i] * 13 + nums[i+1]
    out.append(value)

print("HEX:")
print(out.hex())

print("\nLATIN1:")
print(out.decode("latin1"))

print("\nREPR:")
print(repr(out.decode("latin1")))
                                                                                                      
