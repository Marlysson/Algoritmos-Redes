# -*- coding : utf-8 -*- 

from hamming import Frame , Hamming


paridades = {"par":"pair","impar":"odd"}
opcoes = ["Enviar frame","Receber Frame"]

def menu():
	for index , value in enumerate(opcoes,start=1):
		print("{} - {}".format(index,value))

print("#####################################")
print("Implementação do Algoritmo de Hamming")
print("#####################################")
print("")


continuar = "s"

while continuar == "s":

	menu()
	print("")
	escolhido = int(input("O que deseja fazer: "))
	print("")

	
	while True:
		try:

			valor_paridade = str(input("Valor da paridade: par ou impar : "))
			paridade = paridades.get(valor_paridade,None)
			hamming = Hamming(paridade)
			break

		except ValueError:
			print("Digite um valor de paridade válido ")
			
	if escolhido == 1:

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

					print("O conteúdo do frame enviado é : {}".format(frame_encoded))
					break

				except ValueError:

					print("Digite uma posição válida: ")									
		else:

			print("O conteúdo do frame enviado é : {}".format(frame_encoded))

	elif escolhido == 2:

		conteudo = str(input("Digite o conteúdo do frame: "))

		frame = Frame(conteudo)

		while not frame.is_valid():
			conteudo = str(input("Digite o conteúdo do frame: "))
			frame = Frame(conteudo)
			

		verificar_validade = str(input("Deseja verificar se o frame está correto ? s / n: "))

		validade = hamming.check(frame)

		if validade:

			print("O frame {} está correto.".format(frame))

		else:

			posicao_errada = hamming.wrong_position(frame)

			print("O frame {} , está incorreto , e o bit errado é o : {}".format(frame,posicao_errada))

			consertar = str(input("Deseja consertar o frame? s / n : "))

			if consertar == "s":

				fix_frame = hamming.fix(frame)

				print("O frame errado {} , foi consertado : {}".format(frame,fix_frame))

	continuar = str(input("Deseja continuar ? s / n : "))