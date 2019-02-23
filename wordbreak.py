t = int(input())

n = input()	

dictionary = input().split(' ')

string = input()

memo = [-1 for x in range(len(string)+1)]

def dp(i, f):
	if i > len(string): # se o índice inicial é maior que o tamanho da string
		return 0 # não há mais palavras para se formar (acabou o problema)
	
	if f > len(string): # se o índice final é maior que o tamanho da string
		return dp(i+1, i+2) # recomeça a procurar, dessa vez com i = i+1

	if memo[i] != -1: # se já temos uma solução para esse subproblema
		return memo[i]# retornamos essa solução

	if string[i:f] not in dictionary: # se o subproblema não está no dicionário
		return dp(i, f+1) # incrementamos o índice inicial em 1
	
	# se o subproblema está no dicionário, então precisamos decidir entre:
	# pegá-lo e continuar verificando o restante da string;
	# ou ignorá-lo e incrementar o índice final, procurando uma palavra maior
	# nesse caso, escolhemos o que retorna uma maior sequência de palavras 
	# presentes dicionário separada por espaços maior (sub-problema ótimo)
	# salvamos em memo para reutilização e retornamos
	memo[i] = max(len(string[i:f]) + dp(f, f+1), dp(i, f+1)) 
	return memo[i]

def can_break(lenght):
	# a string poderá ser quebrada se for do mesmo tamanho que o retorno de dp
	if lenght == len(string):
		return 1

	return 0

print(can_break(dp(0,0)))
t -= 1

while t > 0:
	n = input()

	dictionary = input().split(' ')

	string = input()

	memo = [-1 for x in range(len(string)+1)]

	print(can_break(dp(0,0)))

	t -= 1
