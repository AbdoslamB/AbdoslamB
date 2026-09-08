import re

path_h = "profile/streak.svg"
path_v = "profile/streak-vertical.svg"

try:
    with open(path_h, "r", encoding="utf-8") as f:
        s = f.read()

    num_pat = r"(<!-- Current Streak big number -->\s*<g transform=[\'\"]translate\(247\.5,\s*48\)[\'\"][^>]*>\s*<text[^>]*>)\s*0\s*(</text>\s*</g>)"
    is_zero_streak = bool(re.search(num_pat, s)) or ("Local Dev" in s and "cursorBlink" in s)

    tot_m = re.search(r"<!-- Total Contributions big number -->.*?<text[^>]*>\s*([^<]+)\s*</text>", s, re.DOTALL)
    tot_num = tot_m.group(1).strip() if tot_m else "421"
    tot_r_m = re.search(r"<!-- Total Contributions range -->.*?<text[^>]*>\s*([^<]+)\s*</text>", s, re.DOTALL)
    tot_range = tot_r_m.group(1).strip() if tot_r_m else "Oct 5, 2018 - Present"

    curr_num_m = re.search(r"<!-- Current Streak big number -->.*?<text[^>]*>\s*([^<]+)\s*</text>", s, re.DOTALL)
    curr_num = curr_num_m.group(1).strip() if curr_num_m else "3"
    curr_r_m = re.search(r"<!-- Current Streak range -->.*?<text[^>]*>\s*([^<]+)\s*</text>", s, re.DOTALL)
    curr_range = curr_r_m.group(1).strip() if curr_r_m else "Sep 5 - Sep 7"

    long_m = re.search(r"<!-- Longest Streak big number -->.*?<text[^>]*>\s*([^<]+)\s*</text>", s, re.DOTALL)
    long_num = long_m.group(1).strip() if long_m else "5"
    long_r_m = re.search(r"<!-- Longest Streak range -->.*?<text[^>]*>\s*([^<]+)\s*</text>", s, re.DOTALL)
    long_range = long_r_m.group(1).strip() if long_r_m else "Dec 11, 2021 - Dec 15, 2021"

    if is_zero_streak:
        curr_h_content = """<!-- Terminal Icon for Local Dev -->
        <svg x='50%' y='68' overflow='visible'>
            <g style='animation: devPulse 2s ease-in-out infinite'>
                <rect x='-20' y='-15' width='40' height='30' rx='4' fill='#0d1117' stroke='#2F97C1' stroke-width='1.8'/>
                <line x1='-20' y1='-7' x2='20' y2='-7' stroke='#2F97C1' stroke-width='1' opacity='0.4'/>
                <circle cx='-14' cy='-11' r='1.3' fill='#FF5F56'/>
                <circle cx='-10' cy='-11' r='1.3' fill='#FFBD2E'/>
                <circle cx='-6' cy='-11' r='1.3' fill='#27C93F'/>
                <path d='M -12 -1 L -7 3 L -12 7' fill='none' stroke='#F5B700' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/>
                <line x1='-3' y1='7' x2='4' y2='7' stroke='#0CF574' stroke-width='2' stroke-linecap='round' style='animation: cursorBlink 1s step-end infinite'/>
            </g>
        </svg>
        <text x='50%' y='140' text-anchor='middle' fill='#F5B700' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='700' font-size='14px'>
            Local Dev
        </text>
        <text x='50%' y='166' text-anchor='middle' fill='#0CF574' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='400' font-size='14px'>
            Working Offline
        </text>"""
        curr_v_content = """<!-- Animated Local Dev Terminal Icon -->
        <g transform='translate(195, 235)' style='animation: devPulse 2s ease-in-out infinite'>
            <rect x='-32' y='-23' width='64' height='46' rx='6' fill='#0d1117' stroke='#2F97C1' stroke-width='2.2'/>
            <line x1='-32' y1='-11' x2='32' y2='-11' stroke='#2F97C1' stroke-width='1.4' opacity='0.4'/>
            <circle cx='-22' cy='-17' r='2' fill='#FF5F56'/>
            <circle cx='-16' cy='-17' r='2' fill='#FFBD2E'/>
            <circle cx='-10' cy='-17' r='2' fill='#27C93F'/>
            <path d='M -18 -2 L -10 5 L -18 12' fill='none' stroke='#F5B700' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'/>
            <line x1='-5' y1='12' x2='7' y2='12' stroke='#0CF574' stroke-width='2.8' stroke-linecap='round' style='animation: cursorBlink 1s step-end infinite'/>
        </g>
        <g transform='translate(195, 288)'>
            <text x='0' y='24' stroke-width='0' text-anchor='middle' fill='#F5B700' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='700' font-size='18px' font-style='normal'>
                Local Dev
            </text>
        </g>
        <g transform='translate(195, 320)'>
            <text x='0' y='22' stroke-width='0' text-anchor='middle' fill='#0CF574' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='500' font-size='16px' font-style='normal'>
                Working Offline
            </text>
        </g>"""
    else:
        curr_h_content = f"""<g mask='url(#mask_out_ring_behind_fire)'>
            <circle cx='50%' cy='71' r='40' fill='none' stroke='#2F97C1' stroke-width='5'></circle>
        </g>
        <svg x='50%' y='19.5' overflow='visible'>
            <g stroke-opacity='0'>
                <path d='M -12 -0.5 L 15 -0.5 L 15 23.5 L -12 23.5 L -12 -0.5 Z' fill='none'/>
                <path d='M 1.5 0.67 C 1.5 0.67 2.24 3.32 2.24 5.47 C 2.24 7.53 0.89 9.2 -1.17 9.2 C -3.23 9.2 -4.79 7.53 -4.79 5.47 L -4.76 5.11 C -6.78 7.51 -8 10.62 -8 13.99 C -8 18.41 -4.42 22 0 22 C 4.42 22 8 18.41 8 13.99 C 8 8.6 5.41 3.79 1.5 0.67 Z M -0.29 19 C -2.07 19 -3.51 17.6 -3.51 15.86 C -3.51 14.24 -2.46 13.1 -0.7 12.74 C 1.07 12.38 2.9 11.53 3.92 10.16 C 4.31 11.45 4.51 12.81 4.51 14.2 C 4.51 16.85 2.36 19 -0.29 19 Z' fill='#2F97C1'/>
            </g>
        </svg>
        <text x='50%' y='80' text-anchor='middle' fill='#F5B700' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='700' font-size='28px' style='animation: currstreak 0.6s linear forwards'>
            {curr_num}
        </text>
        <text x='50%' y='140' text-anchor='middle' fill='#F5B700' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='700' font-size='14px' style='animation: fadein 0.5s linear forwards'>
            Current Streak
        </text>
        <text x='50%' y='166' text-anchor='middle' fill='#0CF574' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='400' font-size='12px' style='animation: fadein 0.5s linear forwards'>
            {curr_range}
        </text>"""
        curr_v_content = f"""<g mask='url(#mask_out_ring_behind_fire_v)'>
            <circle cx='195' cy='235' r='46' fill='none' stroke='#2F97C1' stroke-width='6'></circle>
        </g>
        <g transform='translate(195, 172)' stroke-opacity='0'>
            <path d='M -14 -0.5 L 17 -0.5 L 17 27 L -14 27 L -14 -0.5 Z' fill='none'/>
            <path d='M 1.7 0.8 C 1.7 0.8 2.5 3.8 2.5 6.2 C 2.5 8.6 1.0 10.5 -1.3 10.5 C -3.6 10.5 -5.4 8.6 -5.4 6.2 L -5.3 5.8 C -7.6 8.5 -9.0 12.0 -9.0 15.9 C -9.0 20.9 -4.9 25.0 0 25.0 C 4.9 25.0 9.0 20.9 9.0 15.9 C 9.0 9.8 6.1 4.3 1.7 0.8 Z M -0.3 21.5 C -2.3 21.5 -4.0 20.0 -4.0 18.0 C -4.0 16.1 -2.8 14.8 -0.8 14.4 C 1.2 14.0 3.3 13.0 4.4 11.5 C 4.9 13.0 5.1 14.5 5.1 16.1 C 5.1 19.1 2.7 21.5 -0.3 21.5 Z' fill='#2F97C1' stroke-opacity='0'/>
        </g>
        <g transform='translate(195, 212)'>
            <text x='0' y='42' stroke-width='0' text-anchor='middle' fill='#F5B700' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='800' font-size='48px' font-style='normal' style='animation: currstreak 0.6s linear forwards'>
                {curr_num}
            </text>
        </g>
        <g transform='translate(195, 288)'>
            <text x='0' y='24' stroke-width='0' text-anchor='middle' fill='#F5B700' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='700' font-size='18px' font-style='normal'>
                Current Streak
            </text>
        </g>
        <g transform='translate(195, 320)'>
            <text x='0' y='22' stroke-width='0' text-anchor='middle' fill='#0CF574' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='500' font-size='16px' font-style='normal'>
                {curr_range}
            </text>
        </g>"""

    fluid_h_svg = f"""<svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'
     style='isolation: isolate' width='100%' height='195' direction='ltr'>
    <style>
        @keyframes currstreak {{
            0% {{ font-size: 3px; opacity: 0.2; }}
            80% {{ font-size: 34px; opacity: 1; }}
            100% {{ font-size: 28px; opacity: 1; }}
        }}
        @keyframes fadein {{
            0% {{ opacity: 0.3; }}
            100% {{ opacity: 1; }}
        }}
        @keyframes cursorBlink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
        @keyframes devPulse {{ 0%, 100% {{ opacity: 0.95; }} 50% {{ opacity: 1; }} }}
    </style>
    <defs>
        <mask id='mask_out_ring_behind_fire' maskUnits='userSpaceOnUse'>
            <rect width='100%' height='100%' fill='white'/>
            <ellipse cx='50%' cy='32' rx='13' ry='18' fill='black'/>
        </mask>
    </defs>
    <rect x='0.5' y='0.5' width='calc(100% - 1px)' height='194' rx='4.5' fill='#000000' fill-opacity='0' stroke='#E4E2E2' stroke-opacity='1'/>
    <line x1='33.3%' y1='28' x2='33.3%' y2='170' stroke='#E4E2E2' stroke-opacity='0.4' stroke-width='1'/>
    <line x1='66.6%' y1='28' x2='66.6%' y2='170' stroke='#E4E2E2' stroke-width='1' stroke-opacity='0.4'/>
    <g style='isolation: isolate'>
        <text x='16.65%' y='80' text-anchor='middle' fill='#2F97C1' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='700' font-size='28px'>
            {tot_num}
        </text>
        <text x='16.65%' y='116' text-anchor='middle' fill='#2F97C1' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='400' font-size='14px'>
            Total Contributions
        </text>
        <text x='16.65%' y='146' text-anchor='middle' fill='#0CF574' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='400' font-size='12px'>
            {tot_range}
        </text>
    </g>
    <g style='isolation: isolate'>
        {curr_h_content}
    </g>
    <g style='isolation: isolate'>
        <text x='83.35%' y='80' text-anchor='middle' fill='#2F97C1' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='700' font-size='28px'>
            {long_num}
        </text>
        <text x='83.35%' y='116' text-anchor='middle' fill='#2F97C1' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='400' font-size='14px'>
            Longest Streak
        </text>
        <text x='83.35%' y='146' text-anchor='middle' fill='#0CF574' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='400' font-size='12px'>
            {long_range}
        </text>
    </g>
</svg>"""
    with open(path_h, "w", encoding="utf-8") as f:
        f.write(fluid_h_svg)

    vert_svg = f"""<svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'
     style='isolation: isolate' viewBox='0 0 390 540' width='100%' height='auto' direction='ltr'>
    <style>
        @keyframes currstreak {{
            0% {{ font-size: 8px; opacity: 0.2; }}
            80% {{ font-size: 52px; opacity: 1; }}
            100% {{ font-size: 48px; opacity: 1; }}
        }}
        @keyframes cursorBlink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
        @keyframes devPulse {{ 0%, 100% {{ opacity: 0.95; }} 50% {{ opacity: 1; }} }}
    </style>
    <defs>
        <clipPath id='outer_rectangle_v'>
            <rect width='390' height='540' rx='4.5'/>
        </clipPath>
        <mask id='mask_out_ring_behind_fire_v'>
            <rect width='390' height='540' fill='white'/>
            <ellipse cx='195' cy='188' rx='15' ry='20' fill='black'/>
        </mask>
    </defs>
    <g clip-path='url(#outer_rectangle_v)'>
        <g style='isolation: isolate'>
            <rect stroke='#E4E2E2' stroke-opacity='1' fill='#000000' fill-opacity='0' rx='4.5' x='0.5' y='0.5' width='389' height='539'/>
        </g>
        <g style='isolation: isolate'>
            <line x1='20' y1='155' x2='370' y2='155' stroke='#E4E2E2' stroke-opacity='0.25' stroke-width='1.5'/>
            <line x1='20' y1='365' x2='370' y2='365' stroke='#E4E2E2' stroke-opacity='0.25' stroke-width='1.5'/>
        </g>
        <g style='isolation: isolate'>
            <g transform='translate(195, 18)'>
                <text x='0' y='42' stroke-width='0' text-anchor='middle' fill='#2F97C1' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='800' font-size='48px' font-style='normal'>
                    {tot_num}
                </text>
            </g>
            <g transform='translate(195, 75)'>
                <text x='0' y='24' stroke-width='0' text-anchor='middle' fill='#2F97C1' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='600' font-size='18px' font-style='normal'>
                    Total Contributions
                </text>
            </g>
            <g transform='translate(195, 108)'>
                <text x='0' y='22' stroke-width='0' text-anchor='middle' fill='#0CF574' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='500' font-size='16px' font-style='normal'>
                    {tot_range}
                </text>
            </g>
        </g>
        <g style='isolation: isolate'>
            {curr_v_content}
        </g>
        <g style='isolation: isolate'>
            <g transform='translate(195, 385)'>
                <text x='0' y='42' stroke-width='0' text-anchor='middle' fill='#2F97C1' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='800' font-size='48px' font-style='normal'>
                    {long_num}
                </text>
            </g>
            <g transform='translate(195, 442)'>
                <text x='0' y='24' stroke-width='0' text-anchor='middle' fill='#2F97C1' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='600' font-size='18px' font-style='normal'>
                    Longest Streak
                </text>
            </g>
            <g transform='translate(195, 475)'>
                <text x='0' y='22' stroke-width='0' text-anchor='middle' fill='#0CF574' stroke='none' font-family='"Segoe UI", Ubuntu, sans-serif' font-weight='500' font-size='16px' font-style='normal'>
                    {long_range}
                </text>
            </g>
        </g>
    </g>
</svg>"""
    with open(path_v, "w", encoding="utf-8") as f:
        f.write(vert_svg)
    print("Processed fluid streak cards successfully!")
except Exception as e:
    print("Streak processor error:", e)
    exit(1)
