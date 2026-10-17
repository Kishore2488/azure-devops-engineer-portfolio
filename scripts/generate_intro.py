#!/usr/bin/env python3
"""Render a 45-second portfolio intro video from programmatic motion graphics."""
from pathlib import Path
import math
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, SECONDS = 1280, 720, 24, 45
OUT = Path("_site/videos/kishore-intro.mp4")
AUDIO = Path("build/narration.mp3")
OUT.parent.mkdir(parents=True, exist_ok=True)

SCENES = [
    {"start": 0, "end": 7, "eyebrow": "AZURE DEVOPS ENGINEER  /  HYDERABAD, INDIA",
     "title": ["Venkata Kishore", "Vusa"], "sub": "I automate the path from code to production.",
     "chips": ["CLOUD", "AUTOMATION", "RELIABILITY"], "code": ["$ whoami", "Azure DevOps Engineer", "status: open to opportunities"]},
    {"start": 7, "end": 14, "eyebrow": "CONTINUOUS DELIVERY",
     "title": ["Build. Test.", "Ship with confidence."], "sub": "Reusable GitHub Actions workflows and secure CI/CD.",
     "chips": ["GITHUB ACTIONS", "YAML", "QUALITY GATES"], "code": ["git push origin main", "✓ lint + tests", "✓ security scan", "✓ release approval"]},
    {"start": 14, "end": 21, "eyebrow": "CLOUD & INFRASTRUCTURE",
     "title": ["Cloud-native", "by design."], "sub": "Azure and AWS, with automation that scales.",
     "chips": ["AZURE", "AWS", "ANSIBLE"], "code": ["terraform plan", "ansible-playbook site.yml", "infra: repeatable"]},
    {"start": 21, "end": 28, "eyebrow": "CONTAINERS & ORCHESTRATION",
     "title": ["Deploy consistently.", "Recover quickly."], "sub": "Docker images, Kubernetes workloads and practical runbooks.",
     "chips": ["DOCKER", "KUBERNETES", "AKS"], "code": ["kubectl rollout status deploy/app", "✓ readiness probes", "✓ rolling updates"]},
    {"start": 28, "end": 35, "eyebrow": "DATA PLATFORM DELIVERY",
     "title": ["Microsoft Fabric", "release operations."], "sub": "Environment governance and data validation before deployment.",
     "chips": ["FABRIC", "KEY VAULT", "RBAC"], "code": ["validate workspace", "check table synchronization", "require approved deployment"]},
    {"start": 35, "end": 45, "eyebrow": "SECURE AUTOMATION  /  DELIVERY OWNERSHIP",
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
    # Illustrated AI presenter avatar: stylized, clearly synthetic, not a real-person likeness.
    # Place it between the headline and the terminal so it remains visible throughout the intro.
    ax, ay = 696, 218
    d.ellipse((ax-66, ay-66, ax+66, ay+66), fill=(10, 35, 42, 245), outline=(85, 230, 177, 210), width=3)
    d.ellipse((ax-52, ay-52, ax+52, ay+52), outline=(112, 167, 255, 100), width=2)
    # shoulders and shirt
    d.rounded_rectangle((ax-39, ay+19, ax+39, ay+55), radius=18, fill=(28, 57, 76, 255), outline=(112, 167, 255, 230), width=2)
    # neck and face
    d.rounded_rectangle((ax-13, ay+7, ax+13, ay+34), radius=7, fill=(190, 125, 88, 255))
    d.ellipse((ax-29, ay-38, ax+29, ay+25), fill=(207, 145, 104, 255), outline=(235, 181, 137, 255), width=1)
    # hair silhouette
    d.pieslice((ax-31, ay-44, ax+31, ay+2), start=180, end=360, fill=(27, 25, 28, 255))
    d.polygon([(ax-30, ay-15), (ax-25, ay-39), (ax-8, ay-47), (ax+12, ay-43), (ax+29, ay-27), (ax+20, ay-23), (ax+6, ay-31), (ax-10, ay-29)], fill=(27, 25, 28, 255))
    # facial features
    d.ellipse((ax-18, ay-8, ax-11, ay-2), fill=(30, 29, 29, 255))
    d.ellipse((ax+11, ay-8, ax+18, ay-2), fill=(30, 29, 29, 255))
    d.line((ax-18, ay-13, ax-10, ay-15), fill=(49, 35, 30, 255), width=2)
    d.line((ax+10, ay-15, ax+18, ay-13), fill=(49, 35, 30, 255), width=2)
    d.line((ax, ay-3, ax-3, ay+7, ax+3, ay+8), fill=(155, 91, 66, 255), width=2)
    d.arc((ax-11, ay+5, ax+11, ay+19), start=10, end=170, fill=(95, 44, 42, 255), width=2)
    d.rounded_rectangle((ax-53, ay+69, ax+53, ay+91), radius=10, fill=(8, 19, 27, 240), outline=(55, 133, 119, 220), width=1)
    d.text((ax-43, ay+72), "AI AVATAR", font=font(12, True), fill=(*MINT, int(255*fade)))
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
        "-af", "apad=pad_dur=45", "-c:a", "aac", "-b:a", "128k",
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
