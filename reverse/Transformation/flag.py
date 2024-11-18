def reverse_transformation(transformed):
    original = []
    for char in transformed:
        combined_value = ord(char)
        # Extract the high byte (first character)
        high_byte = combined_value >> 8
        # Extract the low byte (second character)
        low_byte = combined_value & 0xFF
        # Convert bytes back to characters
        original.append(chr(high_byte))
        original.append(chr(low_byte))
    return ''.join(original)

# Transformed result
transformed = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽"

# Reverse the transformation
original_flag = reverse_transformation(transformed)
print(f"Original Flag: {original_flag}")
