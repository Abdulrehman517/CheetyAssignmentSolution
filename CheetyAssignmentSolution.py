# Question NUmber 01

# n = Total number of activities
# s[]= An array that contains start time of all activities
# f[] = An array that contains finish time of all activities
def ActivitySelection(s , f ):
	n = len(f)
	print ("The following activities are selected")

	# The first activity is always selected
	i = 0
	print (i),

	for j in range(n):
		if s[j] >= f[i]:
			print (j),
			i = j

# Driver program to test above function
s = [1 , 3 , 0 , 5 , 5 , 6]
f = [2 , 4 , 6 , 7 , 9 , 9]
ActivitySelection(s , f)

#   Python program for activity selection problem
# when input activities may not be sorted.
def MaxActivities(arr, n):
	selected = []
	
	Activity.sort(key = lambda x : x[1])
	
	i = 0
	selected.append(arr[i])

	for j in range(1, n):
		
	    if arr[j][0] >= arr[i][1]:
		    selected.append(arr[j])
		    i = j
	return selected


	Activity = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [10, 9]]
	n = len(Activity)
	selected = MaxActivities(Activity, n)
	print("Following activities are selected :")
	print(selected)
