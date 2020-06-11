s ="aaaa"
n = 4

def substrCount(n, s):
	c = 0
	for i in range(1,n):
		for j in range(n-i+1):
			subs = list(s[j:j+i])
			ss = len(set(subs))
			print(subs)
			if ss == 1:
				c += 1
				print(subs)
			elif ss == 2:
				sn = len(subs)
				if subs[:sn//2] == subs[sn//2+1:]:
					c += 1
	if len(set(s)) == 1 or ((len(set(s))) == 2 and s[:n//2] == s[n//2+1:]):
		c+=1
					
	print(c)     


substrCount(n,s)


