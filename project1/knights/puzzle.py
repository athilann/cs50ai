from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(And(And(AKnight, AKnave), AKnight), And(Not(And(AKnave, AKnight)), AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),
    Or(And(And(AKnave, BKnave), AKnight), And(Not(And(AKnave, BKnave)), AKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),
    Or(Or(And(And(AKnave, BKnave), AKnight), And(Not(And(AKnave, BKnave)), AKnave)), Or(
        And(And(AKnight, BKnight), AKnight), And(Not(And(AKnight, BKnight)), AKnave))),
    Or(And(And(BKnight, AKnave), BKnight), And(And(BKnave, AKnight), BKnight))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))),
    Or(And(BKnight, Not(BKnave)), And(BKnave, Not(BKnight))),
    Or(And(CKnight, Not(CKnave)), And(CKnave, Not(CKnight))),
    And(Or(And(AKnight, Not(AKnave)), And(AKnave, Not(AKnight))), AKnight),
    And(Or(And(AKnave, BKnight), And(Not(And(AKnave, BKnight)), BKnave)),
        Or(And(CKnave, BKnight), And(Not(And(CKnave, BKnight)), BKnave))),
    Or(And(AKnight, CKnight), And(AKnave, CKnave)),
    # TODO Not sure if I sould test A for a Knave
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
