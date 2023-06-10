import llvmtools as llvm

result = llvm.llc(["--help"])
print(result.stdout.read().decode())