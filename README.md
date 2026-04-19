# cwstringformatter

A Python utility for amateur-radio operators that formats arbitrary text into
ready-to-paste **CW (Continuous Wave / Morse-code) memory strings** for
transceivers such as the **Kenwood TS-590SG**.

It slices your message into correctly-sized chunks, wraps each chunk in the
appropriate **CAT command** syntax, and places the finished sequence on your
**clipboard** — ready to paste straight into logging software like
[Amateur Contact Log (ACLog) by N3FJP](https://n3fjp.com).

---

## Table of Contents

- [Background](#background)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Configuration](#configuration)
- [License](#license)

---

## Background

Many HF transceivers store CW memory messages as a series of strings that must
not exceed a fixed character limit per memory slot.  For example, the Kenwood
TS-590SG accepts up to **24 characters** per CW memory entry.  Logging
programs such as ACLog can program these memories over a serial CAT link, but
the operator must first split a long message manually and wrap each piece in
the correct command.  `cwstringformatter` automates that tedious process.

---

## Features

- Accepts a CW message string of any reasonable length.
- Automatically slices the message into **24-character chunks** (matching the
  TS-590SG memory slot size).
- Wraps every chunk in the required **CAT command** so it can be sent directly
  to the rig or to compatible logging software.
- Copies the complete, formatted output to the **system clipboard** — no
  manual copy-paste needed.
- Works on any platform where Python and a clipboard library are available
  (Windows, macOS, Linux).

---

## Prerequisites

| Requirement | Version |
|-------------|---------|
| Python      | 3.8 +   |
| `pyperclip` | latest  |

> `pyperclip` is the cross-platform clipboard library used to write the output
> to the system clipboard.  On Linux you also need either `xclip` or `xsel`
> installed (`sudo apt install xclip`).

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/dhilliker/cwstringformatter.git
cd cwstringformatter

# 2. (Recommended) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install the required dependency
pip install pyperclip
```

---

## Usage

### Basic example

```python
from cwstringformatter import format_cw_string

message = "CQ CQ CQ DE W1ABC W1ABC W1ABC K"
result = format_cw_string(message)
print(result)
```

**Output** (each line is a separate CAT command ready to be pasted into ACLog
or sent directly to the rig):

```
EX0740 CQ CQ CQ DE W1ABC  ;
EX0741 W1ABC W1ABC K       ;
```

---

### Running the script directly

```bash
python cwstringformatter.py "CQ CQ CQ DE W1ABC W1ABC W1ABC K"
```

The program prints the formatted CAT command sequence **and** copies it to
your clipboard automatically.

---

### Sending a contest exchange

```python
from cwstringformatter import format_cw_string

exchange = "TU 5NN 001 001 W1ABC W1ABC"
formatted = format_cw_string(exchange)
# Paste `formatted` directly into ACLog's CW memory field
print(formatted)
```

---

## How It Works

1. **Input** — you supply a plain-text CW message (e.g. a contest exchange or
   a CQ call).
2. **Chunking** — the message is split into segments of at most 24 characters,
   breaking on word boundaries where possible to keep the morse rhythm clean.
3. **CAT wrapping** — each chunk is prefixed with the appropriate Kenwood CAT
   memory-write command (e.g. `EX074x`) and terminated with a semicolon
   delimiter.
4. **Clipboard copy** — the full command sequence is written to the system
   clipboard via `pyperclip` so you can paste it immediately without any
   further editing.

---

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `chunk_size` | `24` | Maximum characters per memory slot (matches TS-590SG limit). |
| `command_prefix` | `EX074` | CAT command prefix for Kenwood TS-590SG CW memories. |

These constants are defined at the top of `cwstringformatter.py` and can be
edited to match a different rig's CAT syntax or memory slot size.

---

## License

This project is licensed under the **GNU General Public License v3.0**.
See the [LICENSE](LICENSE) file for the full text.

