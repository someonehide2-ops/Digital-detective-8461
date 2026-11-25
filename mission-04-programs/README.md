# Mission 4 — How programs run

## 1. Task / objective
Create and run a simple Python program and compare compilers with interpreters.

## 2. Work completed
Created `hello.py`:

```python
print("Hello from Python")
```

Run it from this folder with:

```bash
python3 hello.py
```

Expected output:

```text
Hello from Python
```

### Task 4.2 — Compiler and interpreter comparison
| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates source code before the resulting program is run. | Executes instructions at runtime, often while reading or processing the program. |
| Typical output | Often produces machine code or another executable form. | Often executes directly or uses an intermediate representation/runtime. |
| One example | A C compiler such as Clang. | A Python interpreter such as CPython. |
| One advantage | The resulting program can run without recompiling the source each time. | Convenient for interactive use and quick testing. |

A compiler generally translates a program before it runs, while an interpreter carries out instructions at runtime. The distinction is not absolute: modern language implementations may combine compilation and interpretation. Python's implementation commonly compiles source to bytecode and then executes that bytecode in its virtual machine.

## 3. Commands / tools used
- `python3 hello.py` runs the Python script.
- Text editor creates and saves `hello.py`.
 
## 4. My understanding
A program is a set of instructions. A compiler and an interpreter are different ways of translating or executing those instructions, and real language implementations can combine approaches.

## 5. Difficulties faced
No major difficulties.
