import random as r
print('''Rules are simple :-
        On every wrong guess the hang stages will increase if you guess is right then hange man stage will not increase.
        ''')
st = "abcdefghijklmnopqrstuvwxyz"
n = int(input("Enter the length of the word. :- "))

word_ls = r.choices(st,weights=None,k=n)
c_wordst = ""
for i in range(n):
    c_wordst += str(word_ls[i])

ms_wordls = r.sample(c_wordst, k = n)
miss_words = ""

for i in range(len(ms_wordls)):
    miss_words += c_wordst.replace(ms_wordls[i],"_")

miss_wordsstr = ""
for i in range(len(ms_wordls)):
    miss_wordsstr += str(ms_wordls[i])

# print(miss_wordsstr)
print("Word is:-- ",miss_words)

max_limit = 1
count = 7
win=0
while count > max_limit and win!=n:
    user = input('''Enter the word you guess which can fill in the empty space.--> ''')
    print()
    if user in miss_wordsstr:
        win+=1
        print('''Your guess is right.
        ''')
    elif user not in miss_wordsstr:
        count -=1
        match count:
            case 6:
                print('''
                 +----+
                 O    |
                      |
                      |
                     ---''')
                print('''Your guess is wrong and remaining chances are :--  ''',count-1) 
            case 5:
                print('''
                 +----+
                 O    |
                 |    |
                      |
                     ---''')
                print('''Your guess is wrong and remaining chances are :--  ''',count-1)
            case 4:
                print('''
                 +----+
                 O    |
                /|    |
                      |
                     ---''')
                print('''Your guess is wrong and remaining chances are :--  ''',count-1)
            case 3:
                print('''
                 +----+
                 O    |
                /|\   |
                      |
                     ---''')
                print('''Your guess is wrong and remaining chances are :--  ''',count-1)
            case 2:
                print('''
                 +----+
                 O    |
                /|\   |
                /     |
                     ---''')
                print('''Your guess is wrong and remaining chances are :--  ''',count-1)
            case 1:
                print('''
                 +----+
                 O    |
                /|\   |
                / \   |
                     ---''')
                print('''Your guess is wrong and remaining chances are :--  ''',count-1)
    else:
        print("Please! Enter a valid word!")
    
if max_limit==count:
    print('''Your chances are over! 
    +----+
    O    |
   /|\   |
   / \   |
        ---
    Sorry! you hanged the man.    ''')
if win==n:
    print('''Congrats!! You won the Game and saved the man :) 
    O    
   /|\   
   / \   
    ''')