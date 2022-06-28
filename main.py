from arithmetic_arranger import arithmetic_arranger
from unittest import main

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

# Run tests
main(module='test_module', exit=False)