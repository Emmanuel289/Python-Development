# Conditional expressions, aka ternary
def quiz_message(grade):
    if grade < 50:
        outcome = 'failed'
    else:
        outcome = 'passed'

    print('You', outcome, 'the quiz with a grade of', grade)


# test
quiz_message(48)

quiz_message(89)


# Single-line conditional expression syntax

def quiz_message2(grade):
    outcome = 'failed' if grade < 50 else 'passed'
    print('You', outcome, 'the quiz with a grade of', grade)


quiz_message2(48)

quiz_message2(89)
