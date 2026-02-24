# 🐱 Sensei CLI - Terminal Python Course Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

<p align="center">
  <img src="docs/sensei-cat.png" alt="Sensei Cat" width="200"/>
</p>

<p align="center">
  <b>A modular, terminal-based Python learning engine with a friendly ASCII mascot</b>
</p>

<p align="center">
  <i>"Learn Python with Sensei Cat - your terminal sensei!"</i>
</p>

---

## 📚 Overview

**Sensei CLI** is a comprehensive, terminal-based Python course engine designed to take learners from absolute beginner to Python expert. With its modular architecture, extensible design, and charming ASCII mascot, it provides an engaging and structured learning experience directly in your terminal.

The platform is built to deliver **37 modules** covering the complete Python ecosystem - from basic syntax to advanced topics like concurrency, metaclasses, and design patterns.

---

## ✨ Key Features

| Feature                         | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| 🐱 **Interactive Mascot**       | Sensei Cat reacts to your progress with dynamic expressions |
| 📦 **Modular Architecture**     | Easy to add new topics without modifying core engine        |
| 🎨 **Kanagawa Theme**           | Beautiful, terminal-native color scheme                     |
| 🔄 **Multiple Learning Modes**  | Study, Practice, (future: Hardcore, Zen)                    |
| 📊 **Progress Tracking**        | (Coming soon) Persistent progress across sessions           |
| 🎯 **37 Comprehensive Modules** | Complete Python curriculum from basics to expert            |
| 🚀 **Zero Dependencies**        | Pure Python, standard library only                          |
| 💻 **Cross-Platform**           | Works on Windows, macOS, and Linux                          |

---

## 🎯 Target Audience

- **Absolute Beginners** - No prior programming experience needed
- **Intermediate Developers** - Fill knowledge gaps and master fundamentals
- **Advanced Pythonistas** - Deep dive into internals and expert topics
- **Educators** - Use as teaching tool or curriculum reference
- **Teams** - Standardize Python training across organizations

---

## 📋 Curriculum Overview

### Phase 1: Python Foundations

1. Syntax & Execution Model
2. Variables & Data Types
3. Operators
4. Control Flow
5. Functions
6. Comprehensions & Generators

### Phase 2: Object-Oriented Python

7. Classes & Objects
8. OOP Principles
9. Magic Methods
10. Dataclasses
11. Enums

### Phase 3: Advanced Language Features

12. First-Class Functions
13. Decorators
14. Context Managers
15. Error Handling
16. Modules & Packages

### Phase 4: Python Internals

17. Execution Model
18. Memory Management
19. Data Model Deep Dive
20. Scope & Namespaces

### Phase 5: Concurrency & Parallelism

21. Threading
22. Multiprocessing
23. Async Programming

### Phase 6: Standard Library Mastery

24. File & OS Operations
25. System & CLI Tools
26. Data Handling (JSON, CSV, SQLite)
27. Collections & Utilities
28. Networking
29. Logging & Debugging

### Phase 7: Testing & Tooling

30. Testing (unittest, pytest)
31. Packaging & Distribution
32. Linting & Formatting

### Phase 8: Advanced Topics

33. Type System
34. C Extensions & Performance
35. Embedding & Interfacing
36. Security
37. Design Patterns

### Phase 9: Domain Ecosystems (Reference)

- Backend (Flask, Django, FastAPI)
- AI/ML (NumPy, Pandas, PyTorch)
- DevOps (Docker automation)
- GUI (Tkinter, PyQt)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- A terminal emulator (any modern terminal works)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/sensei-cli.git
cd sensei-cli

# Make the main script executable (Unix/macOS)
chmod +x main.py

# Run Sensei CLI
python main.py
```

### First Steps

1. Launch Sensei CLI
2. Select a module (start with "Python Basics")
3. Choose a topic
4. Pick your mode:
   - **Study Mode**: Learn concepts with examples
   - **Practice Mode**: Test your knowledge with exercises
5. Follow along with Sensei Cat!

---

## 🎮 Learning Modes

### 📖 Study Mode

- Comprehensive theory explanations
- Code examples with syntax highlighting
- Edge cases and common pitfalls
- Advanced notes for deeper understanding
- Sensei Cat in teaching mode `( o.o )`

### ✏️ Practice Mode

- Interactive exercises
- Fill-in-the-blank questions
- Output prediction challenges
- Debugging scenarios
- Real-time feedback and scoring
- Sensei Cat reacts to your answers:
  - Correct: `( ^-^ )`
  - Incorrect: `( -.- )`

### 🔥 Hardcore Mode (Coming Soon)

- Minimal hints
- Strict time limits
- Sharper mascot attitude `( -.^ )`

### 🧘 Zen Mode (Coming Soon)

- Relaxed pacing
- Focus on theory
- Calm mascot demeanor `( ._. )`

---

## 🏗️ Architecture

```
sensei-cli/
│
├── main.py                    # Entry point
│
├── core/
│   ├── engine.py              # Core learning engine
│   ├── ui.py                  # UI rendering
│   ├── mascot.py              # Sensei Cat logic
│   ├── theme.py               # Kanagawa color theme
│   ├── renderer.py            # Layout manager
│   └── scoring.py             # Practice scoring
│
├── modules/                   # Course content
│   ├── python_basics/
│   │   ├── module_config.py
│   │   └── topics/
│   │       ├── variables.py
│   │       ├── datatypes.py
│   │       └── ...
│   └── ...
│
├── data/                      # User data
│   └── progress.json          # (Future)
│
└── docs/                      # Documentation
    └── sensei-cat.png         # Mascot image
