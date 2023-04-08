
class Address:
    def __init__(self, image_width, image_height) -> None:
        self.IMAGE_WIDTH = image_width
        self.IMAGE_HEIGHT = image_height

        self.DISPLAY_WIDTH = 512
        self.DISPLAY_HEIGHT = 256
        self.DISPLAY_MEMORY_BITWISE = 16
        self.NUMBER_OF_EMPTY_PIXELS = (self.DISPLAY_WIDTH - self.IMAGE_WIDTH) // 2

        self.line_number = (self.DISPLAY_HEIGHT - self.IMAGE_HEIGHT) // 2
        self.address = self.calculate_address()

    def get_current_address(self):
        res = self.address
        self.address += 1
        return res

    def get_initial_bit_index(self):
        return self.DISPLAY_MEMORY_BITWISE - 1 - self.NUMBER_OF_EMPTY_PIXELS % self.DISPLAY_MEMORY_BITWISE

    def get_bit_number(self):
        return self.DISPLAY_MEMORY_BITWISE

    def go_to_next_line(self):
        self.line_number += 1
        self.address = self.calculate_address()

    def calculate_address(self):
        DISPLAY_START_ADDRESS = 0x4000
        BYTES_PER_LINE = self.DISPLAY_WIDTH // self.DISPLAY_MEMORY_BITWISE
        LINE_OFFSET = self.NUMBER_OF_EMPTY_PIXELS // self.DISPLAY_MEMORY_BITWISE

        return DISPLAY_START_ADDRESS + BYTES_PER_LINE * self.line_number + LINE_OFFSET
