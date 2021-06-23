# Question Number 03

def longestSubstrDitinctChars(string):

# 	# last index of every character
	last_idx = {}
	max_len = 0

# 	# starting index of current
# 	# window to calculate max_len
	start_idx = 0

	for i in range(0, len(string)):
	
		if string[i] in last_idx:
			start_idx = max(start_idx, last_idx[string[i]] + 1)

		max_len = max(max_len, i-start_idx + 1)

		last_idx[string[i]] = i

	return max_len


# # Driver program to test the above function
string = "CheetyAssignmentSolution"
print("The input string is " + string)
length = longestSubstrDitinctChars(string)
print("The length of the longest non-repeating character" +
	" substring is " + str(length))

