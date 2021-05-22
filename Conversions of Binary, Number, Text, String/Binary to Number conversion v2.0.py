BinaryString = input("Enter the Binary String please")
StringLength = len(BinaryString)
DenaryValue = 0
for i in range(StringLength):
    Bit = BinaryString[i]
    BitValue = int(Bit)
    DenaryValue = DenaryValue * 2 + BitValue
print(DenaryValue)
