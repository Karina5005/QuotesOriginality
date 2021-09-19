import re

from DataBase import Database
from InvertedIndex import InvertedIndex


def highlight_term(id, term, text, letter_case: bool):
    clean_text = re.sub(r'[^\w\s]', '', text).replace('\n', ' ')
    terms = re.split(' ', clean_text)
    replaced_text = text
    print(letter_case)
    if not letter_case:
        print('here')
        for text_term in terms:
            if text_term.lower() == term.lower():
                replaced_text = replaced_text.replace(text_term, "\033[1;32;40m {term} \033[0;0m".format(term=text_term))
    else:
        replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
    return "---- document {id} ---- \n{replaced}".format(id=id, replaced=replaced_text)


def main():
    documents = input("Enter file names on one lines: ").split(' ')
    letter_case = eval(input('Case sensitive (True/False): '))
    db = Database()
    index = InvertedIndex(db, letter_case)
    index.create_inverted_index(documents)

    search_term = input("Enter term(s) to search: ")
    result = index.lookup_query(search_term)
    if not result:
        print('Nothing found')
        return

    print('Result of search:')
    for term in result.keys():
        for appearance in result[term]:
            document = db.get(appearance.docId)
            print(highlight_term(appearance.name, term, document['text'], letter_case))
        print("----------------------------------------")


if __name__ == '__main__':
    main()
