import image
import data
import functions


lines = image.get()

DST_FILE_NAME = "display.asm"
dst_file = open(DST_FILE_NAME, "w")
dst_file.write("# Assembler code\n")

dst_file = open(DST_FILE_NAME, "a")

data = data.Address(len(lines[0]), len(lines))
for line in lines:
    values = functions.char2bit(
        line, data.get_initial_bit_index(), data.get_bit_number())
    dst_file.write("# New line\n")
    data.go_to_next_line()
    for value in values:
        dst_file.write(functions.get_print_instruction(
            value, data.get_current_address()))

dst_file.close()
