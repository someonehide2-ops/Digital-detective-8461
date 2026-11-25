# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Practise Terminal navigation and safe file operations, understand flags and pipes, and explain package managers.

## 2. Work completed
### Task 2.1 — Command reference
| Operation | Command | What it does |
|---|---|---|
| Show current location | `pwd` | Shows the current folder |
| List files | `ls` | Shows files and folders |
| Detailed list | `ls -l` | Shows file details |
| Go back one folder | `cd ..` | Moves to the parent folder |
| Create folder | `mkdir practice` | Creates a new folder |
| Create file | `touch notes.txt` | Creates an empty file |
| Copy file | `cp notes.txt copy.txt` | Creates a copy |
| Rename file | `mv copy.txt new-copy.txt` | Changes the file name |
| View file | `cat notes.txt` | Shows the file content |

### Task 2.2 — Safe file changes
Perform these examples only inside your repository's `terminal-practice` folder.

```bash
mkdir -p terminal-practice
cd terminal-practice
printf "First line\n" > practice.txt
printf "Second line\n" >> practice.txt
cat practice.txt
cp practice.txt practice-backup.txt
mv practice-backup.txt renamed-backup.txt
```

- Replacing contents with `>` writes new contents and replaces the previous contents.
- Appending with `>>` adds text at the end and keeps existing contents.
- Copying creates another file; moving changes the file's location or name.
- `pwd` tells me where Terminal is currently working.
- A directory listing helps me see which files and folders are present.

### Task 2.3 — Flags and pipes
Examples to run from the repository:

```bash
ls
ls -lah
ls -l | head
```

`-l` requests a long listing, `-a` includes hidden entries, and `-h` makes file sizes easier for people to read. A pipe (`|`) sends the output from the command on its left as input to the command on its right. In `ls -l | head`, the listing is passed to `head`, which displays only the first few lines.

### Task 2.4 — Package managers
A package manager helps install, update and remove software while managing dependencies. Homebrew is a package manager commonly used on macOS. The assignment says to check it only if already installed; do not install or uninstall anything for this task.

```bash
brew --version
brew list
```

If `brew` is not found, record that Homebrew is not installed and do not install it just for this assignment.

## 3. Commands / tools used
`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `printf`, `head`, `brew --version`, `brew list`. 
## 4. My understanding
Terminal commands perform actions in the current working directory. Flags modify a command's behaviour, and pipes connect commands so one command's output can be processed by another.

## 5. Difficulties faced
I did not face any particular major difficulties.

