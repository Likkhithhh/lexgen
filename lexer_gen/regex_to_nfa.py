# regex_to_nfa.py

class State:
    def __init__(self):
        self.transitions = {}  # char -> list of states
        self.epsilon = []      # epsilon transitions
        self.is_accepting = False
        self.token_type = None

class NFA:
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def add_concat_operator(regex):
    """Insert explicit concatenation operators."""
    result = ""
    for i in range(len(regex)):
        c1 = regex[i]
        result += c1
        if i + 1 < len(regex):
            c2 = regex[i + 1]
            if (c1 not in '(|' and c2 not in '|)*+?)'):
                result += '.'
    return result

def to_postfix(regex):
    output = ''
    stack = []
    precedence = {'*': 3, '.': 2, '|': 1}
    i = 0
    while i < len(regex):
        c = regex[i]
        if c == '\\':  # handle escape character
            if i + 1 < len(regex):
                output += regex[i:i+2]  # include both \ and escaped char
                i += 2
                continue
            else:
                raise ValueError(f"Incomplete escape in regex: {regex}")
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            if not stack:
                raise ValueError(f"Unmatched parentheses in regex: {regex}")
            stack.pop()
        elif c in precedence:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[c]:
                output += stack.pop()
            stack.append(c)
        else:
            output += c
        i += 1

    while stack:
        if stack[-1] == '(':
            raise ValueError(f"Unmatched parentheses in regex: {regex}")
        output += stack.pop()

    return output

def regex_to_nfa(postfix):
    stack = []

    for char in postfix:
        if char == '*':
            nfa1 = stack.pop()
            start = State()
            accept = State()
            start.epsilon.append(nfa1.start)
            start.epsilon.append(accept)
            nfa1.accept.epsilon.append(nfa1.start)
            nfa1.accept.epsilon.append(accept)
            stack.append(NFA(start, accept))
        elif char == '+':
            nfa1 = stack.pop()
            start = State()
            accept = State()
            start.epsilon.append(nfa1.start)
            nfa1.accept.epsilon.append(nfa1.start)
            nfa1.accept.epsilon.append(accept)
            stack.append(NFA(start, accept))
        elif char == '?':
            nfa1 = stack.pop()
            start = State()
            accept = State()
            start.epsilon.append(nfa1.start)
            start.epsilon.append(accept)
            nfa1.accept.epsilon.append(accept)
            stack.append(NFA(start, accept))
        elif char == '.':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.accept.epsilon.append(nfa2.start)
            stack.append(NFA(nfa1.start, nfa2.accept))
        elif char == '|':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            start = State()
            accept = State()
            start.epsilon.extend([nfa1.start, nfa2.start])
            nfa1.accept.epsilon.append(accept)
            nfa2.accept.epsilon.append(accept)
            stack.append(NFA(start, accept))
        else:
            start = State()
            accept = State()
            start.transitions[char] = [accept]
            stack.append(NFA(start, accept))

    return stack.pop()

def build_nfa_from_token_specs(filename):
    with open(filename) as f:
        lines = f.readlines()

    master_start = State()
    for line in lines:
        if not line.strip():
            continue
        token_name, pattern = line.strip().split("=", 1)
        postfix = to_postfix(pattern)
        nfa = regex_to_nfa(postfix)
        nfa.accept.is_accepting = True
        nfa.accept.token_type = token_name
        master_start.epsilon.append(nfa.start)

    return NFA(master_start, None)
