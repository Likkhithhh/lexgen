# LexGen — Educational Lexer Generator

LexGen is a Python prototype for exploring how lexical analyzers can be generated from token specifications.

It models a classic compiler-design pipeline:

```text
Token regex specifications
        ↓
Regular expression → NFA
        ↓
NFA → DFA
        ↓
DFA minimization
        ↓
Python lexer code generation
```

## Repository structure

- `token_spec.txt` — example token definitions
- `lexer_gen/regex_to_nfa.py` — regular-expression to NFA logic
- `lexer_gen/nfa_to_dfa.py` — NFA to DFA conversion
- `lexer_gen/dfa_minimizer.py` — DFA minimization stage
- `lexer_gen/codegen.py` — Python lexer code generation
- `lexer_gen/lexer_gen.py` — pipeline entry point
- `output_lexer.py` — generated/example lexer output
- `lexer_gen/test_lexer.py` — interactive lexer test utility

## Example token specification

```text
ID=[a-zA-Z_][a-zA-Z0-9_]*
NUMBER=[0-9]+
PLUS=\+
MINUS=\-
EQUAL==
LPAREN=\(
RPAREN=\)
WS=[ \t\n]+
```

## Run the generator

From the repository root:

```bash
python3 lexer_gen/lexer_gen.py
```

## Status

This repository is an educational compiler-construction prototype. Some regular-expression cases and DFA-minimization behavior may still require refinement before production use.
