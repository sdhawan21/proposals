import matplotlib.pyplot as plt
import numpy as np
def main():
	opt=np.loadtxt('2003hv_opt.dat', dtype='string', delimiter='&')
	print opt[1]
main()
