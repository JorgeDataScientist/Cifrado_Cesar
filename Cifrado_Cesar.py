alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


Continuar_Codificando = True

while Continuar_Codificando:
  direccion = input('Que quieres hacer, "codificar" o "decodificar":\n').lower()
  Mensaje = input(f'Escribe el mensaje a {direccion}:\n').lower()
  shift = int(input('Numero de Turnos:\n'))

  #Codigo para evitar que coloquen numeros (shift) mayores
  # a la cantidad de letras que tengo en "alphabet"
  shift = shift % 26


  #MODELO MAS PROFESIONAL DEL PROYECTO.
  #Codigo para opciones de "Codificar" y "Decodificar"
  def Cifrado_Cesar(Start_Texto, Shift_Saltos, Direccion_Cifrado):
    Texto_Final = ""
    if Direccion_Cifrado == 'decodificar':
      Shift_Saltos *= -1
    for caracter in Start_Texto:
      if caracter in alphabet:
        posicion = alphabet.index(caracter)
        NewPosicion = posicion + Shift_Saltos
        Texto_Final += alphabet[NewPosicion]
      else:
        Texto_Final += caracter
    print(f'El texto "{Mensaje}" se va a {Direccion_Cifrado}........\nResultado: {Texto_Final}')

  #Import logo del archivo Art
  from Art import logo
  print(logo)

  #llamado a ejecutar funcion
  Cifrado_Cesar(Start_Texto=Mensaje, Shift_Saltos=shift, Direccion_Cifrado=direccion)

  #Preguntar si continuamos codificando
  Pregunta = input('Escribe "SI" si quieres volver a codificar, de lo contrario, escribe "NO":\n').lower()
  if Pregunta == 'no':
    Continuar_Codificando = False
    print('Hasta Luego!!!!!!')




# #MODELO BASICO PARA REALIZAR EL PROYECTO
# #Funcion para Codificar
# def encriptar(Texto_Plano, Shift_Saltos):
#   Texto_Cifrado = ""
#
#   for letra in Texto_Plano:
#     posicion = alphabet.index(letra)
#     New_posicion = posicion + Shift_Saltos
#     New_letra = alphabet[New_posicion]
#     Texto_Cifrado += New_letra
#
#
# #Funcion para Decodificar
# def desencriptar(Texto_Cript, Shift_Saltos):
#   Texto_Descifrado = ""
#
#   for letter in Texto_Cript:
#     posicion = alphabet.index(letter)
#     New_posicion = posicion - Shift_Saltos
#     Texto_Descifrado += alphabet[New_posicion]
#   print(f'El texto Decodificado es: {Texto_Descifrado}')
#
# # Llamado de Funciones segun intereses
# if direccion == 'codificar':
#   encriptar(Texto_Plano=Mensaje, Shift_Saltos=shift)
# elif direccion == 'decodificar':
#   desencriptar(Texto_Cript=Mensaje, Shift_Saltos=shift)
# else:
#   print(f'El comando es Incorrecto')
# #--------------------------------------------------------