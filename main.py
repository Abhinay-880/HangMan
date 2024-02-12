#HANGMAN
import random
print("""
H   H  AAAAA  N   N  GGGG   M   M  AAAAA  N   N
H   H  A   A  NN  N  G      MM MM  A   A  NN  N
HHHHH  AAAAA  N N N  G  GG  M M M  AAAAA  N N N
H   H  A   A  N  NN  G   G  M   M  A   A  N  NN
H   H  A   A  N   N  GGGG   M   M  A   A  N   N
""")
hangman = ["""
     ------
     |    |
     |    O
     |   /|\
     |   / \
     |
    ---
    ""","""
     ------
     |    |
     |    O
     |   /|\
     |   / 
     |
    ---
    """, """
     ------
     |    |
     |    O
     |   /|\
     |
     |
    ---
    ""","""
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---
    ""","""
     ------
     |    |
     |    O
     |    |
     |
     |
    ---
    ""","""
     ------
     |    |
     |    O
     |
     |
     |
    ---
    ""","""
     ------
     |    |
     |
     |
     |
     |
    ---
    """]
hang=len(hangman)
word = ["ant", "bear", "cat", "dog", "elephant", "flamingo", "giraffe", "hedgehog", "iguana", "jaguar", "koala", "lion", "monkey", "narwhal", "owl", "penguin", "quokka", "rabbit", "snake", "tiger", "unicorn", "vulture", "whale", "x-ray tetra", "yeti", "zebra"]
a=random.choice(word)
c=len(a)
on=[]
lives=6
for i in range(c):
        on+='_'
print(on)
end=False
while not end:
    b=input('guess a letter ')
    guess=b.lower()
    for i in range(c):
        if a[i]==guess:
            print('YOUR GUESS IS CORRECT')
            on[i]=guess
    print(on)
    if guess not in on:
        lives-=1
        print(f"you guessed letter {guess},that's not in the word.you lose one life")
        print(hangman[lives])
        if lives==0:
            end=True
            print('YOU LOSE')
            print('the word is ',a)
    if '_' not in on:
        print("""
Y   Y   OOO   U    U   W       W III  N   N
 Y Y   O   O  U    U   W       W  I   NN  N
  Y    O   O  U    U   W   W   W  I   N N N
  Y    O   O  U    U   W W   W W  I   N  NN
  Y     OOO    UUUU    W       W III  N   N
""")

end=True
