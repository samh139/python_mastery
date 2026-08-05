"""
Milestone: m01_collections_mastery
Task: Word Frequency
"""
text = "The quick brown fox jumps over the lazy dog and the lazy cat"

##The Expected Outputpython# {
#     "the": 3,
#     "quick": 1,
#     "brown": 1,
#     "fox": 1,
#     "jumps": 1,
#     "over": 1,
#     "lazy": 2,
#     "dog": 1,
#     "and": 1,
#     "cat": 1
# }

word_count = {}
for word in text.lower().split():
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

print(word_count)

