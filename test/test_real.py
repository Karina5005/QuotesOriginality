from DataBase import Database
from InvertedIndex import InvertedIndex
from Appearence import Appearance


def test_simple_case_sensitive():
    db = Database()
    index = InvertedIndex(db, True)
    index.create_inverted_index(['testFiles/letter1'])
    assert [Appearance(0, 8, 'testFiles/letter1')] == index.lookup_query('ты')['ты']


def test_empty_case_sensitive():
    db = Database()
    index = InvertedIndex(db, True)
    index.create_inverted_index(['testFiles/letter1'])
    assert {} == index.lookup_query('Чехов')


def test_two_files_case_sensitive():
    db = Database()
    index = InvertedIndex(db, True)
    index.create_inverted_index(['testFiles/letter1', 'testFiles/letter2'])
    assert [Appearance(0, 1, 'testFiles/letter1'), Appearance(1, 1, 'testFiles/letter2')] == index.lookup_query('если')[
        'если']


def test_all_files_case_sensitive():
    db = Database()
    index = InvertedIndex(db, True)
    index.create_inverted_index(
        ['testFiles/letter1', 'testFiles/letter2', 'testFiles/letter3', 'testFiles/letter4', 'testFiles/letter5',
         'testFiles/letter6', 'testFiles/letter7', 'testFiles/letter8', 'testFiles/letter9', 'testFiles/letter10'])
    assert [Appearance(0, 8, 'testFiles/letter1'),
            Appearance(2, 7, 'testFiles/letter3'), Appearance(3, 4, 'testFiles/letter4'),
            Appearance(6, 1, 'testFiles/letter7'),
            Appearance(7, 12, 'testFiles/letter8'), Appearance(8, 1, 'testFiles/letter9'),
            Appearance(9, 2, 'testFiles/letter10')] == index.lookup_query('ты')['ты']


def test_simple():
    db = Database()
    index = InvertedIndex(db, False)
    index.create_inverted_index(['testFiles/letter1'])
    assert [Appearance(0, 13, 'testFiles/letter1')] == index.lookup_query('ты')['ты']


def test_empty():
    db = Database()
    index = InvertedIndex(db, False)
    index.create_inverted_index(['testFiles/letter1'])
    assert {} == index.lookup_query('Чехов')


def test_two_files():
    db = Database()
    index = InvertedIndex(db, False)
    index.create_inverted_index(['testFiles/letter1', 'testFiles/letter2'])
    assert [Appearance(0, 2, 'testFiles/letter1'), Appearance(1, 5, 'testFiles/letter2')] == index.lookup_query('если')[
        'если']


def test_all_files():
    db = Database()
    index = InvertedIndex(db, False)
    index.create_inverted_index(
        ['testFiles/letter1', 'testFiles/letter2', 'testFiles/letter3', 'testFiles/letter4', 'testFiles/letter5',
         'testFiles/letter6', 'testFiles/letter7', 'testFiles/letter8', 'testFiles/letter9', 'testFiles/letter10'])
    assert [Appearance(0, 13, 'testFiles/letter1'), Appearance(1, 1, 'testFiles/letter2'),
            Appearance(2, 7, 'testFiles/letter3'), Appearance(3, 5, 'testFiles/letter4'),
            Appearance(5, 1, 'testFiles/letter6'), Appearance(6, 1, 'testFiles/letter7'),
            Appearance(7, 12, 'testFiles/letter8'), Appearance(8, 2, 'testFiles/letter9'),
            Appearance(9, 3, 'testFiles/letter10')] == index.lookup_query('ты')['ты']
