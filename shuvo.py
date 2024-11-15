def remove_vowel(input_string): # this is the remove function which remove the vowel 
    vowel='aeiouAEIOU'# vowel are 
    result ="

for char in input_string:
    is_vowel =False
    for vowel in vowels:
      if char == vowel:
       is_vowel=True
       break
      if not is_vowel:
          result += char #Character Types
    return result # return the  
   
inpurt_str ="shuvo" # inpurt function
print(remove_vowel(inpurt_str)) # print the all vowel which are remove 