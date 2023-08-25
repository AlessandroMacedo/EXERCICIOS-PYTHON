while True:
  try:
    if int(input("SEU ZE DA MANGA DIGITE 0 ou 10: ")) in range(11):
      print("Legal obrigado amigo.")
      break
    else:
      print("SEU FILHO DE CRISTO DIGITE SOMENTE 0 OU 10")
  except:
    print("SEU FILHO DE CRISTO DIGITE SOMENTE 0 OU 10 NÃO LETRAS")
