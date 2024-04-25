number_template = "The number is {}"
print(number_template.format(42))

a = 5
b = 10
sum_template = "{0} plus {1} is {2}"
print(sum_template.format(a, b, a + b))

debit = 300.00
credit = 450.00
template = "Debit: ${0:.2f}, Credit: ${1:.2f}, Balance: ${2:.2f}"
print(template.format(debit, credit, credit - debit))
