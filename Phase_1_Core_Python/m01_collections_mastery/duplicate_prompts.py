"""
Milestone: m01_collections_mastery
Task: Duplicate Prompts
"""
raw_prompts = [
    "Write a quicksort algorithm in Python",
    "Explain quantum computing simply",
    "Write a quicksort algorithm in Python",  # Duplicate
    "What is the capital of France?",
    "Explain quantum computing simply",        # Duplicate
    "Write a quicksort algorithm in Python"   # Duplicate
]

# Expected Final Output:
# {
#     "Write a quicksort algorithm in Python": 3,
#     "Explain quantum computing simply": 2
# }

prompts_count = {}
for prompt in raw_prompts:
    if prompt in prompts_count:
        prompts_count[prompt] +=1
    else:
        prompts_count[prompt] =1
        
print(prompts_count)

duplicate_res = {}

for prompt, count in prompts_count.items():
    if count>1:
        duplicate_res[prompt] = count
print(duplicate_res)