from pathlib import Path

# Docling Core 2.101.1
source_file = Path(
    "/opt/app-root/lib64/python3.12/site-packages/"
    "docling_core/transforms/serializer/doclang.py"
)

old_code = """        parts: list[str] = []
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                cell = item.data.grid[i][j]
"""

new_code = """        # IA_HomeLabs: Build the table grid only once.
        grid = item.data.grid

        parts: list[str] = []
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                cell = grid[i][j]
"""

if not source_file.is_file():
    raise SystemExit(
        f"[IA_HomeLabs] Source file not found: {source_file}"
    )

content = source_file.read_text(encoding="utf-8")

if content.count(old_code) != 1:
    raise SystemExit(
        "[IA_HomeLabs] Expected source code not found exactly once. "
        "Verify the installed Docling Core version."
    )

content = content.replace(old_code, new_code, 1)

source_file.write_text(content, encoding="utf-8")

print("[IA_HomeLabs] DCLX grid optimization applied successfully.")
