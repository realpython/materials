# Relative imports only work inside packages, so this top-level script
# imports the two packages' modules with absolute imports. The relative
# imports live in package1/module1.py and package2/module3.py.
from package1 import module1
from package2 import module3

print("module1.main():")
module1.main()
print("\nmodule3.main():")
module3.main()
