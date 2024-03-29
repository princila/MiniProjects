with open('story.txt',"r" ) as f:
    story = f.read()

words = set()
#words =[]
target_start_word = "<"
target_end_word = ">"
start_index = -1

for char, item in enumerate(story):
    if item == target_start_word:
        start_index = char

    if item == target_end_word and start_index != -1:
        word = story[start_index:char+1]
        words.add(word)

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ":")
    answers[word] = answer

for key, value in answers.items():
    story = story.replace(key, value)


print(story)
