import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="전략적으로 물어봐", layout="wide")
st.markdown(
    "<style>.block-container{padding:0;max-width:100%;} header{visibility:hidden;} footer{visibility:hidden;}</style>",
    unsafe_allow_html=True,
)

HTML_CONTENT = """<!doctype html>
<html lang="ko">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>전략적으로 물어봐</title>
<style>
  :root {
    --bg: #F5F4F2;
    --surface: #FFFFFF;
    --surface-2: #EDEBE7;
    --ink: #2A2724;
    --ink-2: #57534E;
    --muted: #837E77;
    --faint: #B2ADA5;
    --accent: #6B655D;
    --accent-strong: #47423D;
    --accent-ink: #FFFFFF;
    --accent-soft: #E7E4DF;
    --btn: #47423D;
    --btn-strong: #322E2A;
    --btn-ink: #FFFFFF;
    --line: #E2DFDA;
    --shadow-sm: 0 1px 2px rgba(40, 38, 34, 0.06);
    --shadow-md: 0 1px 2px rgba(40, 38, 34, 0.05), 0 10px 28px -14px rgba(40, 38, 34, 0.16);
    --good-soft: #E3ECE1;
    --good-strong: #3F6B3A;
    --caution-soft: #F4E3DA;
    --caution-strong: #9C4A2E;

    --font-display: -apple-system, BlinkMacSystemFont, "Segoe UI", "Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", "Hiragino Sans", "Yu Gothic", "Noto Sans JP", "PingFang SC", "Microsoft YaHei", "Noto Sans SC", ui-sans-serif, system-ui, sans-serif;
    --font-body: -apple-system, BlinkMacSystemFont, "Segoe UI", "Apple SD Gothic Neo", "Malgun Gothic", "Hiragino Sans", "Yu Gothic", "Noto Sans JP", "PingFang SC", "Microsoft YaHei", "Noto Sans SC", ui-sans-serif, system-ui, sans-serif;
    --font-mono: "Cascadia Code", "SF Mono", ui-monospace, Menlo, Consolas, monospace;

    --fs-micro: clamp(0.66rem, 0.63rem + 0.14vw, 0.72rem);
    --fs-small: clamp(0.78rem, 0.75rem + 0.14vw, 0.85rem);
    --fs-body: clamp(0.92rem, 0.89rem + 0.14vw, 0.98rem);
    --fs-lead: clamp(1rem, 0.95rem + 0.28vw, 1.08rem);
    --fs-h3: clamp(1.02rem, 0.96rem + 0.3vw, 1.14rem);
    --fs-h2: clamp(1.22rem, 1.08rem + 0.66vw, 1.5rem);
    --fs-h1: clamp(1.68rem, 1.32rem + 1.8vw, 2.5rem);
    --fs-wordmark: clamp(1.28rem, 1.18rem + 0.5vw, 1.6rem);
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #181715;
      --surface: #221F1C;
      --surface-2: #29261F;
      --ink: #EEECE8;
      --ink-2: #C9C5BE;
      --muted: #9A958D;
      --faint: #6E6961;
      --accent: #B5AFA5;
      --accent-strong: #D6D1C7;
      --accent-ink: #201E1B;
      --accent-soft: #322E28;
      --btn: #B5AFA5;
      --btn-strong: #D6D1C7;
      --btn-ink: #201E1B;
      --line: #322E29;
      --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.35);
      --shadow-md: 0 1px 2px rgba(0, 0, 0, 0.35), 0 10px 28px -14px rgba(0, 0, 0, 0.6);
      --good-soft: #26332A;
      --good-strong: #8FBF87;
      --caution-soft: #3A2A22;
      --caution-strong: #E2A688;
    }
  }
  :root[data-theme="dark"] {
    --bg: #181715;
    --surface: #221F1C;
    --surface-2: #29261F;
    --ink: #EEECE8;
    --ink-2: #C9C5BE;
    --muted: #9A958D;
    --faint: #6E6961;
    --accent: #B5AFA5;
    --accent-strong: #D6D1C7;
    --accent-ink: #201E1B;
    --accent-soft: #322E28;
    --btn: #B5AFA5;
    --btn-strong: #D6D1C7;
    --btn-ink: #201E1B;
    --line: #322E29;
    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.35);
    --shadow-md: 0 1px 2px rgba(0, 0, 0, 0.35), 0 10px 28px -14px rgba(0, 0, 0, 0.6);
    --good-soft: #26332A;
    --good-strong: #8FBF87;
    --caution-soft: #3A2A22;
    --caution-strong: #E2A688;
  }
  :root[data-theme="light"] {
    --bg: #F5F4F2;
    --surface: #FFFFFF;
    --surface-2: #EDEBE7;
    --ink: #2A2724;
    --ink-2: #57534E;
    --muted: #837E77;
    --faint: #B2ADA5;
    --accent: #6B655D;
    --accent-strong: #47423D;
    --accent-ink: #FFFFFF;
    --accent-soft: #E7E4DF;
    --btn: #47423D;
    --btn-strong: #322E2A;
    --btn-ink: #FFFFFF;
    --line: #E2DFDA;
    --shadow-sm: 0 1px 2px rgba(40, 38, 34, 0.06);
    --shadow-md: 0 1px 2px rgba(40, 38, 34, 0.05), 0 10px 28px -14px rgba(40, 38, 34, 0.16);
    --good-soft: #E3ECE1;
    --good-strong: #3F6B3A;
    --caution-soft: #F4E3DA;
    --caution-strong: #9C4A2E;
  }

  * { box-sizing: border-box; }
  html, body {
    margin: 0;
    padding: 0;
    background: var(--bg);
    color: var(--ink);
    overflow-x: hidden;
  }
  body {
    font-family: var(--font-body);
    font-size: var(--fs-body);
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    line-height: 1.65;
    letter-spacing: -0.006em;
    word-break: keep-all;
    overflow-wrap: break-word;
  }
  h1, h2, h3 {
    font-family: var(--font-display);
    font-weight: 700;
    letter-spacing: -0.015em;
    text-wrap: balance;
    margin: 0;
    color: var(--ink);
  }
  .tabular { font-variant-numeric: tabular-nums; font-family: var(--font-mono); }
  a { color: inherit; }
  ::selection { background: var(--accent-soft); color: var(--accent-strong); }

  .shell {
    max-width: 1040px;
    margin: 0 auto;
    padding: 0 24px 88px;
    position: relative;
  }
  .shell::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: -1;
    background-image:
      linear-gradient(color-mix(in srgb, var(--bg) 22%, transparent), color-mix(in srgb, var(--bg) 22%, transparent)),
      url("skin-products-different-recipients-composition_23-2148761457.avif");
    background-size: cover;
    background-position: center;
  }

  /* ---------- Header ---------- */
  header.top {
    position: sticky;
    top: 0;
    z-index: 10;
    background: var(--bg);
    border-bottom: 1px solid var(--line);
  }
  .top-inner {
    max-width: 1040px;
    margin: 0 auto;
    padding: 16px 24px;
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 16px;
    flex-wrap: wrap;
  }
  .brand-block { display: flex; flex-direction: column; gap: 2px; }
  .kicker {
    font-size: var(--fs-micro);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--faint);
  }
  .wordmark {
    font-family: var(--font-display);
    font-size: var(--fs-wordmark);
    font-weight: 800;
    letter-spacing: -0.02em;
    line-height: 1.1;
  }
  .wordmark em {
    font-style: normal;
    color: var(--accent);
  }
  .top-meta {
    display: flex;
    align-items: baseline;
    gap: 12px;
    color: var(--muted);
    font-size: var(--fs-small);
    font-variant-numeric: tabular-nums;
  }
  .top-meta .divider { color: var(--line); }

  .eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: var(--fs-micro);
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--accent);
    font-weight: 600;
    margin-bottom: 14px;
  }
  .eyebrow::before {
    content: "";
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: var(--accent);
    display: inline-block;
  }

  /* ---------- Hero (light, editorial) ---------- */
  .hero {
    background: var(--bg);
    padding: 56px 24px 40px;
    border-bottom: 1px solid var(--line);
  }
  .hero-inner {
    max-width: 1040px;
    margin: 0 auto;
  }
  .hero h1 {
    font-size: var(--fs-h1);
    max-width: 20ch;
    letter-spacing: -0.02em;
    line-height: 1.15;
  }
  .hero-headline {
    overflow: hidden;
    padding: 6px 0;
    margin: -6px 0;
  }
  #hero-headline-text {
    display: inline-block;
    font-weight: 700;
    transition: transform 0.35s cubic-bezier(.2,.8,.2,1), opacity 0.35s ease;
  }
  #hero-headline-text.is-out {
    transform: translateY(-14px);
    opacity: 0;
  }
  #hero-headline-text.is-in {
    transform: translateY(14px);
    opacity: 0;
  }
  .hero-rule {
    width: 40px;
    height: 2px;
    border-radius: 2px;
    background: var(--accent);
    margin: 22px 0;
  }
  .hero p {
    color: var(--ink-2);
    max-width: 58ch;
    margin: 0;
    font-size: var(--fs-lead);
    line-height: 1.7;
  }

  /* ---------- Section shell ---------- */
  section.block { margin-top: 56px; }
  .block-head {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 20px;
    flex-wrap: wrap;
  }
  .block-head h2 { font-size: var(--fs-h2); letter-spacing: -0.012em; }
  .block-head .sub { color: var(--muted); font-size: var(--fs-small); margin-top: 5px; }
  .count-tag {
    font-size: var(--fs-micro);
    letter-spacing: 0.02em;
    color: var(--muted);
    background: var(--surface-2);
    border: 1px solid var(--line);
    padding: 4px 11px;
    border-radius: 999px;
    white-space: nowrap;
  }

  /* ---------- Country trend rail ---------- */
  .rail {
    display: flex;
    gap: 14px;
    overflow-x: auto;
    padding-bottom: 6px;
    margin: 0 -24px;
    padding-left: 24px;
    padding-right: 24px;
    scroll-snap-type: x proximity;
  }
  .country-card {
    scroll-snap-align: start;
    flex: 0 0 268px;
    display: flex;
    flex-direction: column;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 16px;
    overflow: hidden;
    box-shadow: var(--shadow-md);
    transition: transform 0.18s cubic-bezier(.2,.8,.2,1), border-color 0.18s ease;
  }
  .country-card { cursor: pointer; }
  .country-card:hover { transform: translateY(-3px); border-color: color-mix(in srgb, var(--accent) 40%, var(--line)); }
  .country-card:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
  .country-media {
    flex: none;
    height: 84px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, var(--accent) 0%, var(--btn) 100%);
    color: #fff;
    font-family: var(--font-display);
    font-weight: 700;
    font-size: 1.5rem;
    letter-spacing: 0.1em;
  }
  .country-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 18px 20px 18px;
  }
  .country-card .region {
    font-size: var(--fs-micro);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--faint);
    font-weight: 600;
  }
  .country-card h3 {
    font-size: var(--fs-h3);
    margin-top: 10px;
    line-height: 1.4;
    letter-spacing: -0.008em;
  }
  .country-card p {
    font-size: var(--fs-small);
    color: var(--muted);
    margin: 11px 0 0;
    line-height: 1.6;
  }
  .country-card .src {
    margin-top: auto;
    padding-top: 11px;
    font-size: var(--fs-micro);
    color: var(--accent);
    border-top: 1px solid var(--line);
  }

  /* ---------- Ingredient chips ---------- */
  .chip-grid {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .chip-card {
    display: flex;
    align-items: center;
    gap: 14px;
    width: 100%;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 13px;
    padding: 13px 17px;
    cursor: pointer;
    transition: border-color 0.16s ease, transform 0.16s cubic-bezier(.2,.8,.2,1), box-shadow 0.16s ease;
    text-align: left;
    font: inherit;
    color: inherit;
    box-shadow: var(--shadow-sm);
  }
  .chip-card:hover { border-color: color-mix(in srgb, var(--accent) 45%, var(--line)); transform: translateY(-2px); }
  .chip-card:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
  }
  .chip-card.active {
    border-color: var(--accent);
    background: var(--accent-soft);
    box-shadow: var(--shadow-md);
  }
  .chip-rank {
    flex: none;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-display);
    font-weight: 700;
    font-size: var(--fs-small);
    background: var(--accent-soft);
    color: var(--accent-strong);
  }
  .chip-card:nth-child(-n+3) .chip-rank {
    background: var(--btn);
    color: var(--btn-ink);
  }
  .chip-main { flex: 1; min-width: 0; }
  .chip-card .name {
    font-weight: 600;
    font-size: var(--fs-body);
    letter-spacing: -0.006em;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
  }
  .chip-card .delta {
    font-size: var(--fs-micro);
    color: var(--accent-strong);
    font-weight: 700;
  }
  .chip-card .desc {
    font-size: var(--fs-small);
    color: var(--muted);
    margin-top: 4px;
    line-height: 1.55;
  }

  /* ---------- Ingredient detail panel ---------- */
  .detail-panel {
    margin-top: 14px;
    background: var(--surface);
    border: 1px solid var(--accent);
    border-radius: 16px;
    padding: 22px 24px;
    box-shadow: var(--shadow-md);
    display: none;
  }
  .detail-panel.open { display: block; }
  .detail-head {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 16px;
  }
  .detail-titles .std-tag {
    font-size: var(--fs-micro);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
    font-weight: 700;
  }
  .detail-titles h3 {
    font-size: var(--fs-h2);
    margin-top: 6px;
    letter-spacing: -0.012em;
  }
  .detail-titles .eng {
    color: var(--muted);
    font-size: var(--fs-small);
    margin-top: 4px;
  }
  .detail-close {
    flex: none;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    border: 1px solid var(--line);
    background: var(--surface-2);
    color: var(--muted);
    cursor: pointer;
    font-size: 1rem;
    line-height: 1;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .detail-close:hover { color: var(--btn-ink); background: var(--btn); border-color: var(--btn); }
  .detail-close:focus-visible { outline: 2px solid var(--btn); outline-offset: 2px; }

  .detail-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 16px;
    padding: 14px 0;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
  }
  .detail-meta div { min-width: 140px; }
  .detail-meta .label {
    font-size: var(--fs-micro);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--faint);
  }
  .detail-meta .value {
    margin-top: 4px;
    font-size: var(--fs-body);
    font-family: var(--font-mono);
    font-variant-numeric: tabular-nums;
  }

  .detail-body { margin-top: 16px; }
  .detail-body .label {
    font-size: var(--fs-micro);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--faint);
    margin-bottom: 6px;
  }
  .detail-body p {
    font-size: var(--fs-body);
    color: var(--ink-2);
    line-height: 1.7;
    margin: 0;
  }
  .purpose-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 8px;
  }
  .combo-good-tag {
    display: inline-block;
    font-size: var(--fs-micro);
    background: var(--good-soft);
    color: var(--good-strong);
    padding: 3px 10px;
    border-radius: 999px;
    font-weight: 600;
  }
  .combo-caution-tag {
    display: inline-block;
    font-size: var(--fs-micro);
    background: var(--caution-soft);
    color: var(--caution-strong);
    padding: 3px 10px;
    border-radius: 999px;
    font-weight: 600;
  }
  .caution-note {
    margin-top: 8px;
    font-size: var(--fs-small);
    color: var(--muted);
    line-height: 1.6;
  }

  .detail-foot {
    margin-top: 18px;
    padding-top: 14px;
    border-top: 1px solid var(--line);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
  }
  .detail-foot .src-note {
    font-size: var(--fs-micro);
    color: var(--faint);
  }
  .kcia-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: var(--fs-small);
    font-weight: 600;
    color: var(--btn);
    text-decoration: none;
    border-bottom: 1px solid color-mix(in srgb, var(--btn) 50%, transparent);
    padding-bottom: 1px;
  }
  .kcia-link:hover { color: var(--btn-strong); border-color: var(--btn-strong); }

  /* ---------- Competitor table ---------- */
  .table-toolbar {
    display: flex;
    gap: 10px;
    align-items: center;
    margin-bottom: 14px;
    flex-wrap: wrap;
  }
  .search-box {
    flex: 1 1 240px;
    display: flex;
    align-items: center;
    gap: 9px;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 10px 13px;
    transition: border-color 0.16s ease, box-shadow 0.16s ease;
  }
  .search-box:focus-within {
    border-color: var(--accent);
    box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 16%, transparent);
  }
  .search-box svg { flex: none; color: var(--faint); }
  .search-box input {
    border: none;
    outline: none;
    background: transparent;
    color: var(--ink);
    font-size: var(--fs-small);
    width: 100%;
    font-family: var(--font-body);
  }
  .search-box input::placeholder { color: var(--faint); }
  .reset-btn {
    font-size: var(--fs-small);
    font-weight: 600;
    color: var(--btn-ink);
    background: var(--btn);
    border: 1px solid var(--btn);
    border-radius: 10px;
    padding: 10px 16px;
    cursor: pointer;
    font-family: var(--font-body);
    transition: background-color 0.16s ease, border-color 0.16s ease, transform 0.16s ease;
  }
  .reset-btn:hover { background: var(--btn-strong); border-color: var(--btn-strong); transform: translateY(-1px); }
  .reset-btn:focus-visible { outline: 2px solid var(--btn); outline-offset: 2px; }

  .concept-tag {
    display: inline-block;
    font-size: var(--fs-micro);
    background: var(--accent-soft);
    color: var(--accent-strong);
    padding: 3px 10px;
    border-radius: 999px;
    font-weight: 600;
  }

  /* ---------- Product grid ---------- */
  .product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 14px;
  }
  .empty-state {
    grid-column: 1 / -1;
    text-align: center;
    color: var(--muted);
    padding: 36px 16px;
    font-size: var(--fs-body);
  }
  .product-card {
    display: flex;
    flex-direction: row;
    align-items: stretch;
    text-align: left;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 14px;
    overflow: hidden;
    cursor: pointer;
    font: inherit;
    color: inherit;
    box-shadow: var(--shadow-sm);
    transition: transform 0.16s cubic-bezier(.2,.8,.2,1), border-color 0.16s ease, box-shadow 0.16s ease;
  }
  .product-card:hover {
    transform: translateY(-2px);
    border-color: color-mix(in srgb, var(--accent) 45%, var(--line));
    box-shadow: var(--shadow-md);
  }
  .product-card:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
  .product-card-media {
    flex: none;
    width: 104px;
    background: var(--accent-soft);
    color: var(--accent-strong);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .product-card-media svg { width: 34px; height: 34px; }
  .product-tile {
    flex: none;
    width: 52px;
    height: 52px;
    border-radius: 10px;
    background: var(--accent-soft);
    color: var(--accent-strong);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .product-tile svg { width: 60%; height: 60%; }
  .product-card-body {
    min-width: 0;
    flex: 1;
    padding: 14px 16px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .product-card-body .brand-name {
    font-size: var(--fs-micro);
    color: var(--muted);
  }
  .product-card-body .product-name {
    font-weight: 600;
    font-size: var(--fs-body);
    letter-spacing: -0.006em;
    line-height: 1.4;
    margin-top: 2px;
  }
  .product-card-body .rank-preview {
    margin-top: 8px;
    font-size: var(--fs-micro);
    color: var(--accent-strong);
  }

  /* ---------- Product detail modal ---------- */
  .modal-backdrop {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(10, 12, 14, 0.5);
    backdrop-filter: blur(3px);
    align-items: center;
    justify-content: center;
    padding: 20px;
    z-index: 100;
  }
  .modal-backdrop.open { display: flex; }
  .product-modal {
    position: relative;
    width: 100%;
    max-width: 560px;
    max-height: 86vh;
    overflow-y: auto;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 26px;
    box-shadow: var(--shadow-md);
  }
  .modal-close { position: absolute; top: 18px; right: 18px; }
  .modal-top {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    padding-right: 30px;
  }
  .modal-top .product-tile {
    width: 72px;
    height: 72px;
    border-radius: 14px;
    font-size: 1.3rem;
  }
  .modal-country-tile {
    flex: none;
    width: 72px;
    height: 72px;
    border-radius: 14px;
    background: linear-gradient(135deg, var(--accent) 0%, var(--btn) 100%);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-display);
    font-weight: 700;
    font-size: 1.3rem;
    letter-spacing: 0.1em;
  }
  .modal-titles .std-tag {
    font-size: var(--fs-micro);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
    font-weight: 700;
  }
  .modal-titles h3 {
    font-size: var(--fs-h2);
    margin-top: 6px;
    letter-spacing: -0.012em;
  }
  .modal-brand {
    color: var(--muted);
    font-size: var(--fs-small);
    margin-top: 3px;
  }
  .modal-rank {
    display: inline-block;
    margin-top: 10px;
    font-size: var(--fs-micro);
    background: var(--accent-soft);
    color: var(--accent-strong);
    padding: 4px 10px;
    border-radius: 999px;
    font-weight: 600;
  }
  .review-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 8px;
  }
  .review-item {
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 12px 14px;
    background: var(--surface-2);
  }
  .review-item .review-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    margin-bottom: 5px;
  }
  .review-item .stars {
    color: var(--btn);
    font-size: var(--fs-small);
    letter-spacing: 1px;
  }
  .review-item .skin-tag {
    font-size: var(--fs-micro);
    color: var(--faint);
  }
  .review-item p {
    font-size: var(--fs-small);
    color: var(--ink-2);
    line-height: 1.6;
    margin: 0;
  }

  footer.note {
    margin-top: 52px;
    padding-top: 22px;
    border-top: 1px solid var(--line);
    color: var(--faint);
    font-size: var(--fs-small);
    line-height: 1.6;
  }

  /* ---------- Cursor text highlight ---------- */
  .hero p,
  .country-content p,
  .detail-body p,
  .review-item p,
  footer.note {
    padding: 2px 6px;
    border-radius: 6px;
    transition: background-color 0.15s ease;
  }
  .hero p:hover,
  .country-content p:hover,
  .detail-body p:hover,
  .review-item p:hover,
  footer.note:hover {
    background-color: var(--accent-soft);
  }

  @media (max-width: 640px) {
    .shell { padding: 0 16px 64px; }
    .top-inner { padding: 13px 16px; }
    .hero { padding: 44px 16px 36px; }
    .rail { margin: 0 -16px; padding-left: 16px; padding-right: 16px; }
    .country-card { flex-basis: 224px; }
  }

  @media (prefers-reduced-motion: reduce) {
    .chip-card, .country-card, .reset-btn, .search-box, .product-card { transition: none; }
    .hero p, .country-content p, .detail-body p, .review-item p, footer.note { transition: none; }
    #hero-headline-text { transition: none; }
  }
</style>
</head>
<body>

<header class="top">
  <div class="top-inner">
    <div class="brand-block">
      <span class="kicker">Cosmax Strategic Intelligence</span>
      <div class="wordmark">전략적으로 <em>물어봐</em></div>
    </div>
    <div class="top-meta">
      <span>2026.07.07 TUE</span>
      <span class="divider">·</span>
      <span>전략마케팅팀 아침 브리핑</span>
    </div>
  </div>
</header>

<section class="hero">
  <div class="hero-inner">
    <div class="eyebrow">Daily Intelligence</div>
    <h1 class="hero-headline"><span id="hero-headline-text">오늘, 뷰티 시장에서 알아야 할 것들</span></h1>
    <div class="hero-rule"></div>
    <p>국가별 트렌드, 뜨는 성분, 성분별 인기 브랜드 제품을 한 화면에서 확인하세요. 아래 성분을 클릭하면 관련 제품만 걸러볼 수 있습니다.</p>
  </div>
</section>

<div class="shell">
  <section class="block" id="trends">
    <div class="block-head">
      <div>
        <h2>국가별 트렌드</h2>
        <div class="sub">지난 24시간, 주요 시장에서 포착된 신호</div>
      </div>
      <span class="count-tag">5개 지역</span>
    </div>
    <div class="rail">
      <article class="country-card" data-country="KR" tabindex="0" role="button" aria-haspopup="dialog">
        <div class="country-media">KR</div>
        <div class="country-content">
          <div class="region">한국</div>
          <h3>저자극 · 맨살 화장 열풍 지속</h3>
          <p>피부 장벽 강화를 내세운 "스킨 배리어" 라인 검색량 전주 대비 상승. 무기자차 재조명.</p>
          <div class="src">출처: 올리브영 트렌드 리포트 · 클릭하면 관련 기사를 볼 수 있어요</div>
        </div>
      </article>
      <article class="country-card" data-country="US" tabindex="0" role="button" aria-haspopup="dialog">
        <div class="country-media">US</div>
        <div class="country-content">
          <div class="region">미국</div>
          <h3>더마 코스메틱, 매스 채널로 확장</h3>
          <p>피부과 처방 성분(레티놀, 아젤라산)을 담은 매스 브랜드 신제품이 잇따라 출시.</p>
          <div class="src">출처: Cosmetics Business · 클릭하면 관련 기사를 볼 수 있어요</div>
        </div>
      </article>
      <article class="country-card" data-country="JP" tabindex="0" role="button" aria-haspopup="dialog">
        <div class="country-media">JP</div>
        <div class="country-content">
          <div class="region">일본</div>
          <h3>두피 스킨케어 카테고리 성장</h3>
          <p>"두피도 피부"라는 메시지로 헤어 제품이 스킨케어 성분(세라마이드 등)을 차용.</p>
          <div class="src">출처: MAQUIA ONLINE · 클릭하면 관련 기사를 볼 수 있어요</div>
        </div>
      </article>
      <article class="country-card" data-country="FR" tabindex="0" role="button" aria-haspopup="dialog">
        <div class="country-media">FR</div>
        <div class="country-content">
          <div class="region">프랑스</div>
          <h3>저용량 · 고순도 포뮬러 선호</h3>
          <p>성분 수를 줄인 "미니멀 포뮬러"가 클린 뷰티의 다음 단계로 언급되는 빈도 증가.</p>
          <div class="src">출처: Demain Beauty · 클릭하면 관련 기사를 볼 수 있어요</div>
        </div>
      </article>
      <article class="country-card" data-country="CN" tabindex="0" role="button" aria-haspopup="dialog">
        <div class="country-media">CN</div>
        <div class="country-content">
          <div class="region">중국</div>
          <h3>기능성 원료 국산화 가속</h3>
          <p>자국산 발효 원료·펩타이드 소재를 강조하는 브랜드 라인업이 빠르게 늘어나는 추세.</p>
          <div class="src">출처: CBNData · 클릭하면 관련 기사를 볼 수 있어요</div>
        </div>
      </article>
    </div>
  </section>

  <section class="block" id="ingredients">
    <div class="block-head">
      <div>
        <h2>요즘 뜨는 성분 랭킹</h2>
        <div class="sub">전주 대비 검색량 증가율 기준 · 클릭하면 대한화장품협회 성분사전 정보와, 아래 관련 브랜드 제품을 함께 볼 수 있어요</div>
      </div>
      <span class="count-tag" id="ingredient-count">TOP 10</span>
    </div>
    <div class="chip-grid" id="chip-grid">
    </div>

    <div class="detail-panel" id="detail-panel">
      <div class="detail-head">
        <div class="detail-titles">
          <div class="std-tag">KCIA 표준 성분명</div>
          <h3 id="detail-name"></h3>
          <div class="eng" id="detail-eng"></div>
        </div>
        <button class="detail-close" id="detail-close" type="button" aria-label="상세 정보 닫기">&times;</button>
      </div>

      <div class="detail-meta">
        <div>
          <div class="label">CAS No.</div>
          <div class="value tabular" id="detail-cas"></div>
        </div>
        <div>
          <div class="label">성분코드</div>
          <div class="value tabular" id="detail-code"></div>
        </div>
      </div>

      <div class="detail-body">
        <div class="label">기원 및 정의</div>
        <p id="detail-definition"></p>
      </div>

      <div class="detail-body">
        <div class="label">배합목적</div>
        <div class="purpose-tags" id="detail-purposes"></div>
      </div>

      <div class="detail-body">
        <div class="label">추천 배합 조합</div>
        <div class="purpose-tags" id="detail-good-combo"></div>
      </div>

      <div class="detail-body">
        <div class="label">배합 시 주의가 필요한 조합</div>
        <div class="purpose-tags" id="detail-caution-combo"></div>
        <p class="caution-note" id="detail-caution-note"></p>
      </div>

      <div class="detail-body">
        <div class="label">추천 피부 타입</div>
        <div class="purpose-tags" id="detail-skin-types"></div>
      </div>

      <div class="detail-foot">
        <span class="src-note">출처: 대한화장품협회(KCIA) 화장품성분사전</span>
        <a class="kcia-link" id="detail-link" href="#" target="_blank" rel="noopener">
          성분사전 원문 보기 →
        </a>
      </div>
    </div>
  </section>

  <section class="block" id="competitors">
    <div class="block-head">
      <div>
        <h2>성분별 인기 브랜드 제품</h2>
        <div class="sub">성분당 실제 판매 중인 제품 3개 · 클릭하면 소개·랭킹·리뷰를 볼 수 있어요</div>
      </div>
      <span class="count-tag tabular" id="row-count">18건</span>
    </div>

    <div class="table-toolbar">
      <label class="search-box">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
          <circle cx="7" cy="7" r="5.25" stroke="currentColor" stroke-width="1.4"></circle>
          <path d="M11 11L14 14" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"></path>
        </svg>
        <input id="search-input" type="text" placeholder="브랜드, 제품명으로 검색" aria-label="브랜드 제품 검색" />
      </label>
      <button class="reset-btn" id="reset-btn" type="button">필터 초기화</button>
    </div>

    <div class="product-grid" id="product-grid">
    </div>
  </section>

  <footer class="note">
    성분별 브랜드 제품은 올리브영에서 실제 판매 중인 제품명을 기준으로 정리했습니다. 랭킹·평점 중 일부(토리든, 아이소이)는 공개된 실제 수치이며, 그 외 랭킹 표기와 리뷰 3개는 화면 구성을 보여주기 위한 예시입니다. 실제 서비스에서는 올리브영 데이터를 실시간 연동합니다.
  </footer>
</div>

<div class="modal-backdrop" id="product-modal-backdrop">
  <div class="product-modal" id="product-modal" role="dialog" aria-modal="true" aria-labelledby="modal-product-name">
    <button class="detail-close modal-close" id="modal-close" type="button" aria-label="제품 정보 닫기">&times;</button>
    <div class="modal-top">
      <div class="product-tile" id="modal-tile"></div>
      <div class="modal-titles">
        <div class="std-tag" id="modal-ingredient-tag"></div>
        <h3 id="modal-product-name"></h3>
        <div class="modal-brand" id="modal-brand"></div>
        <div class="modal-rank" id="modal-rank"></div>
      </div>
    </div>

    <div class="detail-body">
      <div class="label">제품 소개</div>
      <p id="modal-intro"></p>
    </div>

    <div class="detail-body">
      <div class="label">리뷰 3개 (예시)</div>
      <div class="review-list" id="modal-reviews"></div>
    </div>
  </div>
</div>

<div class="modal-backdrop" id="trend-modal-backdrop">
  <div class="product-modal" id="trend-modal" role="dialog" aria-modal="true" aria-labelledby="trend-title">
    <button class="detail-close modal-close" id="trend-modal-close" type="button" aria-label="트렌드 기사 닫기">&times;</button>
    <div class="modal-top">
      <div class="modal-country-tile" id="trend-region-tag"></div>
      <div class="modal-titles">
        <div class="std-tag" id="trend-source"></div>
        <h3 id="trend-title"></h3>
      </div>
    </div>

    <div class="detail-body">
      <div class="label">기사 핵심 내용</div>
      <p id="trend-summary"></p>
    </div>

    <div class="detail-foot">
      <span class="src-note">실제 보도된 기사 링크입니다</span>
      <a class="kcia-link" id="trend-link" href="#" target="_blank" rel="noopener">
        원문 기사 보기 →
      </a>
    </div>
  </div>
</div>

<script>
  (function () {
    // 출처: 대한화장품협회(KCIA) 화장품성분사전 https://kcia.or.kr/cid/main/
    var ingredients = [
      {
        name: "시카(병풀추출물)",
        stdName: "병풀추출물",
        engName: "Centella Asiatica Extract",
        cas: "84696-21-9",
        code: "540",
        definition: "병풀(Centella asiatica)의 전초에서 추출한 것.",
        purposes: ["피부컨디셔닝제"],
        url: "https://kcia.or.kr/cid/search/ingd_view.php?no=540",
        delta: "+18%",
        desc: "진정 · 장벽 강화 클레임과 함께 재조명",
        goodWith: ["판테놀", "세라마이드", "히알루론산"],
        avoidWith: ["고농도 각질케어산(AHA/BHA)", "고농도 레티놀"],
        avoidNote: "피부 장벽이 약해졌을 때 자극적인 각질케어 성분과 동시에 쓰면 진정 효과가 상쇄될 수 있어요.",
        skinTypes: ["민감성", "트러블성", "복합성"]
      },
      {
        name: "나이아신아마이드",
        stdName: "나이아신아마이드",
        engName: "Niacinamide",
        cas: "98-92-0",
        code: "1941",
        definition: "헤테로고리 방향족 아마이드 구조를 가진 성분(비타민 B3 계열). 국내에서는 기능성화장품 고시 성분으로 분류된다.",
        purposes: ["헤어컨디셔닝제", "피부컨디셔닝제(기타)"],
        url: "https://kcia.or.kr/cid/search/ingd_view.php?no=1941",
        delta: "+12%",
        desc: "톤업 · 모공 케어 스테디셀러로 자리잡음",
        goodWith: ["히알루론산", "판테놀", "펩타이드", "세라마이드"],
        avoidWith: ["고농도 순수 비타민C(아스코르빅애씨드)"],
        avoidNote: "낮은 pH의 고농도 순수 비타민C와 함께 쓰면 두 성분의 효과가 서로 떨어질 수 있어 시간차를 두는 게 좋아요.",
        skinTypes: ["지성", "복합성", "모공·톤 케어가 필요한 피부"]
      },
      {
        name: "펩타이드",
        stdName: "에스에이치-올리고펩타이드-1",
        engName: "sh-Oligopeptide-1",
        cas: "표기 없음",
        code: "7534",
        definition: "대장균에서 발효하여 얻은 단일사슬 재조합 휴먼 펩타이드. 상피세포성장인자(EGF)를 코딩하는 사람 유전자와 동일한 코드로 합성했으며, 국내 배합한도는 0.001%.",
        purposes: ["피부컨디셔닝제(기타)"],
        url: "https://kcia.or.kr/cid/search/ingd_view.php?no=7534",
        delta: "+24%",
        desc: "성장인자 계열 펩타이드로 안티에이징 라인 확장",
        goodWith: ["히알루론산", "나이아신아마이드", "세라마이드"],
        avoidWith: ["고농도 각질케어산(AHA/BHA)", "레티놀"],
        avoidNote: "펩타이드는 단백질 구조라 강한 산성 성분과 함께 쓰면 구조가 깨져 효과가 떨어질 수 있어요.",
        skinTypes: ["건성", "탄력 저하 피부", "노화 케어가 필요한 피부"]
      },
      {
        name: "판테놀",
        stdName: "판테놀",
        engName: "Panthenol",
        cas: "81-13-0 (D-Form) / 16485-10-2",
        code: "3528",
        definition: "판토테닉애씨드(비타민 B5) 유도체 알코올. D-판테놀은 점성 오일, DL-판테놀은 크림상 백색 결정 분말 형태다.",
        purposes: ["헤어컨디셔닝제", "용제", "피부컨디셔닝제(보습제)"],
        url: "https://kcia.or.kr/cid/search/ingd_view.php?no=3528",
        delta: "+9%",
        desc: "저자극 라인의 기본 진정 성분으로 채택 증가",
        goodWith: ["시카(병풀추출물)", "히알루론산", "세라마이드", "대부분의 성분"],
        avoidWith: [],
        avoidNote: "자극이 거의 없는 만능 진정·보습 성분이라 배합 제한이 크지 않아요.",
        skinTypes: ["모든 피부 타입", "건성", "민감성"]
      },
      {
        name: "프로바이오틱스",
        stdName: "락토바실러스/쌀겨발효여과물",
        engName: "Lactobacillus/Rice Bran Ferment Filtrate",
        cas: "표기 없음",
        code: "10000",
        definition: "미생물 Lactobacillus로 쌀(Oryza sativa) 겨를 발효하여 얻은 생성물을 여과한 것. 발효 유래 성분으로 마이크로바이옴 컨셉 제품에 주로 사용된다.",
        purposes: ["산화방지제", "피부컨디셔닝제(기타)"],
        url: "https://kcia.or.kr/cid/search/ingd_view.php?no=10000",
        delta: "+15%",
        desc: "피부 마이크로바이옴 밸런싱 컨셉과 결합",
        goodWith: ["판테놀", "세라마이드", "히알루론산"],
        avoidWith: ["고농도 알코올", "벤조일퍼옥사이드 등 강한 항균 성분"],
        avoidNote: "강한 항균·살균 성분과 함께 쓰면 유익균과 발효 성분의 밸런싱 효과가 상쇄될 수 있어요.",
        skinTypes: ["민감성", "건성", "피부 장벽이 약한 피부"]
      },
      {
        name: "히알루론산",
        stdName: "소듐하이알루로네이트",
        engName: "Sodium Hyaluronate",
        cas: "9067-32-7",
        code: "1265",
        definition: "하이알루로닉애씨드의 소듐염. 다중 분자량으로 정제해 보습 지속력과 흡수 속도를 차별화하는 데 주로 쓰인다.",
        purposes: ["피부컨디셔닝제"],
        url: "https://kcia.or.kr/cid/search/ingd_view.php?no=1265",
        delta: "+7%",
        desc: "다중 분자량 조합으로 보습 차별화",
        goodWith: ["나이아신아마이드", "펩타이드", "세라마이드", "비타민C"],
        avoidWith: [],
        avoidNote: "건조한 환경에서 보습 크림 없이 단독 사용하면 오히려 피부 속 수분을 끌어올려 날려버릴 수 있어 유수분 크림과 함께 쓰는 걸 추천해요.",
        skinTypes: ["모든 피부 타입", "건성", "수분 부족형 지성"]
      },
      {
        name: "아젤라익애씨드",
        stdName: "아젤라익애씨드",
        engName: "Azelaic Acid",
        cas: "123-99-9",
        code: "-",
        definition: "곡물 발효 또는 합성으로 제조되는 디카르복실산 계열 성분. 피지 조절과 색소 침착 개선 목적으로 사용된다.",
        purposes: ["피부컨디셔닝제", "피지조절제"],
        url: "https://kcia.or.kr/cid/search/ingd_list.php",
        delta: "+21%",
        desc: "미국發 트러블·색소 케어 처방 성분, 매스 채널로 확산",
        goodWith: ["나이아신아마이드", "히알루론산", "판테놀"],
        avoidWith: ["고농도 순수 비타민C(아스코르빅애씨드)", "강한 물리적 각질제거"],
        avoidNote: "산성도가 있는 성분이라 강한 산성 성분과 겹치면 자극이 커질 수 있어, 사용 시간을 나눠 쓰는 게 좋아요.",
        skinTypes: ["지성", "트러블성", "색소침착 고민 피부"]
      },
      {
        name: "레티놀",
        stdName: "레티놀",
        engName: "Retinol",
        cas: "68-26-8",
        code: "-",
        definition: "비타민 A 유도체로, 피부 재생 주기를 촉진해 주름·탄력·모공 케어에 널리 쓰이는 성분.",
        purposes: ["피부컨디셔닝제(기타)"],
        url: "https://kcia.or.kr/cid/search/ingd_list.php",
        delta: "+16%",
        desc: "저자극 캡슐화 기술 발전으로 매스 라인까지 확대",
        goodWith: ["히알루론산", "판테놀", "세라마이드"],
        avoidWith: ["고농도 각질케어산(AHA/BHA)", "벤조일퍼옥사이드"],
        avoidNote: "동시 사용 시 자극이 배가될 수 있어 최소 하루 텀을 두고 번갈아 사용하는 걸 추천해요.",
        skinTypes: ["복합성", "노화 케어가 필요한 피부", "모공 케어가 필요한 피부"]
      },
      {
        name: "아데노신",
        stdName: "아데노신",
        engName: "Adenosine",
        cas: "58-61-7",
        code: "-",
        definition: "뉴클레오사이드 계열 성분으로, 국내에서는 주름 개선 기능성화장품 고시 원료로 사용된다.",
        purposes: ["피부컨디셔닝제(기타)"],
        url: "https://kcia.or.kr/cid/search/ingd_list.php",
        delta: "+11%",
        desc: "국내 주름 개선 기능성 고시 성분으로 스테디한 수요",
        goodWith: ["히알루론산", "나이아신아마이드", "펩타이드"],
        avoidWith: [],
        avoidNote: "자극이 적어 다른 기능성 성분과 무난하게 함께 사용할 수 있어요.",
        skinTypes: ["모든 피부 타입", "노화 케어가 필요한 피부"]
      },
      {
        name: "PDRN",
        stdName: "폴리데옥시리보뉴클레오타이드나트륨",
        engName: "Sodium DNA",
        cas: "표기 없음",
        code: "-",
        definition: "연어·송어 등의 생식세포에서 추출한 DNA 유래 성분. 피부 재생과 상처 회복 관련 연구로 주목받고 있다.",
        purposes: ["피부컨디셔닝제(기타)"],
        url: "https://kcia.or.kr/cid/search/ingd_list.php",
        delta: "+27%",
        desc: "재생·탄력 앰플 라인에서 가장 빠르게 성장하는 성분",
        goodWith: ["히알루론산", "펩타이드", "판테놀"],
        avoidWith: ["고농도 각질케어산(AHA/BHA)"],
        avoidNote: "핵산 성분이라 강한 산성 환경에서는 안정성이 떨어질 수 있어요.",
        skinTypes: ["건성", "탄력 저하 피부", "재생 케어가 필요한 피부"]
      }
    ];

    // 출처: 올리브영(oliveyoung.co.kr) 공개 상품 정보. 브랜드·제품명은 실제 판매 상품 기준.
    // 랭킹 중 토리든·아이소이 항목은 공개된 실제 수치(글로우픽/올리브영 어워즈)이며, 그 외 랭킹 문구와 리뷰 3개는 화면 구성을 보여주기 위한 예시입니다.
    var products = [
      {
        brand: "라로슈포제", product: "시카플라스트 멀티 리페어 크림", ingredient: "시카(병풀추출물)",
        price: "약 29,000원 (100ml)", rank: "진정크림 스테디셀러",
        intro: "병풀추출물과 시카필름 성분을 담아 자극받은 피부를 진정시키고 장벽을 채워주는 멀티 리페어 크림입니다.",
        reviews: [
          { stars: "★★★★★", tag: "건성 · 30대", text: "환절기마다 각질 일어날 때 발라주면 확실히 진정되는 느낌이에요." },
          { stars: "★★★★☆", tag: "민감성 · 20대", text: "자극 없이 순한데 향이 약간 병원 냄새 같아서 호불호 있을 듯." },
          { stars: "★★★★★", tag: "복합성 · 40대", text: "레이저 시술 후 진정용으로 쓰는데 재구매만 세 번째예요." }
        ]
      },
      {
        brand: "닥터자르트", product: "시카페어 인텐시브 수딩 리페어 크림", ingredient: "시카(병풀추출물)",
        price: "약 38,000원 (50ml)", rank: "올영 강력진정 카테고리 인기 상품",
        intro: "고농축 시카 콤플렉스로 자극과 붉은기를 빠르게 가라앉히는 강력 진정 크림입니다.",
        reviews: [
          { stars: "★★★★★", tag: "지성 · 20대", text: "피부과 시술 다음날 발랐더니 붉은기가 확실히 덜했어요." },
          { stars: "★★★★☆", tag: "건성 · 30대", text: "진정 효과는 좋은데 겨울엔 보습이 살짝 부족한 느낌." },
          { stars: "★★★★★", tag: "민감성 · 20대", text: "트러블 올라올 때 부분적으로 발라주면 금방 가라앉아요." }
        ]
      },
      {
        brand: "이니스프리", product: "레티놀 시카 모공 흔적 앰플", ingredient: "시카(병풀추출물)",
        price: "약 21,000원 (30ml)", rank: "스킨케어 베스트 상품",
        intro: "레티놀과 시카를 함께 담아 모공과 흔적 케어, 진정을 동시에 노리는 앰플입니다.",
        reviews: [
          { stars: "★★★★☆", tag: "지성 · 20대", text: "레티놀 처음 써보는데 자극 없이 순하게 적응됐어요." },
          { stars: "★★★★★", tag: "복합성 · 30대", text: "모공이 눈에 띄게 조밀해진 느낌, 꾸준히 쓰는 중." },
          { stars: "★★★☆☆", tag: "건성 · 20대", text: "효과는 있는데 저는 살짝 건조해서 로션 더 발라줘요." }
        ]
      },
      {
        brand: "더마팩토리", product: "나이아신아마이드 20% 세럼", ingredient: "나이아신아마이드",
        price: "약 12,000원 (30ml)", rank: "고농도 나이아신아마이드 라인 대표 상품",
        intro: "고농도 20% 나이아신아마이드로 톤 균일화와 모공 케어를 노린 가성비 세럼입니다.",
        reviews: [
          { stars: "★★★★★", tag: "지성 · 20대", text: "가격 대비 톤업 효과 확실해서 계속 재구매하고 있어요." },
          { stars: "★★★★☆", tag: "복합성 · 30대", text: "고농도라 그런지 처음엔 살짝 따가웠는데 금방 적응됐어요." },
          { stars: "★★★★★", tag: "지성 · 20대", text: "모공이랑 잡티가 조금씩 옅어지는 게 눈에 보여요." }
        ]
      },
      {
        brand: "디오디너리", product: "나이아신아마이드 10% + 징크 1%", ingredient: "나이아신아마이드",
        price: "약 9,000원 (30ml)", rank: "글로벌 스테디셀러",
        intro: "나이아신아마이드에 징크를 더해 피지·트러블 케어에 초점을 맞춘 오리지널 포뮬러입니다.",
        reviews: [
          { stars: "★★★★☆", tag: "지성 · 20대", text: "T존 유분이 확실히 줄어드는 게 느껴져요." },
          { stars: "★★★☆☆", tag: "건성 · 30대", text: "저는 건성이라 그런지 살짝 당기는 느낌이 있었어요." },
          { stars: "★★★★★", tag: "복합성 · 20대", text: "가성비 최고, 학생 때부터 계속 쓰고 있는 제품이에요." }
        ]
      },
      {
        brand: "코스알엑스", product: "더 나이아신아마이드 15 세럼", ingredient: "나이아신아마이드",
        price: "약 15,000원 (20ml)", rank: "트러블·피지 완화 카테고리 인기 상품",
        intro: "15% 나이아신아마이드로 피지 분비와 모공 결을 관리하는 세럼입니다.",
        reviews: [
          { stars: "★★★★★", tag: "지성 · 20대", text: "여름에 유독 번들거리는 피부인데 확실히 정돈돼요." },
          { stars: "★★★★☆", tag: "복합성 · 30대", text: "자극 없이 순하게 쓸 수 있어서 좋아요." },
          { stars: "★★★★☆", tag: "지성 · 20대", text: "모공이 조금 조밀해진 느낌, 꾸준히 써야 체감돼요." }
        ]
      },
      {
        brand: "메디큐브", product: "PDRN 핑크 펩타이드 앰플", ingredient: "펩타이드",
        price: "약 32,000원 (30ml)", rank: "올리브영 2025 어워즈 선정 상품",
        intro: "PDRN과 펩타이드를 결합해 자극 없이 흡수되는 재생·탄력 케어 앰플입니다.",
        reviews: [
          { stars: "★★★★★", tag: "건성 · 30대", text: "끈적임 없이 흡수돼서 아침저녁 부담 없이 쓰고 있어요." },
          { stars: "★★★★☆", tag: "복합성 · 40대", text: "탄력 효과는 꾸준히 써야 체감되는 편이에요." },
          { stars: "★★★★★", tag: "건성 · 20대", text: "피부 톤이 화사해지고 결이 매끈해진 느낌!" }
        ]
      },
      {
        brand: "성분에디터", product: "실크펩타이드 EGF 하트핏 볼륨 리프팅 앰플", ingredient: "펩타이드",
        price: "약 34,000원 (40ml)", rank: "탄력앰플 카테고리 1위 태그 상품",
        intro: "실크 펩타이드와 EGF 성분으로 처진 피부에 탄력과 볼륨감을 더하는 리프팅 앰플입니다.",
        reviews: [
          { stars: "★★★★★", tag: "건성 · 40대", text: "볼 라인이 살짝 탄탄해진 느낌이라 계속 쓰고 싶어요." },
          { stars: "★★★★☆", tag: "복합성 · 30대", text: "제형이 꾸덕해서 겨울 밤 케어로 딱이에요." },
          { stars: "★★★★★", tag: "건성 · 30대", text: "패키지도 예쁘고 마사지하면서 쓰기 좋아요." }
        ]
      },
      {
        brand: "바이오힐보", product: "콜라겐 리모델링 세럼", ingredient: "펩타이드",
        price: "약 25,000원 (30ml)", rank: "모공·탄력 세럼 카테고리 인기 상품",
        intro: "콜라겐과 펩타이드 복합 성분으로 처진 모공과 탄력을 함께 케어하는 세럼입니다.",
        reviews: [
          { stars: "★★★★☆", tag: "복합성 · 30대", text: "세로모공 고민이었는데 결이 조금씩 정돈되는 느낌이에요." },
          { stars: "★★★★★", tag: "건성 · 40대", text: "탄력 케어 세럼 중에 흡수력은 제일 만족스러워요." },
          { stars: "★★★☆☆", tag: "지성 · 20대", text: "저는 지성이라 여름엔 살짝 무겁게 느껴져요." }
        ]
      },
      {
        brand: "라운드랩", product: "약콩 판테놀 크림", ingredient: "판테놀",
        price: "약 19,000원 (80ml)", rank: "보습장벽 카테고리 스테디셀러",
        intro: "약콩 성분과 판테놀을 더해 건조하고 예민한 피부의 수분 장벽을 채워주는 크림입니다.",
        reviews: [
          { stars: "★★★★★", tag: "건성 · 20대", text: "가성비 대용량 크림으로 온 가족이 같이 쓰고 있어요." },
          { stars: "★★★★☆", tag: "민감성 · 30대", text: "향도 순하고 자극 없어서 아이 얼굴에도 발라줘요." },
          { stars: "★★★★★", tag: "건성 · 30대", text: "겨울철 필수템, 다 쓰기 전에 미리 재구매해요." }
        ]
      },
      {
        brand: "아토팜", product: "판테놀 크림", ingredient: "판테놀",
        price: "약 18,000원 (80ml)", rank: "올영 대란템으로 꾸준히 언급되는 상품",
        intro: "저자극 포뮬러에 판테놀을 담아 아이부터 성인까지 쓸 수 있는 순한 보습 크림입니다.",
        reviews: [
          { stars: "★★★★★", tag: "민감성 · 30대", text: "아토피성 피부인데 자극 없이 순하게 잘 맞아요." },
          { stars: "★★★★☆", tag: "건성 · 20대", text: "보습력은 좋은데 여름엔 살짝 무거울 수 있어요." },
          { stars: "★★★★★", tag: "복합성 · 40대", text: "온 가족 전용 크림으로 자리잡은 지 오래됐어요." }
        ]
      },
      {
        brand: "마일드랩", product: "블루센텔라 더마 리페어크림", ingredient: "판테놀",
        price: "약 26,000원 (50ml)", rank: "EGF·판테놀 조합 진정크림 인기 상품",
        intro: "판테놀과 병풀 성분을 함께 담아 손상된 피부 장벽을 빠르게 복구하는 크림입니다.",
        reviews: [
          { stars: "★★★★☆", tag: "민감성 · 20대", text: "시술 후 회복용으로 쓰기 좋다고 해서 구매했어요." },
          { stars: "★★★★★", tag: "건성 · 30대", text: "붉은기랑 열감이 확실히 가라앉는 느낌이에요." },
          { stars: "★★★★☆", tag: "복합성 · 20대", text: "제형이 꾸덕한 편이라 밤 크림으로 주로 써요." }
        ]
      },
      {
        brand: "마녀공장", product: "비피다 바이옴 아쿠아 베리어 크림", ingredient: "프로바이오틱스",
        price: "약 22,000원 (80ml)", rank: "장벽케어 카테고리 인기 상품",
        intro: "비피다발효여과물 등 5종 발효 성분으로 피부 장벽과 보습을 동시에 케어하는 크림입니다.",
        reviews: [
          { stars: "★★★★★", tag: "건성 · 30대", text: "가벼운데도 보습력이 오래가서 데일리로 쓰기 좋아요." },
          { stars: "★★★★☆", tag: "복합성 · 20대", text: "발효 성분이라 그런지 자극 없이 순하게 흡수돼요." },
          { stars: "★★★★★", tag: "건성 · 40대", text: "환절기 장벽 무너졌을 때 구원템이었어요." }
        ]
      },
      {
        brand: "마녀공장", product: "비피다 바이옴 콤플렉스 앰플", ingredient: "프로바이오틱스",
        price: "약 24,000원 (30ml)", rank: "장벽부스터 카테고리 인기 상품",
        intro: "발효 성분 복합체로 예민해진 피부 장벽을 채워주는 부스팅 앰플입니다.",
        reviews: [
          { stars: "★★★★☆", tag: "민감성 · 30대", text: "예민할 때 부스터로 먼저 발라주면 진정이 빨라요." },
          { stars: "★★★★★", tag: "건성 · 20대", text: "가볍게 흡수되면서 촉촉함이 오래 유지돼요." },
          { stars: "★★★★☆", tag: "복합성 · 30대", text: "크림이랑 같이 쓰니 보습 지속력이 확실히 좋아졌어요." }
        ]
      },
      {
        brand: "아비브", product: "부활초 비피다 세럼 (퍼밍 드롭)", ingredient: "프로바이오틱스",
        price: "약 25,000원 (50ml)", rank: "발효 스킨케어 라인 대표 상품",
        intro: "부활초 발효 성분과 비피다발효여과물로 탄력과 보습을 동시에 노리는 세럼입니다.",
        reviews: [
          { stars: "★★★★★", tag: "복합성 · 30대", text: "가볍게 발리는데 아침에 피부가 탱탱해진 느낌이에요." },
          { stars: "★★★★☆", tag: "건성 · 40대", text: "보습감은 좋은데 저는 크림이랑 같이 써야 충분해요." },
          { stars: "★★★★★", tag: "지성 · 20대", text: "산뜻한 제형이라 여름에도 부담 없이 쓰기 좋아요." }
        ]
      },
      {
        brand: "토리든", product: "다이브인 저분자 히알루론산 세럼", ingredient: "히알루론산",
        price: "22,000원 (50ml)", rank: "글로우픽 에센스·세럼 7위 · ★4.34 (리뷰 3,292) · 2025 올리브영 어워즈 1위",
        intro: "5중 저분자 히알루론산으로 끈적임 없이 속당김까지 개선하는, 올리브영 3년 연속 수상 세럼입니다.",
        reviews: [
          { stars: "★★★★★", tag: "복합성 · 20대", text: "끈적임 없이 촉촉해서 사계절 내내 쓰는 세럼이에요." },
          { stars: "★★★★★", tag: "건성 · 30대", text: "속당김이 확실히 줄어서 겨울에도 재구매하고 있어요." },
          { stars: "★★★★☆", tag: "지성 · 20대", text: "가볍게 잘 흡수되는데 여름엔 한 번 더 덧발라줘요." }
        ]
      },
      {
        brand: "아누아", product: "PDRN 히알루론산 캡슐 100 세럼", ingredient: "히알루론산",
        price: "39,000원 (30ml)", rank: "글로우픽 에센스·세럼 TOP20 · ★4.34",
        intro: "PDRN과 고농축 히알루론산 캡슐 성분으로 결 관리와 보습을 함께 노리는 세럼입니다.",
        reviews: [
          { stars: "★★★★★", tag: "건성 · 30대", text: "결이 매끈해지고 보습감도 확실히 오래가요." },
          { stars: "★★★★☆", tag: "복합성 · 20대", text: "캡슐 제형이 신기하고 흡수력도 좋은 편이에요." },
          { stars: "★★★★★", tag: "건성 · 40대", text: "가격대는 있지만 그만큼 만족도가 높은 세럼이에요." }
        ]
      },
      {
        brand: "아이소이", product: "브라이트닝 카밍 스팟 세럼", ingredient: "히알루론산",
        price: "35,000원 (35ml)", rank: "★4.39 · 2021 올리브영 어워즈 에센스·세럼 1위",
        intro: "히알루론산 보습 베이스에 잡티·톤 케어 성분을 더한 스팟 세럼입니다.",
        reviews: [
          { stars: "★★★★★", tag: "복합성 · 30대", text: "잡티가 옅어지고 톤이 화사해지는 게 눈에 보여요." },
          { stars: "★★★★☆", tag: "건성 · 40대", text: "보습력도 챙기면서 미백까지 되는 느낌이라 만족해요." },
          { stars: "★★★★★", tag: "지성 · 20대", text: "꾸준히 바르니 잡티 고민이 확실히 줄었어요." }
        ]
      }
    ];

    // 국가별 트렌드에 대응하는 실제 보도 기사
    var trendArticles = {
      KR: {
        source: "코스모닝",
        title: "올리브영 '2026 뷰티 트렌드' FULLMOON 발표",
        summary: "올리브영이 발표한 2026 뷰티 트렌드 'FULLMOON'은 보름달이 상징하는 '온전함·완전성·충만함'을 핵심 개념으로 내세운다. 회복케어와 스킨케어링 메이크업이 강세를 보이며, 환경 차단막을 강화한 스킨케어 제품군이 매출 상위권을 차지하고 있다. '미세먼지 차단 크림', '피부 보호막' 등 관련 검색량은 전년 대비 148% 증가했다.",
        url: "https://www.cosmorning.com/news/article.html?no=51865"
      },
      US: {
        source: "Cosmetics Business",
        title: "What drives the rising demand for cosmetic grade Azelaic Acid?",
        summary: "\"Azelaic acid has a long history in dermatology as a versatile therapeutic agent, addressing a spectrum of skin concerns. In recent years, demand has expanded beyond dermatology and is increasingly featured in over-the-counter skincare and prestige beauty launches, with mass brands releasing stacked formulas that combine it with complementary actives.\"",
        url: "https://cosmeticsbusiness.com/what-drives-the-rising-demand-for-cosmetic-grade"
      },
      JP: {
        source: "MAQUIA ONLINE",
        title: "【2026年最新ヘアケア5選】もはやスキンケア級。キューティクルケアも再注目！",
        summary: "髪表面のキューティクルケアに再び注目が集まっている。これまでは髪内部の補修が中心だったが、キューティクル同士を繋ぎ止めるCMC的な成分でラメラ構造自体を整えるアイテムが増加。頭皮ケア製品にもセラミドなどスキンケア発想の保湿成分が使われ始めている。",
        url: "https://maquia.hpplus.jp/hair/news/115158/"
      },
      FR: {
        source: "Demain Beauty",
        title: "French clean beauty: excellence in skincare in 2026",
        summary: "\"Faced with a proliferation of synthetic active ingredients and saturated routines, finding French clean beauty that combines high tolerance and measurable results has become a real strategic challenge.\" 2026년 프랑스 클린 뷰티는 마이크로바이옴 밸런스와 타깃 바이오테크를 앞세워, 단계 수는 줄이면서도 결과는 타협하지 않는 고농축 미니멀 포뮬러로 진화하고 있다.",
        url: "https://demainbeauty.com/en/blogs/blog/la-clean-beauty-francaise-lexcellence-du-soin"
      },
      CN: {
        source: "CBNData",
        title: "一年90个，化妆品新原料透露哪些趋势？",
        summary: "2024년 이후 중국 국가약품감독관리국(NMPA)에 총 90종의 신규 화장품 원료가 등록되며 2023년(69종) 대비 30.4% 증가했다. 이 중 80% 이상이 자국 기업 등록이며, 식물 유래 원료가 합성 화학 원료를 앞지르고 펩타이드·NMN이 안티에이징 분야의 핵심 소재로 떠오르고 있다.",
        url: "https://m.cbndata.com/information/293509"
      }
    };
    var trendModalBackdrop = document.getElementById("trend-modal-backdrop");
    var trendModalClose = document.getElementById("trend-modal-close");

    function openTrendModal(countryCode) {
      var t = trendArticles[countryCode];
      if (!t) return;
      document.getElementById("trend-region-tag").textContent = countryCode;
      document.getElementById("trend-source").textContent = "출처: " + t.source;
      document.getElementById("trend-title").textContent = t.title;
      document.getElementById("trend-summary").textContent = t.summary;
      document.getElementById("trend-link").href = t.url;
      trendModalBackdrop.classList.add("open");
    }

    function closeTrendModal() {
      trendModalBackdrop.classList.remove("open");
    }

    document.querySelectorAll(".country-card").forEach(function (card) {
      card.addEventListener("click", function () {
        openTrendModal(card.getAttribute("data-country"));
      });
      card.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openTrendModal(card.getAttribute("data-country"));
        }
      });
    });
    trendModalClose.addEventListener("click", closeTrendModal);
    trendModalBackdrop.addEventListener("click", function (e) {
      if (e.target === trendModalBackdrop) closeTrendModal();
    });

    // 헤드라인 다국어 자동 순환 (한국어 → 영어 → 중국어 → 일본어)
    var headlineTexts = [
      "오늘, 뷰티 시장에서 알아야 할 것들",
      "Today, What You Need to Know in the Beauty Market",
      "今天,你需要了解的美妆市场动态",
      "本日、美容市場で知っておくべきこと"
    ];
    var headlineEl = document.getElementById("hero-headline-text");
    var headlineIndex = 0;
    if (headlineEl) {
      setInterval(function () {
        headlineEl.classList.add("is-out");
        setTimeout(function () {
          headlineIndex = (headlineIndex + 1) % headlineTexts.length;
          headlineEl.textContent = headlineTexts[headlineIndex];
          headlineEl.classList.remove("is-out");
          headlineEl.classList.add("is-in");
          void headlineEl.offsetWidth;
          headlineEl.classList.remove("is-in");
        }, 350);
      }, 3000);
    }

    var chipGrid = document.getElementById("chip-grid");
    var productGrid = document.getElementById("product-grid");
    var searchInput = document.getElementById("search-input");
    var resetBtn = document.getElementById("reset-btn");
    var rowCount = document.getElementById("row-count");
    var detailPanel = document.getElementById("detail-panel");
    var detailClose = document.getElementById("detail-close");
    var modalBackdrop = document.getElementById("product-modal-backdrop");
    var modalClose = document.getElementById("modal-close");
    var activeIngredient = null;

    function findIngredient(name) {
      for (var i = 0; i < ingredients.length; i++) {
        if (ingredients[i].name === name) return ingredients[i];
      }
      return null;
    }

    function renderChips() {
      chipGrid.innerHTML = "";
      var ranked = ingredients.slice().sort(function (a, b) {
        return parseFloat(b.delta) - parseFloat(a.delta);
      });
      ranked.forEach(function (ing, idx) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "chip-card" + (activeIngredient === ing.name ? " active" : "");
        btn.setAttribute("aria-pressed", activeIngredient === ing.name ? "true" : "false");
        btn.innerHTML =
          '<div class="chip-rank">' + (idx + 1) + '</div>' +
          '<div class="chip-main">' +
          '<div class="name">' + ing.name + '<span class="delta">' + ing.delta + '</span></div>' +
          '<div class="desc">' + ing.desc + '</div>' +
          '</div>';
        btn.addEventListener("click", function () {
          activeIngredient = activeIngredient === ing.name ? null : ing.name;
          renderChips();
          renderProducts();
          renderDetail();
        });
        chipGrid.appendChild(btn);
      });
    }

    function renderDetail() {
      var ing = activeIngredient ? findIngredient(activeIngredient) : null;
      if (!ing) {
        detailPanel.classList.remove("open");
        return;
      }
      document.getElementById("detail-name").textContent = ing.stdName;
      document.getElementById("detail-eng").textContent = ing.engName;
      document.getElementById("detail-cas").textContent = ing.cas;
      document.getElementById("detail-code").textContent = ing.code;
      document.getElementById("detail-definition").textContent = ing.definition;
      document.getElementById("detail-link").href = ing.url;

      var purposesEl = document.getElementById("detail-purposes");
      purposesEl.innerHTML = "";
      ing.purposes.forEach(function (p) {
        var span = document.createElement("span");
        span.className = "concept-tag";
        span.textContent = p;
        purposesEl.appendChild(span);
      });

      var goodEl = document.getElementById("detail-good-combo");
      goodEl.innerHTML = "";
      ing.goodWith.forEach(function (g) {
        var span = document.createElement("span");
        span.className = "combo-good-tag";
        span.textContent = g;
        goodEl.appendChild(span);
      });

      var cautionEl = document.getElementById("detail-caution-combo");
      cautionEl.innerHTML = "";
      if (ing.avoidWith.length === 0) {
        var noneSpan = document.createElement("span");
        noneSpan.className = "concept-tag";
        noneSpan.textContent = "특별한 주의 성분 없음";
        cautionEl.appendChild(noneSpan);
      } else {
        ing.avoidWith.forEach(function (a) {
          var span = document.createElement("span");
          span.className = "combo-caution-tag";
          span.textContent = a;
          cautionEl.appendChild(span);
        });
      }
      document.getElementById("detail-caution-note").textContent = ing.avoidNote || "";

      var skinEl = document.getElementById("detail-skin-types");
      skinEl.innerHTML = "";
      ing.skinTypes.forEach(function (s) {
        var span = document.createElement("span");
        span.className = "concept-tag";
        span.textContent = s;
        skinEl.appendChild(span);
      });

      detailPanel.classList.add("open");
    }

    // 실제 제품 사진은 이 화면(Artifact)의 보안 정책상 외부 이미지 로딩이 막혀 있어 불러올 수 없어,
    // 용기 형태(크림/세럼·앰플)를 구분하는 아이콘 일러스트로 대신합니다.
    var ICON_JAR =
      '<svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">' +
      '<rect x="10" y="6" width="20" height="6" rx="2" stroke="currentColor" stroke-width="2"/>' +
      '<rect x="8" y="12" width="24" height="22" rx="4" stroke="currentColor" stroke-width="2"/>' +
      '<line x1="8" y1="19" x2="32" y2="19" stroke="currentColor" stroke-width="1.5" opacity="0.5"/>' +
      '</svg>';
    var ICON_BOTTLE =
      '<svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">' +
      '<rect x="16" y="4" width="8" height="8" rx="1.5" stroke="currentColor" stroke-width="2"/>' +
      '<path d="M16 12 L14 16 L14 32 A4 4 0 0 0 18 36 H22 A4 4 0 0 0 26 32 V16 L24 12 Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>' +
      '<line x1="14" y1="22" x2="26" y2="22" stroke="currentColor" stroke-width="1.5" opacity="0.5"/>' +
      '</svg>';

    function getProductIcon(p) {
      return p.product.indexOf("크림") !== -1 ? ICON_JAR : ICON_BOTTLE;
    }

    function renderProducts() {
      var query = searchInput.value.trim().toLowerCase();
      var rows = products.filter(function (p) {
        var matchesIngredient = !activeIngredient || p.ingredient === activeIngredient;
        var haystack = (p.brand + " " + p.product + " " + p.ingredient).toLowerCase();
        var matchesQuery = !query || haystack.indexOf(query) !== -1;
        return matchesIngredient && matchesQuery;
      });

      productGrid.innerHTML = "";
      if (rows.length === 0) {
        var empty = document.createElement("div");
        empty.className = "empty-state";
        empty.textContent = "조건에 맞는 제품이 없습니다.";
        productGrid.appendChild(empty);
      }
      rows.forEach(function (p) {
        var card = document.createElement("button");
        card.type = "button";
        card.className = "product-card";
        card.innerHTML =
          '<div class="product-card-media">' + getProductIcon(p) + '</div>' +
          '<div class="product-card-body">' +
          '<div class="brand-name">' + p.brand + '</div>' +
          '<div class="product-name">' + p.product + '</div>' +
          '<div class="rank-preview">' + p.rank.split(" · ")[0] + '</div>' +
          '</div>';
        card.addEventListener("click", function () { openProductModal(p); });
        productGrid.appendChild(card);
      });
      rowCount.textContent = rows.length + "건";
    }

    function openProductModal(p) {
      document.getElementById("modal-ingredient-tag").textContent = p.ingredient;
      document.getElementById("modal-product-name").textContent = p.product;
      document.getElementById("modal-brand").textContent = p.brand + " · " + p.price;
      document.getElementById("modal-rank").textContent = p.rank;
      document.getElementById("modal-intro").textContent = p.intro;
      document.getElementById("modal-tile").innerHTML = getProductIcon(p);

      var reviewsEl = document.getElementById("modal-reviews");
      reviewsEl.innerHTML = "";
      p.reviews.forEach(function (r) {
        var item = document.createElement("div");
        item.className = "review-item";
        item.innerHTML =
          '<div class="review-head"><span class="stars">' + r.stars + '</span><span class="skin-tag">' + r.tag + '</span></div>' +
          '<p>' + r.text + '</p>';
        reviewsEl.appendChild(item);
      });

      modalBackdrop.classList.add("open");
    }

    function closeProductModal() {
      modalBackdrop.classList.remove("open");
    }

    searchInput.addEventListener("input", renderProducts);
    resetBtn.addEventListener("click", function () {
      searchInput.value = "";
      activeIngredient = null;
      renderChips();
      renderProducts();
      renderDetail();
    });
    detailClose.addEventListener("click", function () {
      activeIngredient = null;
      renderChips();
      renderProducts();
      renderDetail();
    });
    modalClose.addEventListener("click", closeProductModal);
    modalBackdrop.addEventListener("click", function (e) {
      if (e.target === modalBackdrop) closeProductModal();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        closeProductModal();
        closeTrendModal();
      }
    });

    renderChips();
    renderProducts();
    renderDetail();
  })();
</script>
</body>
</html>
"""


components.html(HTML_CONTENT, height=4200, scrolling=True)
