"""Build standalone case pages from the media manifest and verbatim prompt files."""
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build():
    videos = json.loads((ROOT / 'assets/videos/manifest.json').read_text(encoding='utf-8'))['videos']
    output = ROOT / 'cases'
    output.mkdir(exist_ok=True)
    for index, video in enumerate(videos):
        prompt_path = video.get('original_prompt')
        if not prompt_path:
            continue
        prompt = (ROOT / prompt_path).read_text(encoding='utf-8')
        title = escape(video['title_zh'])
        title_en = escape(video['title_en'])
        key = video['id']
        duration = video['prompt_duration_seconds']
        adjacent = []
        for offset, label in [(-1, '← 上一个案例'), (1, '下一个案例 →')]:
            position = index + offset
            if 0 <= position < len(videos) and videos[position].get('original_prompt'):
                item = videos[position]
                adjacent.append(f'<a href="{item["id"]}.html">{label} · {escape(item["title_zh"])}</a>')
        page = f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{title}破纸展示视频与对应原始提示词，可播放、复制和下载。">
  <meta name="theme-color" content="#FFFaf5">
  <title>{title} · 视频与提示词 | Product Paper Reveal</title>
  <link rel="stylesheet" href="../assets/case.css">
  <script src="../assets/case.js" defer></script>
</head>
<body><div class="wrap">
  <nav class="top" aria-label="案例导航"><a class="brand" href="../index.html#{key}">← 返回全部案例 / Gallery</a><a href="https://github.com/yinxiaowai/ecommerce-paper-reveal-video">GitHub 项目</a></nav>
  <header><p class="eyebrow">AI尹小歪 / VIDEO &amp; PROMPT</p><h1>{title} <small lang="en">{title_en}</small></h1><p class="meta">{duration} 秒 · 9:16 竖屏 · {video['width']}P · 作者提供的原始案例</p></header>
  <main>
    <div class="video-wrap"><video controls playsinline preload="metadata" poster="../{video['poster']}" aria-label="{title}破纸展示视频"><source src="../{video['video']}" type="video/mp4">浏览器暂不支持播放，请使用下方下载链接。</video></div>
    <p class="video-download"><a href="../{video['video']}" download>下载视频 / Download video</a></p>
    <section class="prompt" aria-labelledby="prompt-title">
      <div class="prompt-head"><h2 id="prompt-title">原始提示词 <span lang="en">/ Prompt</span></h2><div class="actions"><a href="../{prompt_path}" download>下载 TXT</a><button id="copy-prompt" type="button" hidden>复制提示词 / Copy</button></div></div>
      <p class="note">以下原文对应上方视频，保留当时的参数与写法。复用时，将图片引用绑定到你上传的商品图。<br><span lang="en">Original Chinese prompt for this video. Bind image references to your own product image when reusing it.</span></p>
      <pre><code id="prompt-text">{escape(prompt)}</code></pre>
      <p class="copy-status" id="copy-status" role="status" aria-live="polite"></p>
    </section>
    <nav class="pager" aria-label="相邻案例">{''.join(adjacent)}</nav>
  </main>
  <footer>AI尹小歪 · <a href="../index.html">全部视频</a> · <a href="https://github.com/yinxiaowai/ecommerce-paper-reveal-video/blob/v1.0.0/references/paper-reveal-prompt.zh-CN.md">完整 Skill 规则</a></footer>
</div></body>
</html>
'''
        (output / f'{key}.html').write_text(page, encoding='utf-8', newline='\n')
    print('Built case pages from original prompts.')


if __name__ == '__main__':
    build()
