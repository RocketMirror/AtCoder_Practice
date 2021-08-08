ans = [3,4,5,6,7,8,9,7,6,5,4,3,3]
print(*[ans[i+1] for i in range(len(ans))], sep='\n')