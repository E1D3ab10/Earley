
from sources.EarlyParser import *
import pytest
small_words = []


@pytest.fixture()
def setup_grammar1():
    start_terminal = "S"
    non_terminals = ["S"]
    terminals = ["a", "b"]
    rules = [("S", "aSbS"), ("S", "")]

    grammar = Grammar()
    grammar.setStart(start_terminal)
    for term in terminals:
        grammar.addCharacter(term, True)
    for non_term in non_terminals:
        grammar.addCharacter(non_term, False)
    for rule in rules:
        grammar.addRule(Rule(rule[0], rule[1]))

    words = ['aababb','aabbba']
    ans = [True, False]
    return grammar, words, ans

@pytest.fixture()
def setup_grammar2():
    start_terminal = "S"
    non_terminals = ["S"]
    terminals = ["a", "b", "c"]
    rules = [("S", "a"), ("S", "b"), ("S", "c")]

    grammar = Grammar()
    grammar.setStart(start_terminal)
    for term in terminals:
        grammar.addCharacter(term, True)
    for non_term in non_terminals:
        grammar.addCharacter(non_term, False)
    for rule in rules:
        grammar.addRule(Rule(rule[0], rule[1]))

    words = ['c', 'b', 'a', 'ccbbbac', 'cabbbb', 'aaca', 'ccaccbc', 'abbcbbb']
    ans = [True, True, True, False, False, False, False, False]
    return grammar, words, ans


@pytest.fixture()
def setup_grammar3():
    start_terminal = "S"
    non_terminals = ["S", "T"]
    terminals = ["a", "b"]
    rules = [("S", "T"), ("S", "bT"), ("T", "aTb"), ("T", "")]

    grammar = Grammar()
    grammar.setStart(start_terminal)
    for term in terminals:
        grammar.addCharacter(term, True)
    for non_term in non_terminals:
        grammar.addCharacter(non_term, False)
    for rule in rules:
        grammar.addRule(Rule(rule[0], rule[1]))

    words = ['bab', 'b', 'baabb', 'aaabbb', '', 'acacaba',
             'cbcaabb', 'bbacbbc', 'aaabcca', 'babaaba']
    ans = [True, True, True, True, True, False, False, False, False, False]

    return grammar, words, ans


@pytest.fixture()
def setup_grammar4():
    start_terminal = "S"
    non_terminals = ["S", "F", "G"]
    terminals = ["a", "b"]
    rules = [("S", "aFbF"), ("F", "aFb"), ("F", ""), ("F", "Ga"), ("G", "bSG")]

    grammar = Grammar()
    grammar.setStart(start_terminal)
    for term in terminals:
        grammar.addCharacter(term, True)
    for non_term in non_terminals:
        grammar.addCharacter(non_term, False)
    for rule in rules:
        grammar.addRule(Rule(rule[0], rule[1]))

    words = ['aaabbb', 'aabb', 'abaabb', 'ab', 'aabbab',
             'bbcbacb', 'bcaacba', 'ccbbaac', 'cababac', 'acabaab']
    ans = [True, True, True, True, True, False, False, False, False, False]

    return grammar, words, ans


@pytest.fixture()
def setup_grammar5():
    start_terminal = "S"
    non_terminals = ["S", "A", "B", "C"]
    terminals = ["a", "b"]
    rules = [("S", "aA"), ("A", "a"), ("B", "b")]

    grammar = Grammar()
    grammar.setStart(start_terminal)
    for term in terminals:
        grammar.addCharacter(term, True)
    for non_term in non_terminals:
        grammar.addCharacter(non_term, False)
    for rule in rules:
        grammar.addRule(Rule(rule[0], rule[1]))

    words = ['aa', 'bbacbab', 'cbbaa', 'aaccab', 'cccbba', 'acabca']
    ans = [True, False, False, False, False, False]

    return grammar, words, ans


