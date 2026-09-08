import re
import sys

def update_streak_card(file_path="profile/streak.svg"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Could not read {file_path}: {e}")
        return

    # Mobile typography boost: boost small 12px date labels to 14px bold for crystal clear mobile reading
    content = re.sub(r"font-size='12px'", "font-size='14px'", content)

    # Check if the Current Streak big number is 0
    num_pattern = r"(<!-- Current Streak big number -->\s*<g transform=['\"]translate\(247\.5,\s*48\)['\"][^>]*>\s*<text[^>]*>)\s*0\s*(</text>\s*</g>)"
    
    if re.search(num_pattern, content):
        print("Detected current streak = 0. Injecting animated Developer Terminal icon...")

        # 1. Add blinking cursor animation keyframe to the SVG <style> section if not already present
        if "cursorBlink" not in content:
            keyframes = """
            @keyframes cursorBlink {
                0%, 49% { opacity: 1; }
                50%, 100% { opacity: 0; }
            }
            @keyframes devPulse {
                0%, 100% { opacity: 0.95; }
                50% { opacity: 1; }
            }
            """
            content = content.replace("</style>", keyframes + "\n        </style>")

        # 2. Replace the big number with an animated developer terminal window
        animated_icon = """<!-- Animated Local Dev Terminal Icon -->
                <g transform='translate(247.5, 68)' style='animation: devPulse 2s ease-in-out infinite'>
                    <!-- Terminal Window Body -->
                    <rect x='-20' y='-15' width='40' height='30' rx='4' fill='#0d1117' stroke='#2F97C1' stroke-width='1.8'/>
                    <!-- Window Top Header Bar -->
                    <line x1='-20' y1='-7' x2='20' y2='-7' stroke='#2F97C1' stroke-width='1' opacity='0.4'/>
                    <!-- 3 Colored Window Dots -->
                    <circle cx='-14' cy='-11' r='1.3' fill='#FF5F56'/>
                    <circle cx='-10' cy='-11' r='1.3' fill='#FFBD2E'/>
                    <circle cx='-6' cy='-11' r='1.3' fill='#27C93F'/>
                    <!-- Command Prompt '>' in Gold -->
                    <path d='M -12 -1 L -7 3 L -12 7' fill='none' stroke='#F5B700' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/>
                    <!-- Live Blinking Cursor '_' in Emerald -->
                    <line x1='-3' y1='7' x2='4' y2='7' stroke='#0CF574' stroke-width='2' stroke-linecap='round' style='animation: cursorBlink 1s step-end infinite'/>
                </g>"""
        
        content = re.sub(num_pattern, animated_icon, content)

        # 3. Replace 'Current Streak' label with 'Local Dev'
        label_pattern = r"(<!-- Current Streak label -->\s*<g transform=['\"]translate\(247\.5,\s*108\)['\"][^>]*>\s*<text[^>]*>)\s*Current Streak\s*(</text>)"
        content = re.sub(label_pattern, r"\g<1>Local Dev\g<2>", content)

        # 4. Replace the date range with 'Working Offline'
        range_pattern = r"(<!-- Current Streak range -->\s*<g transform=['\"]translate\(247\.5,\s*145\)['\"][^>]*>\s*<text[^>]*>)\s*[^<]*\s*(</text>)"
        content = re.sub(range_pattern, r"\g<1>Working Offline\g<2>", content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file_path} with mobile typography boost!")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "profile/streak.svg"
    update_streak_card(path)
