---
name: ecommerce-paper-reveal-video
description: Create creative ecommerce product reveal videos or ready-to-use video prompts from a product image. Use for a slow wrapping-paper tear reveal with one hand, full-frame paper, and a brief handheld finish. Defaults to 5 seconds and 9:16; falls back to prompt delivery when subject-reference video generation is unavailable.
---

# 电商商品破纸创意视频 · Product Paper Reveal

Specification version: 1.0.0.

Turn one product image into a slow, curiosity-building paper-tear reveal. This is a model-neutral creative workflow, not a video engine or a Jimeng-only integration.

Read the complete workflow before preparing a prompt or invoking a generator:

- Chinese: [references/paper-reveal-prompt.zh-CN.md](references/paper-reveal-prompt.zh-CN.md)
- English: [references/paper-reveal-prompt.en.md](references/paper-reveal-prompt.en.md)

Read one language in full; both contain the complete rules, timing template, same-hand tiny-item exception, and internal checks. Respond in the user's language.

## Capability routing

1. Inspect the product image. Ask only for missing input or an ambiguous target among different products.
2. If the user requests a video and an available, authorized tool supports product/subject-reference video generation, use its documented reference input and actual resource binding.
3. If video generation is unavailable, only first-frame generation is available, or the user wants a prompt, deliver one fully resolved video prompt plus duration, ratio, and reference-image usage. Do not require a generator installation to provide this useful result.
4. If image understanding is unavailable, explain that limitation and request a brief product description. Do not pretend to have inspected an image.

Never silently use the product image as a first or last frame. Do not invent tool names, resource IDs, native reference tags, or model support. Plain “product reference image” is portable prompt wording; adapt it only to a documented native reference mechanism.

## Preserve the creative core

- Default: 5 seconds, 9:16, locked frontal camera, one continuous shot.
- Wrapping paper fills the frame with its original outer edges beyond the image. Add one sparse printed motif and fine paper grain, with a soft product-adaptive base color.
- Slowly reveal through a central local tear, then offer the product slightly forward and keep it held.
- Exactly the same single young adult woman's hand throughout. Ordinary items retain the established grip; only tiny items that cannot be held visibly use the documented same-hand palm reveal.
- Natural product-category scale; no fixed finger-width or palm-length measurements. Keep wrist and forearm behind the paper.

Keep planning rules internal. Compile only the selected action branch into a concise prompt. Self-check the prompt and actual reference settings before generation. Report real job status and only claim visual inspection when possible; do not retry paid generation without authorization.
