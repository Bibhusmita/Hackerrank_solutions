scores = [100, 100, 50, 40, 40, 20, 10]

alice = [5, 25, 50, 120]

r = []


scores = list(set(scores))
scores.sort(reverse=True)
cur = len(scores) - 1

    
for a in alice:
 
    while True:
        if cur < 0:
            r.append(1)
            break
        else:
            cur_score = scores[cur]
            if cur_score == a:
                r.append(cur + 1)
                break
            elif cur_score > a:
                r.append(cur + 2)
               	break
            else:
            	cur -= 1
print(r)