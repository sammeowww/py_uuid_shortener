import uuid
import string

class UUIDShortener:
    alphabet = string.digits + string.ascii_letters

    @staticmethod
    def encode(uuid_str):
        num = int(uuid_str.replace('-', ''), 16)
        return UUIDShortener._base62_encode(num)

    @staticmethod
    def decode(short_str):
        num = UUIDShortener._base62_decode(short_str)
        uuid_str = format(num, 'x').zfill(32)
        return f'{uuid_str[:8]}-{uuid_str[8:12]}-{uuid_str[12:16]}-{uuid_str[16:20]}-{uuid_str[20:]}'

    @staticmethod
    def _base62_encode(num):
        if num == 0:
            return UUIDShortener.alphabet[0]
        base62 = []
        base = len(UUIDShortener.alphabet)
        while num:
            num, rem = divmod(num, base)
            base62.append(UUIDShortener.alphabet[rem])
        return ''.join(reversed(base62))

    @staticmethod
    def _base62_decode(str):
        base = len(UUIDShortener.alphabet)
        strlen = len(str)
        num = 0
        idx = 0
        for char in str:
            power = (strlen - (idx + 1))
            num += UUIDShortener.alphabet.index(char) * (base ** power)
            idx += 1
        return num

# Example usage
if __name__ == "__main__":
    original_uuid = str(uuid.uuid4())
    print(f"Original UUID: {original_uuid}")

    short_uuid = UUIDShortener.encode(original_uuid)
    print(f"Shortened UUID: {short_uuid}")

    decoded_uuid = UUIDShortener.decode(short_uuid)
    print(f"Decoded UUID: {decoded_uuid}")

