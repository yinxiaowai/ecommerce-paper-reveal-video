English · [简体中文](README.md)

## About the author

**AI Yin Xiaowai (AI尹小歪)** — invited lecturer at the AI Center of the China Academy of Art; WaytoAGI certified instructor, video community lead, AI tool reviewer, AIGC creator, and enterprise AI trainer. Also a cyber guitar singer.

Practical AI tool walkthroughs, hands-on evaluations, and creative demonstrations:

<table>
  <tr>
    <td align="center" valign="top" width="50%">
      <strong>WeChat Official Account｜小歪的AI工具箱</strong><br>
      Detailed tutorials and AI tool breakdowns<br><br>
      <a href="assets/images/wechat-qr.png"><img src="assets/images/wechat-qr.png" width="314" alt="Xiaowai's AI Toolbox WeChat QR code"></a>
    </td>
    <td align="center" valign="top" width="50%">
      <strong>WeChat Channels｜AI尹小歪</strong><br>
      Tool evaluations and video demonstrations<br><br>
      <a href="assets/images/wechat-channels-qr.jpg"><img src="assets/images/wechat-channels-qr.jpg" width="220" alt="AI Yin Xiaowai WeChat Channels QR code"></a>
    </td>
  </tr>
</table>

[Author's column](https://waytoagi.feishu.cn/wiki/Pddywh6NqiRKb4kaJBscAbf9nUA)

# Product Paper Reveal

**One product image. A slow paper-tear reveal that builds curiosity.**

A portable Agent Skill for creative ecommerce videos. Defaults to **5 seconds, 9:16 portrait**: wrapping paper fills the frame, a central tear slowly opens, and the same single young adult woman's hand gently offers the product forward, ending in a held display.

The paper uses a soft product-adaptive base color, one sparse printed motif, and fine paper grain. Ordinary products keep a stable grip; tiny jewelry that cannot be held visibly may be revealed on the same hand's opening palm.

| Agent capability | Result |
| --- | --- |
| Image understanding and authorized subject-reference video generation | Submit the requested video and deliver the real result |
| Image understanding but no suitable video generator | Deliver a complete, ready-to-use video prompt and reference instructions |
| No image understanding | Explain the limitation and ask for a brief product description |

This workflow is **not restricted to Jimeng** and includes no video engine. The Agent must check its actual tool's subject-reference support. The product image controls appearance; it must never become the first frame. The opening frame is intact wrapping paper.

## Video previews

**[▶ Open the playable gallery — five real videos](https://yinxiaowai.github.io/ecommerce-paper-reveal-video/)**

<table>
  <tr>
    <td align="center" width="33%"><a href="https://yinxiaowai.github.io/ecommerce-paper-reveal-video/#video-01"><img src="assets/images/video-01-poster.jpg" width="240" alt="Play the designer toy reveal"><br>▶ Designer toy</a></td>
    <td align="center" width="33%"><a href="https://yinxiaowai.github.io/ecommerce-paper-reveal-video/#video-02"><img src="assets/images/video-02-poster.jpg" width="240" alt="Play the perfume reveal"><br>▶ Perfume</a></td>
    <td align="center" width="33%"><a href="https://yinxiaowai.github.io/ecommerce-paper-reveal-video/#video-03"><img src="assets/images/video-03-poster.jpg" width="240" alt="Play the canned drink reveal"><br>▶ Canned drink</a></td>
  </tr>
</table>

**New: Headphones · approximately 4 seconds**

[<img src="assets/images/video-04-poster.jpg" width="240" alt="Play the headphone reveal">](https://yinxiaowai.github.io/ecommerce-paper-reveal-video/#video-04)

**New: High heel · approximately 5 seconds · 1080p**

[<img src="assets/images/video-05-poster.jpg" width="240" alt="Play the high heel reveal">](https://yinxiaowai.github.io/ecommerce-paper-reveal-video/#video-05)

Author-supplied Jimeng results: approximately 4–5 seconds, 9:16, 720p / 1080p. Click a poster to watch or download the actual video. Posters are extracted from their corresponding clips; the videos are not re-edited or re-encoded.

## Method 1 — Install the Skill

Download the [Skill ZIP](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/releases/latest/download/ecommerce-paper-reveal-video.zip). It contains an `ecommerce-paper-reveal-video/` folder with `SKILL.md`, both complete specifications, and Agent display configuration.

For Codex, place this folder under `~/.codex/skills/` (on Windows, normally `%USERPROFILE%\.codex\skills\`) and open a new session. For other Agents supporting `SKILL.md`, follow that host's installation rules and preserve the complete folder. Reading a repository URL is not an installation.

Upload your product image and say:

```text
Use $ecommerce-paper-reveal-video to create a 5-second, 9:16 creative paper reveal from my product image. If subject-reference video generation is unavailable, give me a ready-to-use video prompt.
```

The Skill does not install a video model, provide API credentials, or enable paid generation. Installed copies and host-saved skills are independent snapshots; GitHub updates do not automatically update them.

## Method 2 — Use the complete MD directly

Upload the product image and give the Agent the complete specification:

- [Read English v1.0.0](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/blob/v1.0.0/references/paper-reveal-prompt.en.md)
- [Download the latest English MD](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/releases/latest/download/paper-reveal-prompt.en.md)
- [Read Chinese v1.0.0](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/blob/v1.0.0/references/paper-reveal-prompt.zh-CN.md)
- [Download the latest Chinese MD](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/releases/latest/download/paper-reveal-prompt.zh-CN.md)

**Create only:**

```text
Read this complete specification and use my uploaded product image to create a 5-second, 9:16 ecommerce paper reveal:
https://github.com/yinxiaowai/ecommerce-paper-reveal-video/blob/v1.0.0/references/paper-reveal-prompt.en.md
Self-check the prompt and reference-image role first. Generate if subject-reference video generation is available; otherwise deliver the complete video prompt. Do not use the image as a first frame. Do not create or install a skill. If you cannot read the full specification, tell me so I can attach the MD.
```

**Create, then save a reusable skill if supported:**

```text
Read the complete specification and create from my uploaded product image; provide the prompt if subject-reference video generation is unavailable:
https://github.com/yinxiaowai/ecommerce-paper-reveal-video/blob/v1.0.0/references/paper-reveal-prompt.en.md
Afterward, if this host supports creating skills, save the general workflow as “Product Paper Reveal” and provide its native add-skill confirmation. Do not hard-code this product, brand, or palette as defaults. Explain if this host cannot save a skill.
```

These are general invocation examples, not verified integrations for every host. Reading an MD and confirming a native saved skill are separate steps. If a link is inaccessible or incompletely read, attach the downloaded MD instead.

## Default timing

| Time | Visible action |
| --- | --- |
| 0–0.6s | Intact full-frame paper gently bulges in the center |
| 0.6–2.8s | A narrow tear gradually widens, revealing a glimpse and then most of the product |
| 2.8–3.8s | Complete the reveal with only necessary holding fingers/palm visible |
| 3.8–4.7s | Maintain the grip and offer slightly forward, decelerating gently |
| 4.7–5s | Settle and keep holding the product |

The generation prompt carries the timeline and essential visible actions. Detailed adaptation and checks stay internal to the Agent. Product size follows its category, not a universal palm-sized target. Default sound is tearing and paper friction only, with no voices, music, captions, or watermark.

## Validation and feedback

The author iterated on the original recipe in Jimeng and accepted the version with paper decoration. This repository generalizes that workflow and now includes five author-supplied video previews. Release checks cover documentation, conditional paths, and package integrity; no additional generation or cross-model visual benchmark was performed for this edition. The clips were supplied without their complete original prompts or exact model settings, so they are not labeled as fresh tests of the portable release.

Reference fidelity, hand anatomy, and paper persistence depend on the model. The Agent checks its prompt and reference settings before submission, and inspects the video only when viewing is possible. A pending task or a prompt is not a finished video; extra paid attempts require authorization.

[Open an issue](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/issues) with the specification version, tool/model, actual prompt, reference mode, and any result you choose to make public.

## Files and license

- [SKILL.md](SKILL.md): installation entry and capability routing.
- [English standalone specification](references/paper-reveal-prompt.en.md) / [Chinese standalone specification](references/paper-reveal-prompt.zh-CN.md).
- [Changelog](CHANGELOG.md) · [v1.0.0 release](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/releases/tag/v1.0.0): ZIP, standalone MDs, and checksum manifest.

The workflow and documentation use the [MIT License](LICENSE). Author QR codes identify the author and do not authorize impersonation. Product images, trademarks, and generation services remain subject to their respective rights and terms.
