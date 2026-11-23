import os

LINE = "My neighbour left a warm banana muffin at my door with a note that just said 'you looked tired yesterday' \u2014 I ate it in the hallway, still in my coat."

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-200 chars,
# not only whitespace, a single line. Fail loudly instead of shipping
# an invalid entry.
if not 1 <= len(LINE) <= 200 or not LINE.strip() or "\n" in LINE:
    raise SystemExit("entry line violates the 1-200 char single-line gate")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
