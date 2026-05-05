class string_reverser:
    def reverse_words(input_string):
        words=input_string.split()
        reversed_words=words[::-1]
        return " ".join(reversed_words)
input_string=input()
print(string_reverser.reverse_words(input_string))