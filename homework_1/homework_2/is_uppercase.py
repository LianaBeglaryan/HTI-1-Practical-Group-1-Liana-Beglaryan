w = input('tpel text kam bar:')
def is_uppercase(word):
    word_copy=word[:]
    word_1=word_copy.upper()
    if word_1 == word:
       return word_1
    else:
        print('No')  
   
if is_uppercase(w):
   print('Yes')