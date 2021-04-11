'''Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC

Sample Output
2'''






def count_substring(string, sub_string):
    c = 0
    for i in range(len(sub_string), (len(string)+1)):
        for j in range(0, (len(string)-len(sub_string)+1)):
            if (string[j:i] == sub_string):
                c +=1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
