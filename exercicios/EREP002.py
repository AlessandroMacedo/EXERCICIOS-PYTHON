"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""
""""
while True:
  usuario = input('Digite uma senha de usuario: ')
  senha = input('Digite uma senha: ')
  if usuario == senha:
    print("SENHA IGUAL AO USUARIO NÃO PAPAI")
  else:
    print("CADASTRADO COM SUCESSO!")
    break
"""

usuario = input('Digite uma senha de usuario: ')
senha = input('Digite uma senha: ')
while usuario == senha:
  print("NÃO PODE SER IGUAL CAVALO")
  usuario = input('Digite uma senha de usuario: ')
  senha = input('Digite uma senha: ')
else:
  print("sucesso!!!")


'''
while input("Digite o nome de usúario: ") == input("Digite a senha do usúario: "):
  print("A senha não pode ser o mesmo nome de usúario")
else:
  print("Login bem sucedido!")


def bucetao():
  if input("Digite o nome de usúario: ") == input("Digite a senha do usúario: "):
     print("A senha não pode ser o mesmo nome de usúario")
     return bucetao()
  else:
    print("Login bem sucedido!")



bucetao()
'''
