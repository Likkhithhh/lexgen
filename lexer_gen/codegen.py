# codegen.py

def generate_lexer_code(start_dfa):
    with open("output_lexer.py", "w") as f:
        f.write("class Lexer:\n")
        f.write("    def __init__(self):\n")
        f.write("        self.reset()\n\n")

        f.write("    def reset(self):\n")
        f.write("        self.state = 0\n\n")

        # DFA transition table
        state_map = {}
        queue = [start_dfa]
        visited = {}
        state_id = 0

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited[current] = state_id
                state_id += 1
                for symbol, target in current.transitions.items():
                    queue.append(target)

        id_to_state = {v: k for k, v in visited.items()}

        # Create transition table
        f.write("        self.transition_table = {\n")
        for sid, state in id_to_state.items():
            line = f"            {sid}: {{"
            for symbol, target in state.transitions.items():
                tid = visited[target]
                line += f"{repr(symbol)}: {tid}, "
            line += "},\n"
            f.write(line)
        f.write("        }\n")

        # Accepting states and token types
        f.write("        self.accepting_states = {\n")
        for sid, state in id_to_state.items():
            if state.is_accepting:
                f.write(f"            {sid}: '{state.token_type}',\n")
        f.write("        }\n\n")

        # Tokenizer method
        f.write("    def tokenize(self, text):\n")
        f.write("        tokens = []\n")
        f.write("        pos = 0\n")
        f.write("        while pos < len(text):\n")
        f.write("            state = 0\n")
        f.write("            last_accept = None\n")
        f.write("            last_pos = pos\n")
        f.write("            i = pos\n")
        f.write("            while i < len(text):\n")
        f.write("                c = text[i]\n")
        f.write("                if c in self.transition_table[state]:\n")
        f.write("                    state = self.transition_table[state][c]\n")
        f.write("                    if state in self.accepting_states:\n")
        f.write("                        last_accept = state\n")
        f.write("                        last_pos = i + 1\n")
        f.write("                    i += 1\n")
        f.write("                else:\n")
        f.write("                    break\n")
        f.write("            if last_accept is not None:\n")
        f.write("                tok_type = self.accepting_states[last_accept]\n")
        f.write("                val = text[pos:last_pos]\n")
        f.write("                if tok_type != 'WHITESPACE':  # skip whitespace\n")
        f.write("                    tokens.append((tok_type, val))\n")
        f.write("                pos = last_pos\n")
        f.write("            else:\n")
        f.write("                raise SyntaxError(f'Unexpected character: {text[pos]}')\n")
        f.write("        return tokens\n")
