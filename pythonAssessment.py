import re

def count_specific_word(text, search_word):
    words = re.findall(r'\b\w+\b', text.lower())
    count = 0

    for word in words:
        if word == search_word.lower():
            count += 1

    return count


def identify_most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    common_word = ""
    highest = 0

    for word in counts:
        if counts[word] > highest:
            highest = counts[word]
            common_word = word

    return common_word


def calculate_average_word_length(text):
    words = re.findall(r'\b\w+\b', text)

    if len(words) == 0:
        return 0

    total = 0

    for word in words:
        total += len(word)

    return total / len(words)


def count_paragraphs(text):
    if text == "":
        return 1

    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


def count_sentences(text):
    if text == "":
        return 1

    return len(re.findall(r'[.!?]', text))


def main():
    with open("news_article.txt", "r", encoding="utf-8") as file:
        article = file.read()

    word = input("Enter a word: ")

    print("Word Count:", count_specific_word(article, word))
    print("Most Common Word:", identify_most_common_word(article))
    print("Average Word Length:", calculate_average_word_length(article))
    print("Paragraph Count:", count_paragraphs(article))
    print("Sentence Count:", count_sentences(article))

    choice = "y"

    while choice.lower() == "y":
        choice = input("Type y to continue: ")

    print("Done")


if __name__ == "__main__":
    main()