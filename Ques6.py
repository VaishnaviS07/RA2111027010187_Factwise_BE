ones = [0,3,3,5,4,4,3,5,5,4]     #letters in ones
teens= [3,6,6,8,8,7,7,9,8,8]    #letters in teens
tens = [0,0,6,6,5,5,5,7,6,6]    #letters in tens

hundreds =[0,10,10,12,11,11,10,12,12,11]
def
count_letters_in_numbers_up_to_1000(
):
  total_letters=0;
  letters_used = []
  total_letters +=sum(ones)
  letters_used.extend(ones)
  total_letters +=sum(teens)
  letters_used.extend(teens)
  total_letters +=sum(tens)*10
  letters_used.extend([sum(tens)]*10)
  total_letters +=sum(hundreds)*100
  letters_used.extend([sum(hundreds)]*100)
  total_letters += 3 * 99
  letters_used.extend([3]*99)
  total_letters += 11#for one thousand
  leters_used.append(11)
  
  return total_letters,letters_used #return the total count
  total_letters , letters_used = count_letters_in_numbers_up_to_1000()

  total_letters = count_letters_in_numbers_up_to_1000()
  print("The total number of letters from 1 to 1000 are:", total_letters)

  
