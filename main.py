from sources.EarlyParser import *

grammar = Grammar()

non_terms_cnt, terms_cnt, rules_cnt = map(int, input().split())
non_terms = input()
terms = input()

for char in non_terms:
    grammar.addCharacter(char, False)

for char in terms:
    grammar.addCharacter(char, True)

for i in range(rules_cnt):
    rule = Rule(*map(str.strip, input().split("->")))
    grammar.addRule(rule)

start = input().strip()
grammar.setStart(start)

parser = EarlyParser()
parser.fit(grammar)

word_cnt = int(input())
for i in range(word_cnt):
    word = input().strip()
    print("Yes" if parser.predict(word) else "No")
