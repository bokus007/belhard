print("q")
s = list("python")
i = 0
def q():
	global i
	print(i)
	i +=1
	return i
ss = f"--".join(s)[::-1]
print(s)
print(ss)
print('main1')