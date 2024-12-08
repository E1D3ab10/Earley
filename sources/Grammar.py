from sources.Rule import Rule
from collections import defaultdict


class Grammar:
    def __init__(self):
        self.is_terminal = defaultdict(lambda: False)
        self.rules = defaultdict(set)
        self.start = None

    def addCharacter(self, character: str, is_term: bool):
        self.is_terminal[character] = is_term

    def addRule(self, rule: Rule):
        self.rules[rule.start].add(rule)

    def setStart(self, character: str):
        self.start = character
