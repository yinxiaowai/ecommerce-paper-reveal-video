const copyButton = document.getElementById('copy-prompt');
const promptText = document.getElementById('prompt-text');
const copyStatus = document.getElementById('copy-status');

copyButton.hidden = false;
copyButton.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(promptText.textContent);
    copyStatus.textContent = '已复制完整提示词 / Copied';
  } catch {
    const range = document.createRange();
    range.selectNodeContents(promptText);
    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    copyStatus.textContent = '自动复制不可用，已选中文本，请手动复制 / Select and copy manually';
  }
});
