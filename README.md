# passgen

A simple CLI password generator written in Python.

## Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/password-generator.git
cd password-generator

# Make executable
chmod +x passgen.py

# Install locally
pip install -e .
```

## Usage

```bash
# Default: 16-character password with special chars
passgen

# Custom length
passgen -l 24

# Multiple passwords
passgen -c 5

# Without special characters
passgen -n

# Combine options
passgen -l 32 -c 3 -n

# Reproducible output (useful for testing)
passgen -l 16 -s 42
```

## Options

| Flag | Description | Default |
|------|-------------|---------|
| `-l, --length` | Password length | 16 |
| `-n, --no-special` | Exclude special characters | false |
| `-c, --count` | Number of passwords | 1 |
| `-s, --seed` | Random seed for reproducibility | random |

## As a Python Module

```python
from passgen import generate_password

# Generate a password
pwd = generate_password(16, use_special=True)
print(pwd)
```
