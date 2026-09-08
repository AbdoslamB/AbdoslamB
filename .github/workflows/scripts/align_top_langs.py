import re
import sys

def align_and_boost_top_langs(file_path="profile/top-langs.svg"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Could not read {file_path}: {e}")
        return

    # 1. Update card width to 495px
    content = re.sub(r'width="\d+"', 'width="495"', content, count=1)
    content = re.sub(r'viewBox="0 0 \d+ \d+"', 'viewBox="0 0 495 245"', content)

    # 2. Keep border hidden (stroke-opacity="0") and card-bg width to 494
    content = re.sub(r'data-testid="card-bg"[^>]*width="\d+"', 'data-testid="card-bg" width="494"', content)
    content = re.sub(r'stroke-opacity="1"', 'stroke-opacity="0"', content)

    # 3. Boost Header from 18px to 20px
    content = re.sub(r"font:\s*600\s*18px\s*'Segoe UI'", "font: 700 20px 'Segoe UI'", content)

    # 4. Boost Language Name & Percentage fonts from 11px to 14px bold for mobile readability
    content = re.sub(
        r'\.lang-name\s*\{\s*font:\s*400\s*11px[^;]*;',
        '.lang-name {\n      font: 600 14px "Segoe UI", Ubuntu, Sans-Serif;',
        content
    )

    # 5. Stretch progress bars to 380px and increase height from 8 to 11px for mobile visibility
    content = re.sub(r'width="205"', 'width="380"', content)
    content = re.sub(r'height="8"', 'height="11"', content)
    content = re.sub(r'rx="5" ry="5"', 'rx="5.5" ry="5.5"', content)

    # 6. Move percentage numbers to x="390"
    content = re.sub(r'x="215"', 'x="390"', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully applied mobile font & scale boost to {file_path}!")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "profile/top-langs.svg"
    align_and_boost_top_langs(path)
