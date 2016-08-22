# -*- coding : utf-8 -*- 

from hamming import Frame , Hamming

# Provocar erro
# Consertar Frame

options = [
		"Enviar Frame",
		"Receber Frame",
]

paridades = {"par":"pair","impar":"odd"}

def show_menu():
	for option , action in enumerate(options,start=1):
		print("{} - {}".format(option,action))

print("#####################################")
print("Implementação do Algoritmo de Hamming")
print("#####################################")
print("")

continuar = "s"

while continuar == "s":

	while True:
		try:
			valor_paridade = str(input("Valor da paridade: par ou impar : "))

			paridade = paridades.get(valor_paridade,None)
			hamming = Hamming(paridade)
			break

		except ValueError:
			print("Digite um valor de paridade válido ")
			

	conteudo = str(input("Digite o conteúdo do frame: "))

	frame = Frame(conteudo)

	while not frame.is_valid():
		conteudo = str(input("Digite o conteúdo do frame: "))
		frame = Frame(conteudo)
		
	mudar_frame = str(input("Deseja provocar um erro? s / n : "))

	frame_encoded = hamming.encode(frame)

	if mudar_frame == "s":

		while True:
			try:

				posicao = int(input("Digite o número da posição: "))
				frame_encoded = frame_encoded.change_bit(posicao)
				break

			except ValueError:

				print("Digite uma posição válida: ")									
		
	print("O conteúdo do frame enviado é : {}".format(frame_encoded))

	verificar_validade = str(input("Deseja verificar se o frame está correto ? s / n: "))

	validade = hamming.check(frame_encoded)

	if validade:

		print("O frame {} está correto.".format(frame_encoded))

	else:

		posicao_errada = hamming.wrong_position(frame_encoded)

		print("O frame {} , está incorreto , e o bit errado é o : {}".format(frame_encoded,posicao_errada))

		consertar = str(input("Deseja consertar o frame? s / n : "))

		if consertar == "s":

			fix_frame = hamming.fix(frame_encoded)

			print("O frame errado {} , foi consertado : {}".format(frame_encoded,fix_frame))

	continuar = str(input("Deseja continuar ? s / n : "))