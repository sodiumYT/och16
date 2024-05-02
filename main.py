def och16(message):
    bits = bin(int.from_bytes(message.encode('utf-8', 'surrogatepass'), 'big'))[2:]
    ones = bits.zfill(8 * ((len(bits) + 7) // 8)).count('1')
    message_bytes = message.encode('utf-8')
    hash_value = 0
    for char in message_bytes:
        hash_value = hash_value * 31 + char
        hash_value &= 0xFFFFFFFFFFFFFFFF
    return str(ones) + 'x' + format(hash_value, '08x')


print(och64("Hello, World!"))