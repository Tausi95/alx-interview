# UTF-8 Validation Project

This project validates whether a dataset represents a valid UTF-8 encoding.

## Files
- `0-validate_utf8.py`: Contains the function `validUTF8(data)` for UTF-8 validation.

## Usage
Run `0-validate_utf8.py` to check for UTF-8 encoding compliance.

## Examples
```python
validUTF8([65])  # Should return True
validUTF8([229, 65, 127, 256])  # Should return False

