def reverse(word):
    index=len(word)-1;
    reversedWord=[];
    while index>0:
        reversedWord.append(word[index]);
        index-=1;
    reversedWord.append(word[0]);
    return reversedWord;
