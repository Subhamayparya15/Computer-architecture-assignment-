address_field = 200
R1 = 40

memory = {
    200: 500,
    240: 900
}

print("a) Immediate Addressing")
print("Rule: Operand is given directly")
print("Operand value =", 25)

print("\nb) Direct Addressing")
print("Rule: EA = Address field")
print("Effective Address =", address_field)
print("Operand value =", memory[address_field])

print("\nc) Indirect Addressing")
print("Rule: EA = Memory[Address field]")
ea = memory[address_field]
print("Effective Address =", ea)

if ea in memory:
    print("Operand value =", memory[ea])
else:
    print("Operand value cannot be determined")
    print("Memory[500] is not provided")

print("\nd) Indexed Addressing")
print("Rule: EA = Address field + R1")
ea = address_field + R1
print("Effective Address =", ea)
print("Operand value =", memory[ea])