@pytest.fixture()
def setup_grammar6():
    start_terminal = "S"
    non_terminals = ["S", "F"]
    terminals = ["a", "b"]
    rules = [("S", "a"), ("S", "aFbF"), ("F", "aFb"), ("F", "")]

    grammar = Grammar()
    grammar.setStart(start_terminal)
    for term in terminals:
        grammar.addCharacter(term, True)
    for non_term in non_terminals:
        grammar.addCharacter(non_term, False)
    for rule in rules:
        grammar.addRule(Rule(rule[0], rule[1]))

    words = ['abaabb', 'ab', 'aabbab', 'a', 'abab',
             'bbaacba', 'ccbcbcc', 'bbaabb', 'accaaca', 'aaca']
    ans = [True, True, True, True, True, False, False, False, False, False]

    return grammar, words, ans


@pytest.fixture()
def setup_grammar7():
    start_terminal = "S"
    non_terminals = ["S", "T"]
    terminals = ["a", "b", "c"]
    rules = [("S", "a"), ("S", "b"), ("S", "c"), ("T", "S")]

    grammar = Grammar()
    grammar.setStart(start_terminal)
    for term in terminals:
        grammar.addCharacter(term, True)
    for non_term in non_terminals:
        grammar.addCharacter(non_term, False)
    for rule in rules:
        grammar.addRule(Rule(rule[0], rule[1]))

    words = ['b', 'a', 'c', 'bcaabcb', 'acbabab',
             'cccabcb', 'acbaccb', 'bccbac']
    ans = [True, True, True, False, False, False, False, False]

    return grammar, words, ans


@pytest.fixture()
def setup_grammar8():
    start_terminal = "S"
    non_terminals = ["S"]
    terminals = ["a", "b"]
    rules = [("S", "SaSb"), ("S", "")]

    grammar = Grammar()
    grammar.setStart(start_terminal)
    for term in terminals:
        grammar.addCharacter(term, True)
    for non_term in non_terminals:
        grammar.addCharacter(non_term, False)
    for rule in rules:
        grammar.addRule(Rule(rule[0], rule[1]))

    words = ['', 'aababb', 'aabbab', 'abaabb', 'abab',
             'abbbbaa', 'cbcaaac', 'bbccacc', 'abaacca', 'bbbabcb']
    ans = [True, True, True, True, True, False, False, False, False, False]

    return grammar, words, ans


def test1(setup_grammar1):
    grammar, words, ans = setup_grammar1

    parser = EarlyParser()
    parser.fit(grammar)

    for test in range(len(words)):
        assert parser.predict(words[test]) == ans[test]

def test2(setup_grammar2):
    grammar, words, ans = setup_grammar2

    parser = EarlyParser()
    parser.fit(grammar)

    for test in range(len(words)):
        assert parser.predict(words[test]) == ans[test]

def test3(setup_grammar3):
    grammar, words, ans = setup_grammar3

    parser = EarlyParser()
    parser.fit(grammar)

    for test in range(len(words)):
        assert parser.predict(words[test]) == ans[test]

def test4(setup_grammar4):
    grammar, words, ans = setup_grammar4

    parser = EarlyParser()
    parser.fit(grammar)

    for test in range(len(words)):
        assert parser.predict(words[test]) == ans[test]

def test5(setup_grammar5):
    grammar, words, ans = setup_grammar5

    parser = EarlyParser()
    parser.fit(grammar)

    for test in range(len(words)):
        assert parser.predict(words[test]) == ans[test]

def test6(setup_grammar6):
    grammar, words, ans = setup_grammar6

    parser = EarlyParser()
    parser.fit(grammar)

    for test in range(len(words)):
        assert parser.predict(words[test]) == ans[test]

def test7(setup_grammar7):
    grammar, words, ans = setup_grammar7

    parser = EarlyParser()
    parser.fit(grammar)

    for test in range(len(words)):
        assert parser.predict(words[test]) == ans[test]

def test8(setup_grammar8):
    grammar, words, ans = setup_grammar8

    parser = EarlyParser()
    parser.fit(grammar)

    for test in range(len(words)):
        assert parser.predict(words[test]) == ans[test]
