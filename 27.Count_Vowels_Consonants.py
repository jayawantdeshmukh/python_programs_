a=input("enter a string:")
vowels= " aeiouAIEOU"
vowel_count=0
consonant_count=0
for char in a:
    if char.isalpha():
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
print(f"vowels: {vowel_count}")
print(f"consonant: {consonant_count}")