def reverse(string):
    string = "".join(reversed(string))
    return string
  
s = "Řetězec"
  
print("Původní řetezec : ", end="")
print(s)
  
print("Obrácený řetězec : ", end="")
print(reverse(s))