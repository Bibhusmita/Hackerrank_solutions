word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "sventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "thirty"]
h = int(input())
m = int(input())

if m == 0:
 	print(h,"o' clock")
elif m == 1 :
	print(word[m-1]," minute past",word[h-1])
elif 60-m == 1 :
	print(word[60-m-1]," minute to",word[h])
elif m == 15 | m== 30:
	print(word[m-1],"past",word[h-1])

elif m < 30:
	print(word[m-1]," minutes past",word[h-1])
elif 60-m == 15:
	print(word[60-m-1],"to",word[h])

else :
	print(word[60-m-1],"minutes to",word[h])
