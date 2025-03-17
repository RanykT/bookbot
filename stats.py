def get_num_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_counts = {}
    text = text.lower()

    for char in text:
        if char.isalpha() == True:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1 
    
    sorted_items = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    char_counts = dict(sorted_items)

    return char_counts