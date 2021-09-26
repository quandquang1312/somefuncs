class MathFuncs():
	def __init__(self):
		self.eps_sqrt = 0.0000001

	def sqrt(self, num):
		return self.cal_sqrt(num,num/2,num)

	def cal_sqrt(self, num, hs, s):
		if (hs**2 > (num-self.eps_sqrt) and hs**2 < (num+self.eps_sqrt)):
			return hs

		if (hs**2 < (num-self.eps_sqrt)):
			return self.cal_sqrt(num, (hs+s)/2, s)
		if (hs**2 > (num+self.eps_sqrt)):
			return self.cal_sqrt(num, hs/2, hs)
