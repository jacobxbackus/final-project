"""Lightweight repository check for the final project.

Fails on: invalid notebooks, code cells that do not parse, and hard-coded credentials.
Warns on: notebooks that were not run top to bottom, and files too large for GitHub Pages.
It never runs the notebooks, so it needs no data, packages, or API keys.
"""
import ast, re, sys, pathlib, warnings
import nbformat

warnings.simplefilter("ignore")

secret = re.compile(r"""(api_key|token|secret|password|bearer)\s*[=:]\s*["'][A-Za-z0-9_\-\.]{16,}["']|sk-[A-Za-z0-9]{20,}""", re.I)
skip_dirs = {".git", ".ipynb_checkpoints", ".venv", "venv", "__pycache__", "node_modules", ".kilo", ".claude"}
failures, notes = [], []


def files(pattern):
    return sorted(p for p in pathlib.Path(".").rglob(pattern) if not skip_dirs & set(p.parts))


def parses(source):
    if source.lstrip().startswith("%%"):
        return None  # cell magics such as %%sql or %%bash hold non-Python code
    source = "\n".join(line for line in source.splitlines() if not line.lstrip().startswith(("%", "!")))
    try:
        compile(source, "<cell>", "exec", flags=ast.PyCF_ONLY_AST | ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    except SyntaxError as error:
        return error


for path in files("*.ipynb"):
    try:
        nb = nbformat.read(path, as_version=4)
        nbformat.validate(nb)
    except Exception as error:
        failures.append(f"{path}: not a valid notebook ({str(error).splitlines()[0]})")
        continue
    code = [c for c in nb.cells if c.cell_type == "code" and c.source.strip()]
    for i, cell in enumerate(nb.cells):
        text = cell.source + "".join(str(o) for o in cell.get("outputs", []))
        if secret.search(text):
            failures.append(f"{path} cell {i}: looks like a hard-coded credential")
        if cell.cell_type == "code" and (error := parses(cell.source)):
            failures.append(f"{path} cell {i}: {error}")
    counts = [c.execution_count for c in code]
    if code and None in counts:
        notes.append((path, "some code cells have not been run. Use Restart Kernel and Run All Cells, then save."))
    elif counts != sorted(counts) or len(set(counts)) != len(counts):
        notes.append((path, "cells were run out of order. Use Restart Kernel and Run All Cells, then save."))
    print(f"{path}: {len(nb.cells)} cells checked")

for path in files("*.py"):
    if secret.search(path.read_text(errors="ignore")):
        failures.append(f"{path}: looks like a hard-coded credential")

for path in files("*"):
    size = path.stat().st_size / 1e6 if path.is_file() else 0
    if size > 25 and path.parts[0] == "web":
        notes.append((path, f"is {size:.0f} MB. Large files slow or break the GitHub Pages deploy; host them elsewhere and link to them."))

for path, message in notes:
    print(f"::warning file={path}::{path} {message}")
for message in failures:
    print(f"::error::{message}")
print("\n".join(failures) or "all checks passed")
sys.exit(bool(failures))
