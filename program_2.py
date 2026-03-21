# Program #2: Word Separator
#3/20/26
#Josiah Hendley
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):

    new_sentence = ""
    #    Add your logic here
    for i, char in enumerate(sentence):
        if i == 0:
            new_sentence += char 
        elif char.isupper():
            new_sentence += " " + char.lower()
        else:
            new_sentence += char

    return new_sentence.strip()

# Example usage
if __name__=="__main__":
    sentence = "StopAndSmellTheRoses"

    new_sentence = word_separator(sentence)

    print(new_sentence)
