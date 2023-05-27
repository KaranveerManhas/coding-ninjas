""" 
Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
Example:
If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".

The string is compressed only when the repeated character count is more than 1.
Note:
Consecutive count of every character in the input string is less than or equal to 9. 
You are not required to print anything. It has already been taken care of. Just implement the given function and return the compressed string.
Input Format:
The first and only line of input contains a string without any leading and trailing spaces.
Output Format:
The output contains the string after compression printed in single line
Constraints:
0 <= N <= 10^6

Where 'N' is the length of the input string.

Time Limit: 1 sec
Sample Input 1:
aaabbccdsa
Sample Output 1:
a3b2c2dsa
Explanation for Sample Output 1:
In the given string 'a' is repeated 3 times, 'b' is repeated 2 times, 'c' is repeated 2 times and 'd', 's' and 'a' and occuring 1 time hence no compression for last 3 characters.
Sample Input 2:
aaabbcddeeeee
Sample Output 2:
a3b2cd2e5
Explanation for Sample Output 2:
In the given string 'a' is repeated 3 times, 'b' is repeated 2 times, 'c' is occuring single time, 'd' is repeating 2 times and 'e' is repeating 5times.

"""
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def getCompressedString(string) :
	# Write your code here.
	string2=""
	n=len(string)
	count=1
	for i in range(1, n):
		if string[i-1]==string[i]:
			count+=1
		else:
			string2+=string[i-1]
			if count>1:
				string2+=str(count)
			count=1
	string2+=string[-1]
	if count>1:
		string2+=str(count)
	return string2


# Main.
string = stdin.readline().strip()
ans = getCompressedString(string)
print(ans)