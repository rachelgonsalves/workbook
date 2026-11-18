"""Build the workbook PDF and the website into the build/ folder.

Run it:   python build.py
GitHub Actions runs this automatically on every push, so you normally never need to.

Everything personal (names, links, colours, disclosures) comes from config.yaml.
"""

import os
import shutil
import sys
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "build"
IN_CI = os.environ.get("CI") == "true"


def load_config() -> dict:
    with open(ROOT / "config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def make_env() -> Environment:
    # StrictUndefined: a typo like {{ c.advisor.nmae }} stops the build instead of printing blank.
    env = Environment(
        loader=FileSystemLoader(str(ROOT)),
        autoescape=select_autoescape(["html"]),
        undefined=StrictUndefined,
    )
    env.filters["css_string"] = css_string
    env.filters["pretty_url"] = pretty_url
    return env


def pretty_url(url: str) -> str:
    """Short, printable version of a link: https://www.site.com/ -> site.com"""
    short = str(url).split("://", 1)[-1]
    if short.startswith("www."):
        short = short[4:]
    return short.rstrip("/")


def css_string(text: str) -> Markup:
    """Make config text safe to use inside CSS, e.g. content: "...";"""
    escaped = str(text).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    escaped = escaped.replace("<", "\\3C ").replace(">", "\\3E ")
    return Markup(f'"{escaped}"')


def write_tokens(cfg: dict) -> None:
    """Turn the colours in config.yaml into CSS variables (styles/tokens.css)."""
    lines = [":root {"]
    for name, value in cfg["colours"].items():
        lines.append(f"  --{name.replace('_', '-')}: {value};")
    lines.append("}")
    (OUT / "styles").mkdir(parents=True, exist_ok=True)
    (OUT / "styles" / "tokens.css").write_text("\n".join(lines) + "\n", encoding="utf-8")


def copy_static() -> None:
    for folder in ("styles", "assets"):
        src = ROOT / folder
        if src.exists():
            shutil.copytree(src, OUT / folder, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns("README.md"))


def build_site(cfg: dict, env: Environment) -> None:
    """Render every site/*.html page. Files starting with _ are layouts, not pages."""
    for page in sorted((ROOT / "site").glob("*.html")):
        if page.name.startswith("_"):
            continue
        html = env.get_template(f"site/{page.name}").render(c=cfg)
        (OUT / page.name).write_text(html, encoding="utf-8")
        print(f"  page  -> build/{page.name}")
    # Tell GitHub Pages to serve files as-is (no Jekyll processing).
    (OUT / ".nojekyll").write_text("", encoding="utf-8")


def build_pdf(cfg: dict, env: Environment) -> None:
    template = ROOT / "workbook" / "workbook.html"
    if not template.exists():
        print("  pdf   -> skipped (workbook/workbook.html not written yet, Phase 1)")
        return

    try:
        from weasyprint import HTML
    except (ImportError, OSError):
        if IN_CI:
            raise
        print("  pdf   -> skipped (WeasyPrint isn't installed on this PC; GitHub Actions builds it)")
        return

    html = env.get_template("workbook/workbook.html").render(c=cfg)
    out_file = OUT / cfg["workbook"]["pdf_filename"]
    # pdf_forms=True turns HTML inputs and checkboxes into real fillable PDF fields.
    HTML(string=html, base_url=str(ROOT)).write_pdf(out_file, pdf_forms=True)
    print(f"  pdf   -> build/{out_file.name}")


def main() -> int:
    cfg = load_config()
    env = make_env()

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    print("Building...")
    copy_static()
    write_tokens(cfg)
    build_site(cfg, env)
    build_pdf(cfg, env)
    print("Done. Open build/index.html in your browser to preview.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
