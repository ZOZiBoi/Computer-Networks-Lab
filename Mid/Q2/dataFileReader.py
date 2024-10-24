import re

def main():
    # Part a
    with open('Data_File.txt', 'r') as file:
        data = file.read()
        print("Contents of Data_File.txt:")
        print(data)

    # Part b
    float_numbers = re.findall(r'\b\d+\.\d+\b', data)
    with open('floating_numbers.txt', 'w') as file:
        for number in float_numbers:
            file.write(number + '\n')
    print("Floating-point numbers written to floating_numbers.txt")

    # Part c
    consonant_words = re.findall(r'\b[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]\w*\b', data)
    with open('consonant_words.txt', 'w') as file:
        for word in consonant_words:
            file.write(word + '\n')
    print("Words starting with a consonant written to consonant_words.txt")

    # Part d
    modified_data = re.sub(r'\b\w*\d\w*\b', 'DIGIT_FOUND', data)
    with open('modified_data.txt', 'w') as file:
        file.write(modified_data)
    print("Modified data written to modified_data.txt")

if __name__ == "__main__":
    main()