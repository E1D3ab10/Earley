from sources.Grammar import *
from sources.Situation import Situation


class EarlyParser:
    _fake_start = '$'

    def __init__(self):
        self.grammar = None
        pass

    def fit(self, grammar: Grammar):
        self.grammar = grammar
        grammar.addCharacter(EarlyParser._fake_start, False)
        grammar.addRule(Rule(EarlyParser._fake_start, grammar.start))
        grammar.setStart(EarlyParser._fake_start)
        return self

    def _calc_situations(self, word) -> set:
        situations = [set()
                      for _ in range(len(word) + 1)]
        start_rule = next(iter(self.grammar.rules[EarlyParser._fake_start]))
        situations[0].add((Situation(start_rule, 0), 0))

        for after in range(len(word) + 1):
            if after != 0:
                for situation, before in situations[after - 1]:
                    if after - 1 < len(word)\
                            and situation.pos < len(situation.rule.end)\
                            and situation.rule.end[situation.pos] == word[after - 1]:
                        situations[after].add((Situation(situation.rule,
                                                            situation.pos + 1), before))

            prev = 0
            while prev != len(situations[after]):
                prev = len(situations[after])

                for situation, before in situations[after].copy():
                    if situation.pos == len(situation.rule.end):
                        for prev_sit, prev_before in situations[before].copy():
                            if prev_sit.pos == len(prev_sit.rule.end) or prev_sit.rule.end[prev_sit.pos] != situation.rule.start:
                                continue

                            next_situation = Situation(
                                prev_sit.rule, prev_sit.pos + 1)
                            situations[after].add(
                                (next_situation, prev_before))

                for situation, before in situations[after].copy():
                    if situation.pos != len(situation.rule.end):
                        for rule in self.grammar.rules[situation.rule.end[situation.pos]]:
                            next_situation = Situation(rule, 0)
                            situations[after].add((next_situation, after))

        return situations

    def predict(self, word: str) -> bool:
        situations = self._calc_situations(word)
        start = next(iter(self.grammar.rules[EarlyParser._fake_start]))
        final = Situation(start, 1)
        ans = False
        return (final, 0) in situations[len(word)]
