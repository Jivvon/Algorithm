from time import time


def timer(func):
		def _timer(*args, **kwargs):
				start = time()
				ret = func(*args, **kwargs)
				print("Args, Returned : {}, {}".format(args, ret))
				print("Duration : {:f} sec".format(time() - start))
				print()
		return _timer
