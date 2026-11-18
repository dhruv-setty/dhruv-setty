import math

AXES = [
    ("Identity Governance", "SailPoint IIQ · JML", 5),
    ("Hybrid Identity", "Entra ID · AD", 4),
    ("Access Assurance", "Controls · Evidence", 4),
    ("Federation & Auth", "OAuth 2.0 · OIDC · SAML", 4),
    ("Systems & Virtualisation", "Linux · KVM · Arm", 3),
    ("Automation", "C# · PowerShell · Python", 3),
]
MAX = 5
W, H = 980, 640
CX, CY, R = W / 2, H / 2 + 6, 205

def pt(i, r):
    a = math.radians(-90 + 60 * i)
    return CX + r * math.cos(a), CY + r * math.sin(a)

def poly(r):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, r) for i in range(6)))

def svg(theme):
    if theme == "light":
        fg, mute, grid, fill, area, stroke = "#1f1f1d", "#77776f", "#dcdcd6", "#ffffff", "rgba(31,31,29,0.10)", "#1f1f1d"
    else:
        fg, mute, grid, fill, area, stroke = "#e6edf3", "#8b949e", "#30363d", "#0d1117", "rgba(230,237,243,0.12)", "#e6edf3"
    font = "Inter, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Skills hexagon">',
         f'<rect width="{W}" height="{H}" rx="14" fill="{fill}"/>']
    for k in range(1, MAX + 1):
        o.append(f'<polygon points="{poly(R * k / MAX)}" fill="none" stroke="{grid}" stroke-width="{1.4 if k == MAX else 1}"/>')
    for i in range(6):
        x, y = pt(i, R)
        o.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" stroke="{grid}" stroke-width="1"/>')
    vals = " ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, R * v / MAX) for i, (_, _, v) in enumerate(AXES)))
    o.append(f'<polygon points="{vals}" fill="{area}" stroke="{stroke}" stroke-width="2.2" stroke-linejoin="round"/>')
    for i, (_, _, v) in enumerate(AXES):
        x, y = pt(i, R * v / MAX)
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    for i, (name, sub, v) in enumerate(AXES):
        x, y = pt(i, R + 34)
        anchor = "middle" if i in (0, 3) else ("start" if i in (1, 2) else "end")
        dy = -14 if i == 0 else (8 if i == 3 else -4)
        o.append(f'<text x="{x:.1f}" y="{y + dy:.1f}" text-anchor="{anchor}" font-family="{font}" font-size="17" font-weight="600" fill="{fg}">{name.replace("&", "&amp;")}</text>')
        o.append(f'<text x="{x:.1f}" y="{y + dy + 21:.1f}" text-anchor="{anchor}" font-family="{font}" font-size="13.5" fill="{mute}">{sub}</text>')
    o.append('</svg>')
    return "\n".join(o)

for t in ("light", "dark"):
    open(f"assets/skills-hexagon-{t}.svg", "w").write(svg(t))
