# nfa_to_dfa.py

from collections import deque, defaultdict
from regex_to_nfa import State, NFA

class DFAState:
    def __init__(self, nfa_states):
        self.nfa_states = frozenset(nfa_states)  # NFA states this DFA state represents
        self.transitions = {}  # char -> DFAState
        self.is_accepting = False
        self.token_type = None

def epsilon_closure(states):
    """Return epsilon-closure of a set of NFA states."""
    stack = list(states)
    closure = set(states)

    while stack:
        state = stack.pop()
        for next_state in state.epsilon:
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    return closure

def move(states, symbol):
    """Return set of states reachable from `states` via `symbol`."""
    result = set()
    for state in states:
        if symbol in state.transitions:
            result.update(state.transitions[symbol])
    return result

def get_token_type(states):
    accepting_states = [s for s in states if s.is_accepting]
    if not accepting_states:
        return None
    # Prioritize by first encountered
    accepting_states.sort(key=lambda s: s.token_type)
    return accepting_states[0].token_type

def convert_nfa_to_dfa(nfa):
    dfa_states_map = {}  # frozenset of NFA states -> DFAState
    dfa_start_states = epsilon_closure([nfa.start])
    dfa_start = DFAState(dfa_start_states)
    dfa_states_map[frozenset(dfa_start_states)] = dfa_start

    if any(s.is_accepting for s in dfa_start_states):
        dfa_start.is_accepting = True
        dfa_start.token_type = get_token_type(dfa_start_states)

    queue = deque([dfa_start])
    symbols = set()

    # Collect all possible symbols
    def collect_symbols(state, visited):
        if state in visited:
            return
        visited.add(state)
        symbols.update(state.transitions.keys())
        for next_states in state.transitions.values():
            for next_state in next_states:
                collect_symbols(next_state, visited)
        for eps in state.epsilon:
            collect_symbols(eps, visited)

    collect_symbols(nfa.start, set())

    while queue:
        current_dfa = queue.popleft()

        for symbol in symbols:
            target_nfa_states = epsilon_closure(move(current_dfa.nfa_states, symbol))
            if not target_nfa_states:
                continue
            key = frozenset(target_nfa_states)

            if key not in dfa_states_map:
                new_dfa = DFAState(target_nfa_states)
                if any(s.is_accepting for s in target_nfa_states):
                    new_dfa.is_accepting = True
                    new_dfa.token_type = get_token_type(target_nfa_states)
                dfa_states_map[key] = new_dfa
                queue.append(new_dfa)

            current_dfa.transitions[symbol] = dfa_states_map[key]

    return dfa_start
