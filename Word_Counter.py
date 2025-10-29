def Word_Count(sentence, N):
    
    #Making all characters in string to lower_case and Storing in a new String.
    Sentence_in_lower = sentence.lower()
    list_of_characters = list(Sentence_in_lower)
    new_char_list = []

    #Removing Punctuations
    for item in list_of_characters:
        if (ord(item)>= 97 and ord(item)<=122) or item == " ":
            new_char_list.append(item)
            
    new_char_list = "".join(new_char_list)

    #Removing Spaces
    final_list_of_words = new_char_list.split(" ")

    #Counting Words
    dict = {}
    for i in final_list_of_words:
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1

    #Filtering Words with Count equal to Given Word_Count
    res_dict = {}
    for item in dict:
        if(dict[item] == N):
            res_dict[item] = dict[item]
    print(res_dict)
    
Sentence = input("Enter the Sentence: ")
number = int(input("Enter the Number count of words: "))
Word_Count(Sentence, number)
            
    


        
        
        

    
        
