from package1 import module1
from package1.module2 import function1
from package2 import class1
from package2.subpackage1.module5 import function2

# Also import module3 to run the absolute imports inside it
from package2 import module3

print("Absolute imports:")
print(function1())
print(class1())
print(function2())

print("\nmodule1.main():")
module1.main()
print("\nmodule3.main():")
module3.main()
