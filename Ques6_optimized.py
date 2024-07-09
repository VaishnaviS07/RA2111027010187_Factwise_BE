def convert_to_words(num):
    if num == 0:
        return "zero"
    
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    words = ""
    flag = False
    
    if num >= 1000:
        flag = True
        words += ones[num // 1000] + "thousand"
        num %= 1000
        
    if num >= 100:
        flag = True
        words += ones[num // 100] + "hundred"
        num %= 100
        
    if num >= 10 and num <= 19:
        words += teens[num - 10]
        num = 0  # Reset num because we've already handled the tens and ones
    
    elif num >= 20:
        words += tens[num // 10]
        num %= 10
        
    if num >= 1 and num <= 9:
        words += ones[num]
    if flag:
        return len(words.strip()) + 3
    else:
        return len(words.strip())

words=0
for i in range (1,1001):
    words += convert_to_words(i)  
print(words)
