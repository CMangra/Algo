"""
Aufgabe: TENDS TO APPEAR QUITE OFTEN IN THE EXAMS

Perform the decision tree learning algorithm manually on the following data set or a data set of your
choice, write out intermediate steps and the result.

    sky     air     humid   wind    water   forecast    attack
1   sunny   warm    normal  strong  warm    same        +
2   sunny   warm    high    strong  warm    same        +
3   rainy   cold    high    strong  warm    change      -
4   sunny   warm    high    strong  cool    change      +
5   sunny   warm    normal  weak    warm    same        -


Algorithm 4 Decision tree learning

function DT-LEARNING(examples, attributes, parent examples)
    if empty(examples) then return PLURALITY-VAL(parent examples)
    else if all examples have same classification then return the classification
    else if empty(attributes) then return PLURALITY-VAL(examples)
    else
        A ← argmax
        a∈attributes
        IMPORTANCE(a, examples)
        tree ← a new decision tree with root test A
        for vk ∈ A do
            exs ← {e|e ∈ examples ∧ e.A = vk}
            subtree ← DT-LEARNING(exs, attributes − A, examples)
            add a branch to tree with label (A = vk) and subtree subtree
        end for
        return tree
    end if
end function

"""