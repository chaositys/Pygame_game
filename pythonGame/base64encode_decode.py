import base64

def encode(number):
    encoded_bytes = base64.b64encode(number.to_bytes((number.bit_length() + 7) // 8, byteorder='big'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def decode(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
    decoded_number = int.from_bytes(decoded_bytes, byteorder='big')
    return decoded_number
