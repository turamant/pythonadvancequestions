"""В этом примере используется оператор match, который позволяет сопоставлять значение
case с различными шаблонами. Каждый case блок соответствует одному из возможных вариантов.
Если ни один из шаблонов не совпадает, то выполняется последний блок с case _:,
который обрабатывает все остальные случаи.

Такой подход более компактный и читабельный, чем использование множества if-elif-else
операторов, как в предыдущем примере. Он также позволяет легко расширять список возможных
вариантов, не усложняя код.

Таким образом, в Python 3.11 появился встроенный механизм, который позволяет реализовать
поведение, аналогичное switch-case в других языках программирования, используя современный
и выразительный синтаксис."""

def switch_case_example(case):
    match case:
        case "option1":
            print("Option 1 selected")
        case "option2":
            print("Option 2 selected")
        case "option3":
            print("Option 3 selected")
        case _:
            print("Invalid option")

# Usage:
switch_case_example("option2")  # Output: "Option 2 selected"
switch_case_example("option4")  # Output: "Invalid option"
