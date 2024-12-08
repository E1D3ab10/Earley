from sources.Rule import Rule


class Situation:
    def __init__(self, rule: Rule, pos: int):
        self.rule = rule
        self.pos = pos

    def __eq__(self, other):
        return self.rule == other.rule and self.pos == other.pos

    def __hash__(self):
        return hash((self.rule.start, self.rule.end, self.pos))
