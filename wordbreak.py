t = int(input())

n = input()	

dictionary = input().split(' ')

string = input()

memo = [[-1 for x in range(len(string)+1)] for y in range(len(string)+1)] 

def best(s1, s2):
	return s1 if len(s1) > len(s2) else s2

def dp(i, f):
	#print('DP('+ str(i) +', '+ str(f) + '):', 'str: ', string[i:f])
	if i > len(string):
		return 0
	
	if f > len(string):
		return dp(i+1, i+2)

	if memo[i][f] != -1:
		return memo[i][f]

	if string[i : f] not in dictionary:
		return dp(i, f+1)
	
	#print(memo[i][f], 'word found in dict:', string[i:f])

	memo[i][f] = max(len(string[i:f]) + dp(f, f+1), dp(i, f+1))
	return memo[i][f]

def can_break(lenght):
	if lenght == len(string):
		return 1

	return 0

print(can_break(dp(0,0)))
t -= 1

while t > 0:
	n = input()

	dictionary = input().split(' ')

	string = input()

	memo = [[-1 for x in range(len(string)+1)] for y in range(len(string)+1)] 

	print(can_break(dp(0,0)))

	t -= 1
