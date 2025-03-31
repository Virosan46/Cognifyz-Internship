file =open("Peaky blinders.text")
data=file.read()
words = data.split()
count = len(words)

print("No. of words in the text file:", count)
print("Given data is:", data)

# Count occurrences
occurrence = data.count("Peaky Blinders")
print("Number of occurrences of 'Peaky Blinders':", occurrence)

occurrences = data.count("Thomas Shelby")
print("Number of occurrences of 'Thomas Shelby':", occurrences)