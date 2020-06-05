# comment

# print('hello'+'world')
# print('what is ur name')
# myName = input()
# print('nice to meet u '+ myName)
# print(len(myName))
# print('what is your age')
# myAge = input()
# print('you wille be ' + str(int(myAge)+1) + 'in a yr')

def myfunc(funcstr):
  print("in function:"+funcstr)
  funcstr = "junk"
  print("in function 2:"+funcstr)
  return funcstr

# so far everything passes by value
def myfunc2(funcarr):
  print("in function:")
  for item in funcarr:
    print(item)
  funcarr = ["junk","junk2"]
  print("in function 2:")
  for item in funcarr: 
        print(item, end =' hi luisa lol ')
  return

myVar = ["string"]
print(myVar)
myfunc2(myVar)
print(myVar)