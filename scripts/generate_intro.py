#!/usr/bin/env python3
"""Render a 90-second portfolio intro video from programmatic motion graphics."""
from pathlib import Path
import math
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H, FPS, SECONDS = 1280, 720, 24, 90
OUT = Path("_site/videos/kishore-intro.mp4")
AUDIO = Path("build/narration.mp3")
OUT.parent.mkdir(parents=True, exist_ok=True)

SCENES = [
    {"start": 0, "end": 15, "eyebrow": "AZURE DEVOPS ENGINEER  /  HYDERABAD, INDIA",
     "title": ["Venkata Kishore", "Vusa"], "sub": "I automate the path from code to production.",
     "chips": ["CLOUD", "AUTOMATION", "RELIABILITY"], "code": ["$ whoami", "Azure DevOps Engineer", "status: open to opportunities", "focus: secure delivery"]},
    {"start": 15, "end": 30, "eyebrow": "CONTINUOUS DELIVERY",
     "title": ["Build. Test.", "Ship with confidence."], "sub": "Reusable GitHub Actions workflows and secure CI/CD.",
     "chips": ["GITHUB ACTIONS", "YAML", "QUALITY GATES"], "code": ["git push origin main", "✓ lint + tests", "✓ security scan", "✓ release approval"]},
    {"start": 30, "end": 45, "eyebrow": "CLOUD & INFRASTRUCTURE",
     "title": ["Cloud-native", "by design."], "sub": "Azure and AWS, with automation that scales.",
     "chips": ["AZURE", "AWS", "ANSIBLE"], "code": ["terraform plan", "ansible-playbook site.yml", "infra: repeatable"]},
    {"start": 45, "end": 60, "eyebrow": "CONTAINERS & ORCHESTRATION",
     "title": ["Deploy consistently.", "Recover quickly."], "sub": "Docker images, Kubernetes workloads and practical runbooks.",
     "chips": ["DOCKER", "KUBERNETES", "AKS"], "code": ["kubectl rollout status deploy/app", "✓ readiness probes", "✓ rolling updates"]},
    {"start": 60, "end": 75, "eyebrow": "DATA PLATFORM DELIVERY",
     "title": ["Microsoft Fabric", "release operations."], "sub": "Environment governance and data validation before deployment.",
     "chips": ["FABRIC", "KEY VAULT", "RBAC"], "code": ["validate workspace", "check table synchronization", "require approved deployment"]},
    {"start": 75, "end": 90, "eyebrow": "SECURE AUTOMATION  /  DELIVERY OWNERSHIP",
     "title": ["Engineering that", "moves teams forward."], "sub": "Explore the projects, pipelines and operational playbooks.",
     "chips": ["CI/CD", "DEVSECOPS", "OBSERVABILITY"], "code": ["4+ years of DevOps experience", "25% reliability improvement*", "40% less setup time*", "github.com/Kishore2488"]}
]

def font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()

F_SMALL, F_MED, F_TITLE, F_BIG, F_MONO = font(17), font(22), font(39, True), font(58, True), font(18)
BG = (7, 11, 16)
MINT = (85, 230, 177)
BLUE = (112, 167, 255)
WHITE = (243, 247, 251)
MUTED = (154, 170, 186)
LINE = (32, 45, 57)

def mix(a, b, t):
    return tuple(int(a[i] * (1-t) + b[i] * t) for i in range(3))

