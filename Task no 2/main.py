def findKth( arr, n, k):
	missing = dict()
	count = 0
	for i in range(n):
		missing[arr[i]] = 1
		
	maxm = max(arr)
	minm = min(arr)

	for i in range(minm + 1, maxm):
		if (i not in missing.keys()):
			count += 1

		if (count == k):
			return i
	
	return -1

T1 = list(map(int, input("Type T1 with space: ").split()))
T2 = list(map(int, input("Type T2 with space: ").split()))
newarr = []

for i in range(len(T1)):
	if (T1[i] in newarr):
		n = len(newarr)
		newval = findKth(newarr, n, 1)
		if (newval == -1):
			newval = max(newarr) + 1
		newarr.append(newval)
		if (T2[i] in newarr):
			newarr.append(max(newarr)+1)
		else:
			newarr.append(T2[i])
	elif (T2[i] in newarr):
		n = len(newarr)
		newval = findKth(newarr, n, 1)
		if (newval == -1):
			newval = max(newarr) + 1
		newarr.append(T1[i])
		newarr.append(newval)
	elif (T2[i] == T1[i]):
		newarr.append(T1[i])
		n = len(newarr)
		newval = findKth(newarr, n, 1)
		if (newval == -1):
			newval = max(newarr) + 1
		newarr.append(newval)
	else:
		newarr.append(T1[i])
		newarr.append(T2[i])

newT2 = []
newT1 = []
for i in range(len(newarr)):
	if (i % 2):
		newT2.append(newarr[i])
	else:
		newT1.append(newarr[i])
print("Result:")
print("New T1: "+ str(newT1))
print("New T2: "+ str(newT2))