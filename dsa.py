import math
import random
from sympy import isprime

def pointAdd(x1, y1, x2, y2, p):
	s = ((y2-y1)*pow((x2-x1),- 1, p)) % p
	x3 = (s**2 - x1 - x2) % p
	y3 = (s*(x1 - x3) - y1) % p
	return (x3, y3)

def pointDouble(x1, y1, a, p):
	s = ((3*x1**2+a)*pow((2*y1), -1, p)) % p
	x3 = (s**2 - x1 - x1) % p
	y3 = (s*(x1 - x3) - y1) % p
	return (x3, y3)

def pointMult(x1, y1, n, a, p):
	x = x1
	y = y1
	d = list(f'{n:b}')
	for i in range(1, len(d)):
		(x, y) = pointDouble(x,y,a,p)
		if d[i] == 1:
			(x, y) = pointAdd(x,y,x1,y1,p)
	return (x, y)

def main():
	a = 654624412321892857559038596828572669649402987879847772735693306089759
	b = 563386056159714380473737077729260896240517015706612537779563193095411
	p = 1579602854473772853128287506817718026426265023617379175335587248616431
	lower_bound = p + 1 - 2*math.sqrt(p)
	upper_bound = p + 1 + 2*math.sqrt(p)
	print('lower_bound = ', lower_bound)
	print('upper_bound = ', upper_bound)

	x = 953216670857201615849458843136747040308850692140282160349854110301248
	y = 187696769665068572312633292858802066603155820538026405642457554453538
	n = 230768357842901099381188113760304602568543491144769691849643435691536

	(xn, yn) = pointMult(x,y,n,a,p)
	print('Let gn = (xn, yn) then we have')
	print('xn = ', xn)
	print('yn = ', yn)

	p = 113003610536769662365475438074349202902393371149098932488829763899759693942182221311951893491037065838678290591836787867236266829425427477322203921585701270997375076009060429934105831431797790713235693561718253840225010037389994367689434248899226231330475152082648849936270434981210830874017521600353881618277
	q = 1461461359677056032138425664688969714401096527653
	g = 96504423597250666602463350548382591669983630413397284533161601799828504875913402437338367980529992940898864793759282567968196860849581229764805627921115713088555922323634319263032762806965222542087676328725218634401760700374749451348066585982534624077588633442696948741889609514070233035695255374063221721717

	random.seed(101)
	d = random.randrange(1, q)
	B = pow(g, d, p)

	random.seed(47)
	e = random.randrange(1, q)
	e_inv = pow(e, -1, q)
	sha1 = 0x9eee42ec50db4cb95d178bbe88dc3d14b6b531dc
	r = pow(g, e, p)%q
	s = ((sha1+d*r)*e_inv)%q

	w = pow(s, -1, q)
	u1 = (w*sha1)%q
	u2 = (w*r)%q
	v = (pow(g,u1,p)*pow(B,u2,p))%q 

	fd = open('output.txt', 'w+')

	print('p =', p, file=fd)
	print('q =', q, file=fd)
	print('g =', g, file=fd)
	print('x =', d, file=fd)
	print('X =', B, file=fd)
	print('e =', e, file=fd)
	print('r =', r, file=fd)
	print('s =', s, file=fd)
	print('w =', w, file=fd)
	print('u1 =', u1, file=fd)
	print('u2 =', u2, file=fd)
	print('v =', v, file=fd)
	if v%q == r%q:
		print('valid sinature', file=fd)
	else:
		print('invalid signature', file=fd)

	fd.close()

	return

if __name__ == '__main__':
	main()