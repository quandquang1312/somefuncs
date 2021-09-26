eps = 0.001

def sqrt(num, hs, s):
	if (hs**2 > (num-eps) and hs**2 < (num+eps)):
		return hs

	if (hs**2 < (num-eps)):
		return sqrt(num, (hs+s)/2, s)
	if (hs**2 > (num+eps)):
		return sqrt(num, hs/2, hs)

