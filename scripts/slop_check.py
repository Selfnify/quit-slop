import colorsys
import re
import sys
from pathlib import Path

EXTS = {".html", ".htm", ".css", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".md", ".mdx"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next"}

BANNED_PHRASES = [
    "welcome to", "in today's", "say goodbye", "unlock", "supercharge", "elevate",
    "seamless", "revolutionize", "empower", "all-in-one", "next-generation",
    "next generation", "to the next level", "game-changer", "game changer",
    "lorem ipsum", "john doe", "jane doe", "cutting-edge", "leverage",
]
PURPLE_WORDS = re.compile(r"\b(purple|violet|indigo|fuchsia)\b|(from|via|to)-(purple|violet|indigo|fuchsia)-\d+", re.I)
HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
UPPER_CSS = re.compile(r"text-transform\s*:\s*uppercase|(?<![\w-])uppercase(?![\w-])")
TEXT_NODE = re.compile(r">\s*([^<>{}\n]{3,})\s*<")


def is_purple(hexcode: str) -> bool:
    h = hexcode.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    hue, light, sat = colorsys.rgb_to_hls(r, g, b)[0] * 360, colorsys.rgb_to_hls(r, g, b)[1], colorsys.rgb_to_hls(r, g, b)[2]
    return 255 <= hue <= 295 and sat > 0.35 and 0.15 < light < 0.85


def scan(path: Path):
    errors, warns = [], []
    text = path.read_text(errors="ignore")
    lines = text.splitlines()
    is_style = path.suffix in {".css"}

    def add(bucket, i, msg):
        bucket.append(f"{path}:{i}: {msg}")

    for i, line in enumerate(lines, 1):
        low = line.lower()
        if "\u2014" in line:
            add(errors, i, "em dash. Use a comma, colon, period or hyphen")
        if re.search(r"\s\u2013\s", line):
            add(warns, i, "en dash used like a dash. Prefer a hyphen or comma")
        if UPPER_CSS.search(line):
            add(errors, i, "uppercase styling. Use sentence case")
        for m in TEXT_NODE.finditer(line):
            t = m.group(1).strip()
            letters = re.sub(r"[^A-Za-z]", "", t)
            if len(letters) >= 4 and t == t.upper() and re.search(r"[A-Z]{4}", t) and "&" not in t[:1]:
                add(errors, i, f'all caps text: "{t[:40]}"')
        if "gradient" in low and (PURPLE_WORDS.search(line) or any(is_purple(h) for h in (m.group(0) for m in HEX.finditer(line)))):
            add(errors, i, "purple gradient. Pick one accent that fits the product")
        elif PURPLE_WORDS.search(line) and "gradient" not in low:
            add(warns, i, "purple-family colour. Is it the product's real accent?")
        for p in BANNED_PHRASES:
            if p in low:
                add(warns, i, f'stock phrase "{p}". Rewrite with something specific')
        if re.search(r"transition\s*:\s*all\b", low) or "transition-all" in low:
            add(warns, i, "transition: all. Animate specific properties")
        if re.search(r"outline\s*:\s*(none|0)\b", low) and "focus-visible" not in text:
            add(warns, i, "outline removed with no :focus-visible replacement")
        if re.search(r"(rounded-full|border-radius\s*:\s*9999px)", low) and re.search(r"badge|pill|chip", low):
            add(warns, i, "badge or pill. Is it earning its place?")
        if re.search(r"(class|className)=[\"'][^\"']*(eyebrow|overline|kicker)", low):
            add(errors, i, "eyebrow element")
        if re.search(r"(status-dot|\bdot\b|bullet-dot)", low) and re.search(r"class|className|\.", low):
            add(warns, i, "dot element. Is it necessary?")

    moves = re.search(r"@keyframes|transition\s*:|transition-|animation\s*:|animate-", text)
    if moves and "prefers-reduced-motion" not in text and not is_style:
        add(warns, 1, "motion used but no prefers-reduced-motion handling in this file")
    if path.suffix in {".html", ".htm"}:
        if "<h1" in text and "text-wrap" not in text:
            add(warns, 1, "no text-wrap: balance on headlines")
        if re.search(r"\d", text) and "tabular-nums" not in text and re.search(r"price|\$\d|%|timer|table", text, re.I):
            add(warns, 1, "numbers shown but no tabular-nums")
        if "viewport" not in text:
            add(warns, 1, "no viewport meta tag")
    return errors, warns


def collect(args):
    for a in args:
        p = Path(a)
        if p.is_file():
            yield p
        elif p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.suffix in EXTS and not (SKIP_DIRS & set(f.parts)):
                    yield f


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    all_err, all_warn, n = [], [], 0
    for f in collect(sys.argv[1:]):
        n += 1
        e, w = scan(f)
        all_err += e
        all_warn += w
    for m in all_err:
        print("ERROR  ", m)
    for m in all_warn:
        print("WARN   ", m)
    print(f"\n{n} file(s) scanned: {len(all_err)} error(s), {len(all_warn)} warning(s)")
    return 1 if all_err else 0


if __name__ == "__main__":
    sys.exit(main())
