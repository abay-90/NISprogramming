text_to_split = input("Add a string of text:  ")
splitter = input("Enter a character to split on:  ")

split_result = text_to_split.split(splitter)
print(split_result)

combiner = input("Enter a character to combine on:  ")
combined_results = combiner.join(split_result)

print(combined_results)