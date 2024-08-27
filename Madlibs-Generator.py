
with open("story.txt","r") as f:
    story = f.read()

words = set()   # because it will only contain unique elements in it
start_of_word = -1
target_start = "<"
target_end = ">"


for index, char in enumerate(story):
    if ( char == target_start ):
        start_of_word = index

    if ( char == target_end and start_of_word != -1 ):
        word = story [ start_of_word : index + 1 ]
        words.add(word)
        start_of_word = -1


answers = {}       # We are creating empty dictionary

for i in words:
    user = input( f"Enter a word for {i} : " )
    answers[i] = user

for i in words:
    story = story.replace( i , answers[i] )

print(story)