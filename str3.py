'''
Read a string from user and display
number of vowels present in it'''
st = input("enter a string:")
vowels = "aeiou"
count=0
for ch in st:
    if ch in vowels:
        count+=1
print(f"Total no. of vowels in given string {count}")