```

### Key Design Principles

- **Separation of Concerns**: Engine, UI, and content are decoupled
- **Plugin Architecture**: New topics are self-contained and auto-discovered
- **Theme Abstraction**: No hardcoded colors in business logic
- **Event-Driven Mascot**: Sensei Cat reacts to learning events

---

## 🤖 Sensei Cat - Your Terminal Sensei

Sensei Cat is always by your side, reacting to your learning journey:

```
    /\_/\
   ( o.o )
    > ^ <
```

### Dynamic Expressions

| Situation        | Expression | Emotion       |
| ---------------- | ---------- | ------------- |
| Teaching         | `( o.o )`  | Focused       |
| Thinking         | `( ~.~ )`  | Contemplative |
| Correct Answer   | `( ^-^ )`  | Happy         |
| Incorrect Answer | `( -.- )`  | Disappointed  |
| Advanced Topic   | `( *.* )`  | Impressed     |
| Tricky Question  | `( @.@ )`  | Curious       |
| Bad Code         | `( =.= )`  | Judgmental    |
| Hardcore Mode    | `( -.^ )`  | Serious       |
| Zen Mode         | `( ._. )`  | Peaceful      |

Sensei Cat also blinks naturally every few seconds:

```
( o.o ) → ( -.- ) → ( o.o )
```

---

## 🎨 Kanagawa Theme

The interface uses a beautiful, terminal-friendly color palette inspired by the Kanagawa wave:

```python
COLORS = {
    'background': '\033[48;2;40;44;52m',  # Deep charcoal
    'text': '\033[38;2;220;223;228m',     # Soft white
    'accent_blue': '\033[38;2;97;175;239m',  # Ocean blue
    'accent_gold': '\033[38;2;224;175;104m', # Warm gold
    'accent_red': '\033[38;2;198;120;120m',  # Muted red
    'accent_green': '\033[38;2;152;195;121m', # Spring green
    'accent_purple': '\033[38;2;198;120;221m', # Lavender
}
```

---

## 🔧 Extending the Course

### Adding a New Topic

1. Create a new file in the appropriate module's `topics/` directory:

```python
# modules/python_basics/topics/strings.py

class StringsTopic:
    title = "Strings"

    def run_study_mode(self):
        # Your study content here
        pass

    def run_exercise_mode(self):
        # Your practice exercises here
        pass
```

2. Register it in `module_config.py`:

```python
TOPICS = [
    "variables",
    "datatypes",
    "strings",  # Add your topic
]
```

That's it! The engine automatically discovers and loads your topic.

### Creating a New Module

1. Create a new directory in `modules/`
2. Add `module_config.py` with module metadata
3. Create a `topics/` subdirectory
4. Add topic files following the Topic interface

---

## 📈 Progress Tracking (Coming Soon)

- JSON-based progress persistence
- Unlockable modules based on prerequisites
- Achievement badges
- Learning streaks
- Exportable progress reports

---

## 🛣️ Development Roadmap

### Phase 1: Core Engine (Current)

- [x] System design complete
- [ ] UI system with Kanagawa theme
- [ ] Mascot system with expressions
- [ ] Module loader
- [ ] Topic interface
- [ ] Study/Practice modes
- [ ] Basic navigation

### Phase 2: Python Basics Module

- [ ] Variables
- [ ] Data Types
- [ ] Input/Output
- [ ] Conditionals
- [ ] Loops
- [ ] Functions

### Phase 3: Enhancement Layer

- [ ] Progress persistence
- [ ] Achievement system
- [ ] Unlock logic
- [ ] UI polish

### Phase 4: Full Curriculum

- [ ] Remaining 36 modules
- [ ] Advanced topics
- [ ] Performance optimization

---

## 🤝 Contributing

Contributions are welcome! Whether it's:

- 📝 Writing content for modules
- 🐛 Fixing bugs
- ✨ Adding features
- 📚 Improving documentation
- 🎨 Enhancing the UI
- 🌍 Translating content

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Content Contributors Needed!

We're looking for Python experts to help write topic content. Each topic needs:

- Clear explanations
- Code examples
- Practice exercises
- Common pitfalls
- Advanced notes

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by classical terminal-based learning tools
- Color palette inspired by the Kanagawa wave
- ASCII cat design evolved from internet culture
- Curriculum structure based on Python mastery paths

---

## 📬 Contact & Community

- **Issues**: [GitHub Issues](https://github.com/yourusername/sensei-cli/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/sensei-cli/discussions)
- **Twitter**: [@senseicli](https://twitter.com/senseicli)

---

<p align="center">
  Made with 🐱 and ☕ for the Python community
</p>

<p align="center">
  <i>"The best way to learn is to teach. Sensei Cat is here to guide you."</i>
</p>
