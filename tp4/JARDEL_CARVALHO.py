class Infinito:
	def __str__(self):
		return 'O'
	pass

def pertence(p, A, B, ponto):
	x, y = ponto
	return (y ** 2) % p == ((x ** 3) + A * x + B) % p	

def soma(p, A, B, P, Q):
	if type(P) == Infinito:
		return Q
	if type(Q) == Infinito:
		return P
	
	if not pertence(p, A, B, P):
		print('\nO ponto ', P, ' não pertence à curva', sep='')
		return None
	if not pertence(p, A, B, Q):
		print('\nO ponto', Q, ' não pertence à curva', sep='')
		return None

	xp, yp = P
	xq, yq = Q
	if xp == xq and yp == -yq % p:
		return Infinito()

	if P != Q:
		m = ((yp - yq) % p) / ((xp - xq) % p)
	else:
		m = (3 * (xp ** 2) + A) / 2 * yp % p

	xr_ = (m ** 2 - xp - xq) % p
	yr_ = (-yp - m * (xr_ - xp)) % p

	R_ = (xr_, yr_)
	return R_
	
if __name__ == '__main__':
	p = 7
	A, B = 3, 4
	
	#Soma: (1, 1) + (5, 2) = (5, 5)
	P = (1, 1)
	Q = (5, 2)
	R_ = soma(7, A, B, P, Q)
	print(P, '+', Q, '=', R_, '\n')

	#Soma: (1, 1) + (1, 1) = (0, 2)
	P = (1, 1)
	Q = (1, 1)
	R_ = soma(7, A, B, P, Q)
	print(P, '+', Q, '=', R_, '\n')

	#Soma: O + (5, 2) = (5, 2)
	P = Infinito()
	Q = (5, 2)
	R_ = soma(7, A, B, P, Q)
	print(P, '+', Q, '=', R_, '\n')

	#Soma: (1, 1) + O = (1, 1)	
	P = (1, 1)
	Q = Infinito()
	R_ = soma(7, A, B, P, Q)
	print(P, '+', Q, '=', R_, '\n')

	#Soma: (1, 1) + (1, 6) = O
	P = (1, 1)
	Q = (1, 6)
	R_ = soma(7, A, B, P, Q)
	print(P, '+', Q, '=', R_, '\n')

	#(1, 2) não pertence à curva
	P = (1, 2)
	Q = (6, 0)
	R_ = soma(7, A, B, P, Q)
	print(P, '+', Q, '=', R_, '\n')
	

	