def draw_frame(t):
    scene = next((s for s in SCENES if s["start"] <= t < s["end"]), SCENES[-1])
    local = t - scene["start"]
    span = scene["end"] - scene["start"]
    fade = min(1.0, local / 0.6, (span - local) / 0.5)
    fade = max(0.0, fade)
    img = Image.new("RGB", (W, H), BG)
    # Soft, moving color field plus a restrained technical grid.
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx = 950 + int(24 * math.sin(t / 4))
    for radius in range(620, 40, -30):
        alpha = max(2, int(18 * (1 - radius / 680)))
        gd.ellipse((cx-radius, 150-radius, cx+radius, 150+radius), fill=(13, 65, 62, alpha))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    d = ImageDraw.Draw(img, "RGBA")
    for x in range(0, W, 64):
        d.line((x, 0, x, H), fill=(85, 230, 177, 15), width=1)
    for y in range(0, H, 64):
        d.line((0, y, W, y), fill=(85, 230, 177, 15), width=1)
    # Animated circuit nodes in the right-side dashboard.
    for i in range(15):
        x = 770 + ((i * 83 + int(t * 16)) % 450)
        y = 95 + ((i * 47) % 490)
        d.ellipse((x-2, y-2, x+2, y+2), fill=(85, 230, 177, 75))
    d.rounded_rectangle((55, 46, 1225, 674), radius=20, outline=(85, 230, 177, 75), width=2, fill=(5, 12, 18, 210))
    # Top brand line
    d.text((88, 75), "KISHORE.DEV", font=F_MED, fill=(*MINT, int(255*fade)))
    d.text((1050, 82), f"INTRO  /  0{int(t):02d}s", font=F_SMALL, fill=(*MUTED, int(255*fade)))
    d.line((88, 120, 1192, 120), fill=(*LINE, 255), width=2)
    d.text((88, 155), scene["eyebrow"], font=F_SMALL, fill=(*MINT, int(255*fade)))
    y = 203
    for idx, line in enumerate(scene["title"]):
        f = F_BIG if idx == 0 else F_TITLE
        d.text((84, y + int((1-fade)*10)), line, font=f, fill=(*(WHITE if idx == 0 else BLUE), int(255*fade)))
        y += 75 if idx == 0 else 62
    d.text((88, y+12), scene["sub"], font=F_MED, fill=(*MUTED, int(255*fade)))
    # Personal photo presenter: use the user's supplied portrait, cropped into a polished circular frame.
    # The source image is committed under assets/ so GitHub Actions can render it deterministically.
    ax, ay = 696, 218
    photo_path = Path("assets/kishore-photo.jpg")
    if not photo_path.is_file():
        raise SystemExit("Missing assets/kishore-photo.jpg; personal presenter cannot be rendered.")
    mask = Image.new("L", (124, 124), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, 123, 123), fill=255)
    # Load the portrait defensively: a malformed image must never break the Pages build.
    photo = None
    if photo_path.is_file():
        try:
            with Image.open(photo_path) as source:
                source.verify()
            with Image.open(photo_path) as source:
                photo = ImageOps.fit(source.convert("RGB"), (124, 124), method=Image.Resampling.LANCZOS, centering=(0.5, 0.34))
        except (OSError, ValueError) as exc:
            print(f"Warning: presenter photo is invalid ({exc}); using a clean illustrated fallback.")
    # Subtle dark backing, then portrait or a fallback illustration.
    d.ellipse((ax-70, ay-70, ax+70, ay+70), fill=(10, 35, 42, 245), outline=(85, 230, 177, 220), width=3)
    if photo is not None:
        img.paste(photo, (ax-62, ay-62), mask)
    else:
        # Reliable vector fallback while the photo asset is repaired.
        d.ellipse((ax-48, ay-48, ax+48, ay+48), fill=(26, 49, 59, 255), outline=(112, 167, 255, 180), width=2)
        d.ellipse((ax-20, ay-28, ax+20, ay+12), fill=(198, 151, 117, 255))
        d.pieslice((ax-24, ay-34, ax+24, ay+10), 180, 360, fill=(28, 25, 28, 255))
        d.rounded_rectangle((ax-34, ay+8, ax+34, ay+55), radius=20, fill=(26, 40, 62, 255))
    d = ImageDraw.Draw(img, "RGBA")
    d.ellipse((ax-64, ay-64, ax+64, ay+64), outline=(85, 230, 177, 240), width=3)
    d.ellipse((ax-69, ay-69, ax+69, ay+69), outline=(112, 167, 255, 110), width=2)
    d.rounded_rectangle((ax-61, ay+73, ax+61, ay+96), radius=10, fill=(8, 19, 27, 245), outline=(55, 133, 119, 230), width=1)
    d.text((ax-49, ay+77), "KISHORE  /  PRESENTER", font=font(11, True), fill=(*MINT, int(255*fade)))
    # Terminal panel
    d.rounded_rectangle((760, 170, 1177, 455), radius=12, fill=(9, 19, 27, 238), outline=(42, 77, 83, 255), width=2)
    d.ellipse((783, 190, 795, 202), fill=(255, 100, 110, 230))
    d.ellipse((804, 190, 816, 202), fill=(255, 204, 102, 230))
    d.ellipse((825, 190, 837, 202), fill=(*MINT, 230))
    d.text((858, 186), "release-terminal", font=F_SMALL, fill=(*MUTED, int(255*fade)))
    cy = 235
    for i, line in enumerate(scene["code"]):
        color = MINT if line.startswith("✓") or line.startswith("$") else WHITE
        d.text((786, cy), line, font=F_MONO, fill=(*color, int(255*fade)))
        cy += 42
    # Skill chips
    x = 88
    chip_y = 545
    for label in scene["chips"]:
        width = int(d.textlength(label, font=F_SMALL)) + 34
        d.rounded_rectangle((x, chip_y, x+width, chip_y+38), radius=18, fill=(18, 44, 48, 245), outline=(55, 133, 119, 220), width=1)
        d.text((x+17, chip_y+8), label, font=F_SMALL, fill=(*MINT, int(255*fade)))
        x += width + 12
    # Bottom progress line
    d.text((88, 620), "SECURE DELIVERY  ·  AUTOMATION  ·  RELIABILITY", font=F_SMALL, fill=(*MUTED, int(255*fade)))
    d.text((1110, 620), f"{int(t/SECONDS*100):02d}%", font=F_SMALL, fill=(*MINT, int(255*fade)))
    d.rounded_rectangle((88, 650, 1192, 658), radius=4, fill=(32, 45, 57, 255))
    d.rounded_rectangle((88, 650, 88 + int(1104*t/SECONDS), 658), radius=4, fill=(*MINT, 255))
    return img

def main():
    if not AUDIO.exists():
        raise SystemExit("Missing build/narration.mp3; generate narration before rendering.")
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-i", str(AUDIO), "-t", str(SECONDS), "-vf", "format=yuv420p",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
        "-af", "apad=pad_dur=90", "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart", str(OUT)
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    try:
        for frame in range(FPS * SECONDS):
            proc.stdin.write(draw_frame(frame / FPS).tobytes())
        proc.stdin.close()
        code = proc.wait()
        if code:
            raise SystemExit(f"ffmpeg exited with status {code}")
    except BrokenPipeError:
        raise SystemExit("ffmpeg stopped before all frames were written")
    print(f"Created {OUT} ({OUT.stat().st_size:,} bytes)")

if __name__ == "__main__":
    main()
