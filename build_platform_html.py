#!/usr/bin/env python3
from __future__ import annotations

import html
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value.strip().lower())
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.replace("đ", "d")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "section"


def inline_markdown(value: str) -> str:
    escaped = html.escape(value)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def close_blocks(out: list[str], state: dict[str, bool]) -> None:
    if state.get("list"):
        out.append("</ul>")
        state["list"] = False
    if state.get("ordered"):
        out.append("</ol>")
        state["ordered"] = False
    if state.get("table"):
        out.append("</table></div>")
        state["table"] = False


def markdown_to_html(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    state = {"code": False, "list": False, "ordered": False, "table": False, "table_header": False}
    i = 0

    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()

        if line.startswith("```"):
            if state["code"]:
                out.append("</code></pre>")
                state["code"] = False
            else:
                close_blocks(out, state)
                out.append("<pre><code>")
                state["code"] = True
            i += 1
            continue

        if state["code"]:
            out.append(html.escape(line) + "\n")
            i += 1
            continue

        if not line.strip():
            close_blocks(out, state)
            i += 1
            continue

        image_match = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", line.strip())
        if image_match:
            close_blocks(out, state)
            alt = html.escape(image_match.group(1))
            src = html.escape(image_match.group(2))
            figcaption = ""
            if i + 1 < len(lines):
                caption_line = lines[i + 1].strip()
                caption_match = re.match(r"^\*(.+)\*$", caption_line)
                if caption_match:
                    figcaption = f"<figcaption>{inline_markdown(caption_match.group(1))}</figcaption>"
                    i += 1
            out.append(f'<figure class="lesson-figure"><img src="{src}" alt="{alt}" loading="lazy">{figcaption}</figure>')
            i += 1
            continue

        if line.startswith("|") and line.endswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if all(re.fullmatch(r"[-: ]*", c) for c in cells):
                state["table_header"] = False
                i += 1
                continue
            if not state["table"]:
                close_blocks(out, state)
                out.append('<div class="table-wrap"><table>')
                state["table"] = True
                state["table_header"] = True
            tag = "th" if state["table_header"] else "td"
            out.append("<tr>" + "".join(f"<{tag}>{inline_markdown(c)}</{tag}>" for c in cells) + "</tr>")
            state["table_header"] = False
            i += 1
            continue

        ordered_match = re.match(r"^(\d+)\. (.+)$", line)
        if ordered_match:
            if not state["ordered"]:
                close_blocks(out, state)
                out.append("<ol>")
                state["ordered"] = True
            out.append(f"<li>{inline_markdown(ordered_match.group(2))}</li>")
            i += 1
            continue

        if line.startswith("- "):
            if not state["list"]:
                close_blocks(out, state)
                out.append("<ul>")
                state["list"] = True
            out.append(f"<li>{inline_markdown(line[2:].strip())}</li>")
            i += 1
            continue

        close_blocks(out, state)

        if line.startswith("# "):
            title = line[2:].strip()
            out.append(f'<h1 id="{slugify(title)}">{inline_markdown(title)}</h1>')
        elif line.startswith("## "):
            title = line[3:].strip()
            out.append(f'<h2 id="{slugify(title)}">{inline_markdown(title)}</h2>')
        elif line.startswith("### "):
            title = line[4:].strip()
            out.append(f'<h3 id="{slugify(title)}">{inline_markdown(title)}</h3>')
        elif line.startswith("> "):
            out.append(f"<blockquote>{inline_markdown(line[2:].strip())}</blockquote>")
        elif line == "---":
            out.append("<hr>")
        else:
            out.append(f"<p>{inline_markdown(line)}</p>")
        i += 1

    if state["code"]:
        out.append("</code></pre>")
    close_blocks(out, state)
    return "\n".join(out)


def first_heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def collect_documents() -> list[Path]:
    order = [
        "README.md",
        "ban-do-homeschooling.md",
        "giao-trinh-homeschooling.md",
        "thuat-ngu-homeschooling.md",
        "cong-cu-thuc-hanh.md",
        "khung-nang-luc-va-rubric.md",
    ]
    docs = [ROOT / name for name in order if (ROOT / name).exists()]
    docs.extend(sorted(ROOT.glob("Module-*.md")))
    return docs


def main() -> None:
    docs = collect_documents()
    if not docs:
        raise SystemExit("Không tìm thấy file Markdown nguồn.")

    title = first_heading(ROOT / "README.md")
    modules = [path for path in docs if path.name.startswith("Module-")]
    nav = "\n".join(
        f'<a href="#{path.stem}"><span>{idx:02d}</span>{html.escape(first_heading(path))}</a>'
        for idx, path in enumerate(docs, start=1)
    )
    sections = "\n".join(
        f'<section class="lesson" id="{path.stem}">{markdown_to_html(path.read_text(encoding="utf-8"))}</section>'
        for path in docs
    )
    module_cards = "\n".join(
        f'<a class="module-card" href="#{path.stem}"><span>Module {idx:02d}</span><strong>{html.escape(first_heading(path))}</strong></a>'
        for idx, path in enumerate(modules, start=1)
    )

    html_doc = f"""<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="Nền tảng học tập chuyên sâu về homeschooling, triết lý giáo dục, phương pháp, vận hành và áp dụng tại Việt Nam.">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>
  <header class="topbar">
    <a class="brand" href="#top"><img class="brand-logo" src="assets/lumi-logo-2022.png" alt="Lumi"><span>Homeschooling Việt Nam</span></a>
    <nav aria-label="Liên kết nhanh">
      <a href="#ban-do-homeschooling">Bản đồ</a>
      <a href="#giao-trinh-homeschooling">Giáo trình</a>
      <a href="#thuat-ngu-homeschooling">Thuật ngữ</a>
      <a href="#Module-01-ban-chat-homeschooling">Module</a>
    </nav>
  </header>
  <div class="layout" id="top">
    <aside class="sidebar">
      <div class="sidebar-inner">
        <p class="eyebrow">Nền tảng học tập</p>
        <h2>Mục lục</h2>
        <div class="nav-list">{nav}</div>
      </div>
    </aside>
    <main>
      <section class="hero">
        <p class="eyebrow">Lý thuyết, mô hình và thực hành</p>
        <h1>{html.escape(title)}</h1>
        <p class="lede">Một giáo trình first-principles giúp phụ huynh và nhà giáo dục hiểu homeschooling như một hệ thống trách nhiệm: mục tiêu, trẻ em, chương trình, phương pháp, đánh giá, xã hội hóa, pháp lý và quản trị rủi ro tại Việt Nam.</p>
        <div class="stats">
          <span><strong>{len(modules)}</strong> module chuyên sâu</span>
          <span><strong>6</strong> tài liệu nền tảng</span>
          <span><strong>30</strong> hình ảnh trực quan</span>
          <span><strong>18/05/2026</strong> mốc cập nhật pháp lý</span>
        </div>
      </section>
      <section class="module-grid" aria-label="Danh sách module">{module_cards}</section>
      {sections}
    </main>
  </div>
</body>
</html>
"""
    (ROOT / "index.html").write_text(html_doc, encoding="utf-8")
    print(f"Đã tạo index.html từ {len(docs)} tài liệu Markdown.")


if __name__ == "__main__":
    main()
