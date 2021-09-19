import re

from Appearence import Appearance


class InvertedIndex:
    def __init__(self, db, letter_case):
        self.index = dict()
        self.db = db
        self.letter_case = letter_case

    def __repr__(self):
        return str(self.index)

    def index_document(self, document):
        clean_text = re.sub(r'[^\w\s]', '', document['text']).replace('\n', ' ')
        if not self.letter_case:
            clean_text = clean_text.lower()
        terms = re.split(' ', clean_text)
        appearances_dict = dict()
        for term in terms:
            term_frequency = appearances_dict[term].frequency if term in appearances_dict else 0
            appearances_dict[term] = Appearance(document['id'], term_frequency + 1, document['name'])
        update_dict = {key: [appearance] if key not in self.index else self.index[key] + [appearance]
                       for (key, appearance) in appearances_dict.items()}
        self.index.update(update_dict)
        self.db.add(document)
        return document

    def lookup_query(self, query):
        return {term: self.index[term] for term in query.split(' ') if term in self.index}

    def create_inverted_index(self, documents):
        id = 0
        for document in documents:
            document = {'id': id, 'name': document, 'text': open(document).read()}
            self.index_document(document)
            id += 1
