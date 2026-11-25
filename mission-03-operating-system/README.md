# Mission 3 — Understand the operating system

## 1. Task / objective
Explore macOS, processes, storage, paths and file permissions, and explain operating-system responsibilities.

## 2. Work completed
### Task 3.1 — System exploration
Run these commands on your own Mac. Do not publish your account name, device name or other identifying output.

| Information       | My Observation                                              |
|-------------------|-------------------------------------------------------------|
| Operating System  | macOS                                                       |
| Current Account   | A user account is logged in.                                |
| Storage           | Checked used and available storage using Terminal.          |
| System Activity   | Several applications and background processes were running. |

Useful commands: `sw_vers`, `df -h /`, `top -l 1 | head -n 12`. Avoid copying private lines from process output.

### Task 3.2 — Processes
A process is an instance of a program that is currently running. A PID (process identifier) is a number the operating system uses to distinguish a running process. Examples that may appear include a web browser and a text editor; record the actual examples you observe.

- What is a process? A running instance of a program.
- What does PID represent? A unique identifier for a process while it is running.
- Two processes I observed: Brave and Finder

### Task 3.3 — Paths and permissions
An absolute path describes a location from the filesystem root. A relative path describes a location in relation to the current directory.

- Absolute path: Shows the complete location of a file.
- Relative path: Shows the location based on the current folder.

- `r` means read, `w` means write, and `x` means execute. For a directory, execute permission allows traversal/access.

Use `ls -l` on a practice file inside the repository and record its permission letters.

### Task 3.4 — Operating-system responsibilities
| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Schedules and manages running programs. | Sharing CPU time between a browser and editor |
| Memory management | Allocates and tracks RAM used by programs. | Giving a browser memory while it runs |
| Device management | Coordinates hardware through drivers and system services. | Managing keyboard input and display output |
| File management | Organises files and directories and controls access. | Saving a document in a folder |
| User interface / shell | Lets users interact with the computer. | macOS desktop or Terminal |
| Security and permissions | Controls access to accounts, files and resources. | Requiring permission to access protected files |

## 3. Commands / tools used
`sw_vers`, `df -h /`, `top`, `head`, `pwd`, `ls -l`, Activity Monitor.
## 4. My understanding
The operating system manages hardware resources and provides common services to applications. Processes are running programs, paths identify file locations, and permissions determine which actions are allowed.

## 5. Difficulties faced
Couldn't understand the difference in absolute and relative paths before but after I learned about them now I know the difference.
