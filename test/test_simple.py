from DataBase import Database
from InvertedIndex import InvertedIndex
from Appearence import Appearance


def test_simple_case_sensitive():
    db = Database()
    index = InvertedIndex(db, True)
    index.create_inverted_index(['testFiles/test1'])
    assert [Appearance(0, 1, 'testFiles/test1')] == index.lookup_query('good')['good']


def test_empty_case_sensitive():
    db = Database()
    index = InvertedIndex(db, True)
    index.create_inverted_index(['testFiles/test1'])
    assert {} == index.lookup_query('bad')


def test_simple():
    db = Database()
    index = InvertedIndex(db, False)
    index.create_inverted_index(['testFiles/test1'])
    assert [Appearance(0, 1, 'testFiles/test1')] == index.lookup_query('good')['good']


def test_empty():
    db = Database()
    index = InvertedIndex(db, False)
    index.create_inverted_index(['testFiles/test1'])
    assert {} == index.lookup_query('bad')
