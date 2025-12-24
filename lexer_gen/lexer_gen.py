# lexer_gen.py

from regex_to_nfa import build_nfa_from_token_specs
from nfa_to_dfa import convert_nfa_to_dfa
from dfa_minimizer import minimize_dfa  # optional
from codegen import generate_lexer_code

def main():
    print("Building NFA...")
    nfa = build_nfa_from_token_specs("token_spec.txt")

    print("Converting NFA to DFA...")
    dfa_start = convert_nfa_to_dfa(nfa)

    print("Minimizing DFA (optional)...")
    dfa_start = minimize_dfa(dfa_start)

    print("Generating Lexer Code...")
    generate_lexer_code(dfa_start)

    print("Lexer generated: output_lexer.py")

if __name__ == "__main__":
    main()
