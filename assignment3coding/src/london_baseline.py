# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

correct = 0
total = 0
with open("birth_dev.tsv", encoding="utf-8") as fin:
    lines = [x.strip().split('\t') for x in fin]
    if len(lines[0]) == 1:
      print('No gold birth places provided; returning (0,0)')
    true_places = [x[1] for x in lines]
    total = len(true_places)
    predicted_places = ["London" for _ in lines]
    correct = len(list(filter(lambda x: x == "London", true_places)))

print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))