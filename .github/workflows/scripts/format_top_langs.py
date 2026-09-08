import re

path = "profile/top-langs.svg"
try:
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    s = re.sub(r"width=\"\d+\"", "width=\"495\"", s, count=1)
    s = re.sub(r"viewBox=\"0 0 \d+ \d+\"", "viewBox=\"0 0 495 245\"", s)
    s = re.sub(r"stroke-opacity=\"1\"", "stroke-opacity=\"0\"", s)
    s = re.sub(r"font:\s*600\s*18px\s*\'Segoe UI\'", "font: 700 20px \'Segoe UI\'", s)
    s = re.sub(r"\.lang-name\s*\{\s*font:\s*400\s*11px[^\}]*\}", ".lang-name { font: 600 14px \"Segoe UI\", Ubuntu, Sans-Serif; fill: #0cf574; }", s)
    s = re.sub(r"width=\"205\"", "width=\"380\"", s)
    s = re.sub(r"height=\"8\"", "height=\"11\"", s)
    s = re.sub(r"x=\"215\"", "x=\"390\"", s)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    print("Aligned top-langs card successfully!")
except Exception as e:
    print("Top-langs align skipped:", e)
