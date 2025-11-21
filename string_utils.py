def reverse_string(s: str):
    return s[::-1]

def count_words(sentence: str):
    return len(sentence.split())

def is_palindrome(text: str):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
