# Credit      : LyFromQixing a.k.a QueenLy
# Date        : 12 November 2021
# Description : A program that accepts two hexadecimal digits of exactly two digits long, performs an addition, and writes the result in two hexadecimal digits

hex_char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

def hex_to_dec(string):
  idx = 0
  while (hex_char[idx] != string[0]):
    idx += 1
  result = idx*16
  idx = 0
  while (hex_char[idx] != string[1]):
    idx += 1
  result += idx
  return result

def dec_to_hex(x):
  return hex_char[x//16] + hex_char[x%16]

A = input("Insert A: ")
B = input("Insert B: ")
hex_result = dec_to_hex(hex_to_dec(A) + hex_to_dec(B))
print(A, "+", B, "=", hex_result)
