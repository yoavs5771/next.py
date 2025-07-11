password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
def decode_password(password):
    decoded = []
    for ch in password:
        decoded.append(chr(ord(ch) + 2))
    return ' '.join(decoded)
def decode_password_one_liner(password):
    return ' '.join([chr(ord(ch) + 2) for ch in password])
# Test the functions
print(decode_password(password))
print(decode_password_one_liner(password))


