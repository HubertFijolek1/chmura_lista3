import base64

def encrypt_base64(text):
    message_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def decrypt_base64(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    text = message_bytes.decode('ascii')
    return text

print(encrypt_base64('siemanko'))
print(decrypt_base64('c2llbWFua28='))
