class Lexer:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = 0

        self.transition_table = {
            0: {'\\': 1, ')': 2, '=': 3, '-': 4, ']': 5, '(': 6, },
            1: {'\\': 1, },
            2: {},
            3: {},
            4: {},
            5: {']': 5, },
            6: {},
        }
        self.accepting_states = {
            0: 'ID',
            1: 'PLUS',
            2: 'RPAREN',
            3: 'EQUAL',
            4: 'MINUS',
            5: 'ID',
            6: 'LPAREN',
        }

    def tokenize(self, text):
        tokens = []
        pos = 0
        while pos < len(text):
            state = 0
            last_accept = None
            last_pos = pos
            i = pos
            while i < len(text):
                c = text[i]
                if c in self.transition_table[state]:
                    state = self.transition_table[state][c]
                    if state in self.accepting_states:
                        last_accept = state
                        last_pos = i + 1
                    i += 1
                else:
                    break
            if last_accept is not None:
                tok_type = self.accepting_states[last_accept]
                val = text[pos:last_pos]
                if tok_type != 'WHITESPACE':  # skip whitespace
                    tokens.append((tok_type, val))
                pos = last_pos
            else:
                raise SyntaxError(f'Unexpected character: {text[pos]}')
        return tokens
