BinaryStr = input("Enter the binary string please :")
StringLength = len(BinaryString)
DenaryValue = 0
BinaryString = BinaryStr[::-1]
for i in range (StringLength):
    Bit = BinaryString[i]
    BitValue = int(Bit) * (2**i)
    DenaryValue += BitValue
print(DenaryValue)
