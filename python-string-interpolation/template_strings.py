from string import Template

template = Template("Hello, $name! Today is $day.")
print(template.substitute(name="John", day="Friday"))

print(Template("$$$amount").substitute(amount="1,000.00"))
print(Template("$greeting, $who!").substitute(greeting="Hello", who="World"))

print(Template("${amount}USD").substitute(amount="100"))
print(Template("$amountUSD").substitute(amount="100"))

greeting = Template("Hello, $name! Today is $day.")
print(greeting.substitute(name="John", day="Friday"))
greeting.template = "Hello, $name! Welcome!"
print(greeting.substitute(name="John"))

numbers = {"one": 1, "two": 2, "three": 3}
print(Template("$one-$two-$three").substitute(**numbers))
