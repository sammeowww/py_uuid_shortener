# Python Library: uuid_shortener

A simple utility to shorten UUIDs using base62 encoding.

## Installation

Install using pip:

```bash
pip install uuid_shortener
```

## Usage

```python
from uuid_shortener import UUIDShortener

original_uuid = 'your-uuid-here'
shortened = UUIDShortener.encode(original_uuid)
print(f'Shortened UUID: {shortened}')

restored = UUIDShortener.decode(shortened)
print(f'Restored UUID: {restored}')
```

Replace your-uuid-here with an actual UUID to test.

## Example

```python
a = str(uuid.uuid4())
print(a)
# >> 5798a735-d00f-4c1d-b86b-15603c6fda82

b = UUIDShortener.encode(a)
print(b)
# >> 2Fi5TIkiHjpn5ZkCA9WOky

print(UUIDShortener.decode(b))
# >> 5798a735-d00f-4c1d-b86b-15603c6fda82
```

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.

