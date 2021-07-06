def reverse():
    word=input("Word: ")
    index=len(word)-1;
    reversedWord=[];
    while index>0:
        reversedWord.append(word[index]);
        index-=1;
    reversedWord.append(word[0]);
    polished="".join(reversedWord);
    print (polished);
