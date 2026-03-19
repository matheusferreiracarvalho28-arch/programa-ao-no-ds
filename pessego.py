a = int(input("digite o numero"))
b = int(input("digite o numero"))
pessego = True
def somar (a,b):
  a+b 
  print ()
  while pessego == True:
    print ("1 - Soma \n 2 - divisão\n 3 - subtração \n 4 - multiplicação \n 5  - porcentagem \n 0-sair")
    op = input ("digite uma opção: ")
    if op == "0": 
      pessego = False
    if op == "1":
      somar(a,b)
    if op == "2":
      resultado = a / b
      print (resultado)
    if op == "3":
      resultado = a - b
      print (resultado)
    if op == "4":
      resultado = a * b
      print (resultado)
    if op == "5":
      resultado = a % b
      print (resultado)