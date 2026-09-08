import re

path_h = "profile/stats.svg"
path_v = "profile/stats-vertical.svg"

try:
    with open(path_h, "r", encoding="utf-8") as f:
        s = f.read()

    stars = re.search(r"data-testid=[\'\"]stars[\'\"][^>]*>([^<]+)<", s)
    commits = re.search(r"data-testid=[\'\"]commits[\'\"][^>]*>([^<]+)<", s)
    prs = re.search(r"data-testid=[\'\"]prs[\'\"][^>]*>([^<]+)<", s)
    issues = re.search(r"data-testid=[\'\"]issues[\'\"][^>]*>([^<]+)<", s)
    contribs = re.search(r"data-testid=[\'\"]contribs[\'\"][^>]*>([^<]+)<", s)
    rank = re.search(r"data-testid=[\'\"]level-rank-icon[\'\"][^>]*>([^<]+)<", s)
    header = re.search(r"data-testid=[\'\"]header[\'\"][^>]*>([^<]+)<", s)

    stars_v = stars.group(1).strip() if stars else "1"
    commits_v = commits.group(1).strip() if commits else "0"
    prs_v = prs.group(1).strip() if prs else "0"
    issues_v = issues.group(1).strip() if issues else "0"
    contribs_v = contribs.group(1).strip() if contribs else "0"
    rank_v = rank.group(1).strip() if rank else "C"
    header_v = header.group(1).strip() if header else "Abdoslam Baabbad's GitHub Stats"

    # Format horizontal card with fluid spacing for desktop
    fluid_stats = f"""<svg
  width="100%"
  height="195"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
  role="img"
  aria-labelledby="descId"
>
  <title id="titleId">{header_v}, Rank: {rank_v}</title>
  <desc id="descId">Total Stars Earned: {stars_v}, Total Commits: {commits_v}, Total PRs: {prs_v}, Total Issues: {issues_v}, Contributed to (last year): {contribs_v}</desc>
  <style>
    .header {{
      font: 700 20px 'Segoe UI', Ubuntu, Sans-Serif;
      fill: #2f97c1;
      animation: fadeInAnimation 0.8s ease-in-out forwards;
    }}
    @supports(-moz-appearance: auto) {{
      .header {{ font-size: 18px; }}
    }}
    .stat {{
      font: 700 15px 'Segoe UI', Ubuntu, "Helvetica Neue", Sans-Serif;
      fill: #0cf574;
    }}
    .stagger {{
      opacity: 0.3;
      animation: fadeInAnimation 0.3s ease-in-out forwards;
    }}
    .rank-text {{
      font: 800 26px 'Segoe UI', Ubuntu, Sans-Serif;
      fill: #0cf574;
    }}
    .bold {{ font-weight: 700 }}
    .icon {{
      fill: #f5b700;
      display: block;
    }}
    .rank-circle-rim {{
      stroke: #2f97c1;
      fill: none;
      stroke-width: 6;
      opacity: 0.2;
    }}
    .rank-circle {{
      stroke: #2f97c1;
      stroke-dasharray: 250;
      stroke-dashoffset: 232;
      fill: none;
      stroke-width: 6;
      stroke-linecap: round;
      opacity: 0.85;
      transform-origin: 0px 0px;
      transform: rotate(-90deg);
    }}
    @keyframes fadeInAnimation {{
      from {{ opacity: 0.3; }}
      to {{ opacity: 1; }}
    }}
  </style>

  <rect
    data-testid="card-bg"
    x="0.5"
    y="0.5"
    rx="4.5"
    height="194"
    stroke="#e4e2e2"
    width="calc(100% - 1px)"
    fill="#00000000"
    stroke-opacity="1"
  />

  <g data-testid="card-title" transform="translate(25, 35)">
    <text x="0" y="0" class="header" data-testid="header">{header_v}</text>
  </g>

  <g data-testid="main-card-body">
    <svg x="calc(100% - 85px)" y="105" overflow="visible">
      <g data-testid="rank-circle">
        <circle class="rank-circle-rim" cx="0" cy="0" r="40" />
        <circle class="rank-circle" cx="0" cy="0" r="40" />
        <text x="0" y="2" alignment-baseline="central" dominant-baseline="central" text-anchor="middle" class="rank-text" data-testid="level-rank-icon">{rank_v}</text>
      </g>
    </svg>

    <g transform="translate(0, 55)">
      <g transform="translate(0, 0)">
        <g class="stagger" transform="translate(25, 0)">
          <svg data-testid="icon" class="icon" viewBox="0 0 16 16" width="16" height="16">
            <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"/>
          </svg>
          <text class="stat bold" x="25" y="12.5">Total Stars Earned:</text>
          <text class="stat bold" x="235" y="12.5" data-testid="stars">{stars_v}</text>
        </g>
      </g>

      <g transform="translate(0, 25)">
        <g class="stagger" transform="translate(25, 0)">
          <svg data-testid="icon" class="icon" viewBox="0 0 16 16" width="16" height="16">
            <path fill-rule="evenodd" d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z"/>
          </svg>
          <text class="stat bold" x="25" y="12.5">Total Commits:</text>
          <text class="stat bold" x="235" y="12.5" data-testid="commits">{commits_v}</text>
        </g>
      </g>

      <g transform="translate(0, 50)">
        <g class="stagger" transform="translate(25, 0)">
          <svg data-testid="icon" class="icon" viewBox="0 0 16 16" width="16" height="16">
            <path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"/>
          </svg>
          <text class="stat bold" x="25" y="12.5">Total PRs:</text>
          <text class="stat bold" x="235" y="12.5" data-testid="prs">{prs_v}</text>
        </g>
      </g>

      <g transform="translate(0, 75)">
        <g class="stagger" transform="translate(25, 0)">
          <svg data-testid="icon" class="icon" viewBox="0 0 16 16" width="16" height="16">
            <path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z"/>
          </svg>
          <text class="stat bold" x="25" y="12.5">Total Issues:</text>
          <text class="stat bold" x="235" y="12.5" data-testid="issues">{issues_v}</text>
        </g>
      </g>

      <g transform="translate(0, 100)">
        <g class="stagger" transform="translate(25, 0)">
          <svg data-testid="icon" class="icon" viewBox="0 0 16 16" width="16" height="16">
            <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"/>
          </svg>
          <text class="stat bold" x="25" y="12.5">Contributed to (last year):</text>
          <text class="stat bold" x="235" y="12.5" data-testid="contribs">{contribs_v}</text>
        </g>
      </g>
    </g>
  </g>
</svg>"""
    with open(path_h, "w", encoding="utf-8") as f:
        f.write(fluid_stats)

    # Format vertical card for mobile view
    vert_stats = f"""<svg
  width="100%"
  height="auto"
  viewBox="0 0 400 450"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
  role="img"
  aria-labelledby="descId_v"
>
  <title id="titleId_v">{header_v}, Rank: {rank_v}</title>
  <desc id="descId_v">Total Stars Earned: {stars_v}, Total Commits: {commits_v}, Total PRs: {prs_v}, Total Issues: {issues_v}, Contributed to (last year): {contribs_v}</desc>
  <style>
    .header {{
      font: 700 21px 'Segoe UI', Ubuntu, Sans-Serif;
      fill: #2f97c1;
    }}
    .stat {{
      font: 700 17px 'Segoe UI', Ubuntu, "Helvetica Neue", Sans-Serif;
      fill: #0cf574;
    }}
    .stat-val {{
      font: 800 18px 'Segoe UI', Ubuntu, "Helvetica Neue", Sans-Serif;
      fill: #0cf574;
      text-anchor: end;
    }}
    .rank-text {{
      font: 800 34px 'Segoe UI', Ubuntu, Sans-Serif;
      fill: #0cf574;
    }}
    .rank-label {{
      font: 700 13px 'Segoe UI', Ubuntu, Sans-Serif;
      fill: #2f97c1;
      letter-spacing: 1.5px;
      opacity: 0.9;
    }}
    .icon {{
      fill: #f5b700;
      display: block;
    }}
    .rank-circle-rim {{
      stroke: #2f97c1;
      fill: none;
      stroke-width: 6;
      opacity: 0.2;
    }}
    .rank-circle {{
      stroke: #2f97c1;
      stroke-dasharray: 289;
      stroke-dashoffset: 268;
      fill: none;
      stroke-width: 6;
      stroke-linecap: round;
      opacity: 0.9;
      transform-origin: 200px 325px;
      transform: rotate(-90deg);
    }}
  </style>

  <rect
    data-testid="card-bg"
    x="0.5"
    y="0.5"
    rx="4.5"
    height="449"
    stroke="#e4e2e2"
    width="399"
    fill="#00000000"
    stroke-opacity="1"
  />

  <g data-testid="card-title" transform="translate(20, 35)">
    <text x="0" y="0" class="header" data-testid="header">{header_v}</text>
  </g>

  <g data-testid="main-card-body">
    <g transform="translate(20, 58)">
      <svg class="icon" viewBox="0 0 16 16" width="18" height="18" y="2">
        <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"/>
      </svg>
      <text class="stat" x="28" y="16">Total Stars Earned:</text>
      <text class="stat-val" x="360" y="16" data-testid="stars">{stars_v}</text>
    </g>

    <g transform="translate(20, 92)">
      <svg class="icon" viewBox="0 0 16 16" width="18" height="18" y="2">
        <path fill-rule="evenodd" d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z"/>
      </svg>
      <text class="stat" x="28" y="16">Total Commits:</text>
      <text class="stat-val" x="360" y="16" data-testid="commits">{commits_v}</text>
    </g>

    <g transform="translate(20, 126)">
      <svg class="icon" viewBox="0 0 16 16" width="18" height="18" y="2">
        <path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"/>
      </svg>
      <text class="stat" x="28" y="16">Total PRs:</text>
      <text class="stat-val" x="360" y="16" data-testid="prs">{prs_v}</text>
    </g>

    <g transform="translate(20, 160)">
      <svg class="icon" viewBox="0 0 16 16" width="18" height="18" y="2">
        <path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z"/>
      </svg>
      <text class="stat" x="28" y="16">Total Issues:</text>
      <text class="stat-val" x="360" y="16" data-testid="issues">{issues_v}</text>
    </g>

    <g transform="translate(20, 194)">
      <svg class="icon" viewBox="0 0 16 16" width="18" height="18" y="2">
        <path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"/>
      </svg>
      <text class="stat" x="28" y="16">Contributed to (last year):</text>
      <text class="stat-val" x="360" y="16" data-testid="contribs">{contribs_v}</text>
    </g>
  </g>

  <line x1="20" y1="235" x2="380" y2="235" stroke="#e4e2e2" stroke-opacity="0.25" stroke-width="1.5"/>

  <g data-testid="rank-circle" transform="translate(200, 320)">
    <circle class="rank-circle-rim" cx="0" cy="0" r="46" />
    <circle class="rank-circle" cx="0" cy="0" r="46" />
    <text x="0" y="2" alignment-baseline="central" dominant-baseline="central" text-anchor="middle" class="rank-text" data-testid="level-rank-icon">{rank_v}</text>
    <text x="0" y="68" text-anchor="middle" class="rank-label">OVERALL RANK</text>
  </g>
</svg>"""
    with open(path_v, "w", encoding="utf-8") as f:
        f.write(vert_stats)
    print("Formatted fluid stats cards successfully!")
except Exception as e:
    print("Stats formatter error:", e)
    exit(1)
