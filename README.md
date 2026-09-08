[English](README_EN.md) · 简体中文

## 作者介绍

作者：AI尹小歪

中国美术学院AI中心特聘讲师  
WaytoAGI 认证讲师 & 视频学社主理人 & AI工具测评专家  
资深AIGC实战创作者、企业AI培训讲师

赛博吉他歌手

🔯为你挖掘各种AI效率工具  
📘保姆级教程带你拆解AI工具热门玩法

欢迎关注我的两个内容入口：公众号看完整图文拆解，视频号看工具实测与案例演示。

<table>
  <tr>
    <td align="center" valign="top" width="50%">
      <strong>微信公众号｜小歪的AI工具箱</strong><br>
      AI 资讯、保姆级教程与完整图文拆解<br><br>
      <a href="assets/images/wechat-qr.png"><img src="assets/images/wechat-qr.png" width="314" alt="小歪的AI工具箱公众号二维码"></a>
    </td>
    <td align="center" valign="top" width="50%">
      <strong>视频号｜AI尹小歪</strong><br>
      AI 工具实测、案例演示与视频教程<br><br>
      <a href="assets/images/wechat-channels-qr.jpg"><img src="assets/images/wechat-channels-qr.jpg" width="220" alt="AI尹小歪视频号二维码"></a>
    </td>
  </tr>
</table>

