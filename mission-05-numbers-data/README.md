# Mission 5 — Numbers and data

## 1. Task / objective
Convert decimal, binary and hexadecimal numbers, verify conversions with Python, build a converter, and explain text encoding.

## 2. Work completed
### Task 5.1 — Manual conversions
| Question | Working and answer |
|---|---|
| Decimal 13 to binary | 13 = 8 + 4 + 1, so the bits for 8, 4, 2, 1 are 1, 1, 0, 1. Answer: `1101`. |
| Decimal 25 to binary | 25 = 16 + 8 + 1. Answer: `11001`. |
| Binary `1010` to decimal | 1×8 + 0×4 + 1×2 + 0×1 = 10. |
| Binary `1101` to decimal | 1×8 + 1×4 + 0×2 + 1×1 = 13. |
| Hexadecimal `A` to decimal | A represents 10. Answer: 10. |
| Hexadecimal `1F` to decimal | 1×16 + 15 = 31. |
| Binary `1111` to hexadecimal | `1111` is decimal 15; hexadecimal digit F represents 15. Answer: `F`. |

### Task 5.2 — Python verification
Use Python's built-in functions to verify the results:

```python
bin(13)       # '0b1101'
bin(25)       # '0b11001'
int('1010', 2)  # 10
int('1101', 2)  # 13
hex(10)       # '0xa'
int('1F', 16)  # 31
hex(int('1111', 2))  # '0xf'
```

Record your actual tests and results: [FILL IN if your instructor expects a separate observation log.]

### Task 5.3 — Number converter
The `number_converter.py` file in this folder asks for a positive whole number and prints its binary and hexadecimal forms.

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| 13 | `1101` (Python display: `0b1101`) | `d` (Python display: `0xd`) |
| 25 | `11001` (Python display: `0b11001`) | `19` (Python display: `0x19`) |
| 31 | `11111` (Python display: `0b11111`) | `1f` (Python display: `0x1f`) |

Run it using:

```bash
python3 number_converter.py
```

`bin()` converts an integer to a binary string with a `0b` prefix. `hex()` converts an integer to a hexadecimal string with a `0x` prefix.

### Task 5.4 — Text encoding
- Uppercase `A` has ASCII decimal code **65**.
- Lowercase `a` has ASCII decimal code **97**.
- An encoding standard gives computers a consistent way to represent characters as numbers/bytes, so text can be stored and exchanged correctly.
- Example of a character outside basic ASCII: `₹` or `é`.

## 3. Commands / tools used
- Python built-ins: `bin()`, `hex()`, `int()`, `input()`, `print()`.
- `python3 number_converter.py` runs the converter.
- [FILL IN: Record the actual tests you ran.]

## 4. My understanding
Binary uses base 2, decimal uses base 10 and hexadecimal uses base 16. Python's conversion functions make it easy to check manual calculations. Character encodings map text characters to numeric representations.

## 5. Difficulties faced
[FILL IN actual difficulty or “No major difficulties”.]

## 6. How I resolved them
[FILL IN actual steps or “Not applicable”.]

## 7. Evidence / files
- `number_converter.py`
- This README
- [FILL IN: Any screenshot or output evidence.]

## 8. Commit details
[FILL IN actual commit message and verify the push.]
