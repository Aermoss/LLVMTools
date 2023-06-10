import llvmtools, os, subprocess

for i in os.listdir(f"{os.path.split(__file__)[0]}/bin"):
    fileName = os.path.splitext(i)[0].replace("llvm-", "")
    llvmtools.__all__.append(fileName)
    globals()[fileName] = lambda args: subprocess.Popen([f"{os.path.split(__file__)[0]}/bin/{i}", *args], stdin = subprocess.PIPE, stdout = subprocess.PIPE)