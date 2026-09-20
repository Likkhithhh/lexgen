# LexGen — Educational Lexer Generator

[![Python syntax check](https://github.com/Likkhithhh/lexgen/actions/workflows/python-syntax.yml/badge.svg)](https://github.com/Likkhithhh/lexgen/actions/workflows/python-syntax.yml)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Compiler Design](https://img.shields.io/badge/Topic-Compiler%20Design-purple)

LexGen is a Python prototype for exploring how lexical analyzers can be generated from token specifications.

## Why this project matters

Instead of treating tokenization as a black box, this project works through the classic compiler-construction pipeline and generates lexer code from token definitions.

## Pipeline

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
- `lexer_gen/regex_to_nfa.py` — regex-to-NFA logic
- `lexer_gen/nfa_to_dfa.py` — NFA-to-DFA conversion
- `lexer_gen/dfa_minimizer.py` — DFA minimization stage
- `lexer_gen/codegen.py` — Python lexer code generation
- `lexer_gen/lexer_gen.py` — pipeline entry point
- `output_lexer.py` — generated/example lexer output
- `lexer_gen/test_lexer.py` — interactive test utility

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

## Run

From the repository root:

```bash
python3 lexer_gen/lexer_gen.py
```

Then test the generated lexer:

```bash
python3 lexer_gen/test_lexer.py
```

## Learning focus

- Regular expressions
- Finite automata
- NFA → DFA conversion
- DFA minimization
- Code generation
- Compiler front-end fundamentals

## Status / roadmap

This is an educational compiler-construction prototype. Next improvements are broader regex support, stronger DFA minimization, deterministic automated tests, and clearer diagnostics for invalid token specifications.


---

## Portfolio navigation

Explore the rest of my GitHub portfolio:

- [QOS-VIDEO](https://github.com/Likkhithhh/QOS-VIDEO) — machine-learning experiments for video-streaming QoS optimization
- [weatherAPP](https://github.com/Likkhithhh/weatherAPP) — browser weather dashboard using public APIs
- [pingSim](https://github.com/Likkhithhh/pingSim) — Python networking and latency simulator
- [lexgen](https://github.com/Likkhithhh/lexgen) — educational lexer-generator and compiler-design project
- [ATTENDENCEBOT](https://github.com/Likkhithhh/ATTENDENCEBOT) — face-recognition reference work for an attendance-system portfolio project
- **READS — North Karnataka Student Dropout Risk System** — Python/AI/ML internship project at Rural Education and Action Development Society (READS), 03 Aug–03 Sep 2026; focused on student-attribute analysis, preprocessing, dropout-risk prediction, model evaluation, and results

**GitHub:** [Likkhithhh](https://github.com/Likkhithhh)