我的个人专栏：[AI尹小歪的个人专栏](https://waytoagi.feishu.cn/wiki/Pddywh6NqiRKb4kaJBscAbf9nUA)

# 电商商品破纸创意视频

**让商品从包装纸后慢慢揭晓。上传一张商品图，做一条有好奇感的产品展示短片。**

Product Paper Reveal 是一个开放的 Agent Skill。默认 **5 秒、9:16 竖屏**：包装纸铺满画面，中央缓缓破开，同一只年轻成年女性的手持商品轻轻向前送，最后保持手持展示。

包装纸根据商品的色调与风格选择柔和底色，搭配一种稀疏小图案与细腻纸纹。普通商品保持稳定握姿；难以握持的微小饰品可由同一只手展开掌心展示。

| 你的 Agent 能力 | 交付结果 |
| --- | --- |
| 能看商品图，并能调用主体参考视频生成工具 | 在已获生成授权时提交视频任务，交付真实结果 |
| 能看图，但没有视频工具或只有首帧图生视频 | 根据商品图交付完整视频提示词和参考图使用说明 |
| 不能看图 | 说明限制，请你补充简短商品描述后继续设计提示词 |

**不限即梦，也不内置任何视频模型。** 工具是否支持主体参考，要由当前 Agent 核对。商品图用于参考商品外观，不能作为首帧；开场应当是完整包装纸。

## 视频效果预览

**[▶ 打开视频预览页，直接播放三条成片](https://yinxiaowai.github.io/ecommerce-paper-reveal-video/)**

<table>
  <tr>
    <td align="center" width="33%"><a href="https://yinxiaowai.github.io/ecommerce-paper-reveal-video/#video-01"><img src="assets/images/video-01-poster.jpg" width="240" alt="播放潮玩手办破纸展示视频"><br>▶ 潮玩手办</a></td>
    <td align="center" width="33%"><a href="https://yinxiaowai.github.io/ecommerce-paper-reveal-video/#video-02"><img src="assets/images/video-02-poster.jpg" width="240" alt="播放皇冠香水破纸展示视频"><br>▶ 皇冠香水</a></td>
    <td align="center" width="33%"><a href="https://yinxiaowai.github.io/ecommerce-paper-reveal-video/#video-03"><img src="assets/images/video-03-poster.jpg" width="240" alt="播放罐装饮料破纸展示视频"><br>▶ 罐装饮料</a></td>
  </tr>
</table>

三条均为作者提供的即梦实测成片，约 5 秒、9:16、720P。点击封面进入可播放页面；页面也提供视频下载。封面取自对应视频，成片未重新剪辑或压缩。

## 方法一：安装为 Skill

下载 [Skill 安装包](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/releases/latest/download/ecommerce-paper-reveal-video.zip)。解压后会得到 `ecommerce-paper-reveal-video/` 文件夹，包含 `SKILL.md`、完整中英文规则与 Agent 显示配置。

对 Codex，将这个文件夹放到 `~/.codex/skills/` 下（Windows 默认对应 `%USERPROFILE%\.codex\skills\`），重新打开会话后调用。其他支持 `SKILL.md` 的 Agent，请按其自身技能安装规范放置完整文件夹；仅访问仓库链接不代表安装成功。

上传商品图，然后说：

```text
使用 $ecommerce-paper-reveal-video，为这张商品图制作 5 秒、9:16 的破纸展示创意视频。如果没有主体参考视频生成能力，直接给我可用的视频提示词。
```

安装这个 Skill 不会安装视频模型、提供 API 密钥或开通付费生成权限。现有安装和平台保存的技能都是独立副本，不会随 GitHub 更新自动升级。

## 方法二：直接使用完整 MD

不安装也能用。上传商品图，将这份**完整规则**交给你的 Agent：

- [阅读中文版 v1.0.0](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/blob/v1.0.0/references/paper-reveal-prompt.zh-CN.md)
- [下载最新中文版 MD](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/releases/latest/download/paper-reveal-prompt.zh-CN.md)
- [English specification v1.0.0](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/blob/v1.0.0/references/paper-reveal-prompt.en.md)
- [下载最新英文版 MD](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/releases/latest/download/paper-reveal-prompt.en.md)

**直接创作：**

```text
请完整读取这份规则，并根据我上传的商品图创作 5 秒、9:16 的电商商品破纸展示视频：
https://github.com/yinxiaowai/ecommerce-paper-reveal-video/blob/v1.0.0/references/paper-reveal-prompt.zh-CN.md
先自行检查提示词与参考图用途。能用主体参考生成视频就执行；没有这项能力就直接交付完整视频提示词。不要把商品图设为首帧，不创建或安装技能。如果读不到完整规则，请告诉我，我会上传 MD。
```

**创作后保存为可复用技能（仅限支持的平台）：**

```text
请按这份完整规则，根据我上传的商品图创作；没有主体参考视频能力就提供提示词：
https://github.com/yinxiaowai/ecommerce-paper-reveal-video/blob/v1.0.0/references/paper-reveal-prompt.zh-CN.md
完成后，如果平台支持创建技能，请将通用规则保存为“电商商品破纸创意视频”，并提供平台原生的添加技能确认入口。不要把这次的商品、品牌或配色固化成默认值。如果平台不支持，请说明。
```

以上是通用调用方式，不代表已在所有 Agent 上验证。即梦等平台的原生“添加技能”确认与读取 MD 是不同步骤。链接读取不全时，可下载 MD 直接作为附件上传。

## 默认镜头节奏

| 时间 | 可见动作 |
| --- | --- |
| 0–0.6 秒 | 满屏完整纸面中央轻轻鼓起 |
| 0.6–2.8 秒 | 裂缝缓缓扩大，商品从局部到大半逐渐露出 |
| 2.8–3.8 秒 | 商品完成揭晓，只显露必要的持物手部 |
| 3.8–4.7 秒 | 保持握姿，微微向前送并减速 |
| 4.7–5 秒 | 停稳，保持手持展示 |

时间轴和关键画面进入提示词，详细的适配规则与自检留给 Agent 内部使用。商品大小按品类判断，不统一限定成掌心大小。声音默认只有撕纸与纸张摩擦声，没有人声、背景音乐、字幕或水印。

## 验证范围与反馈

原始玩法经过作者在即梦多轮测试，并确认带纸面点缀的版本可用。本仓库是在该版本上整理的通用执行规则，现提供作者的三条实际成片预览。通用版发布检查文档、条件分支和安装包一致性，未新增视频生成测试，也未验证所有模型的画面表现。示例的原始完整提示词和确切模型配置未随素材提供，不将其标为通用版的重新生成测试。

参考图一致性、手部结构和纸面持续存在仍取决于生成模型。Agent 会先审查提示词与参考输入，能查看结果时再检查视频；不会把排队状态或提示词当成成片，也不会未经授权自动重复付费生成。

欢迎提交 [Issue](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/issues)。反馈时提供规范版本、模型/工具、实际提示词及参考模式，附上你愿意公开的结果即可。

## 文件与许可

- [SKILL.md](SKILL.md)：安装入口与能力分流。
- [完整中文规则](references/paper-reveal-prompt.zh-CN.md) / [完整英文规则](references/paper-reveal-prompt.en.md)：可单独作为附件使用。
- [更新记录](CHANGELOG.md) · [v1.0.0 Release](https://github.com/yinxiaowai/ecommerce-paper-reveal-video/releases/tag/v1.0.0)：下载包、MD 与校验清单。

本项目规则与文档采用 [MIT License](LICENSE)。作者二维码用于介绍作者，不表示授权冒用身份；用户上传的商品图、商标及生成服务的权利和使用条款分别适用。
