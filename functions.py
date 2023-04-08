
# "*" becomes bit value "1" and "-" becomes bit value "0"
def char2bit(line, initial_bit_index, bit_number):
    values = []
    value = 0
    bit_index = initial_bit_index

    for char in line:
        # due to "hardware" bug the 15th bit in every word is forbidden
        if bit_index == 15:
            bit_index = 14

        if char == "*":
            value |= (1 << bit_index)

        if bit_index == 0:
            bit_index = bit_number
            values.append(value)
            value = 0

        bit_index -= 1
    
    if (bit_index != (bit_number - 1)):
        values.append(value)

    return values

# assembly code to write value to memory with specified address
def get_print_instruction(value, address):
    str = f"""A = 0x{value:X}
D = A
A = 0x{address:X}
*A = D
"""
    return str
