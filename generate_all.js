const fs = require('fs');
const path = require('path');

const projectDir = '/Users/ashrafulasif/Documents/demo/project';

function highlightHTML(rawHtml) {
  // 1. Escape HTML entities
  let text = rawHtml
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');

  // 2. Highlight DOCTYPE
  text = text.replace(/&lt;!DOCTYPE\s+html&gt;/gi, '&lt;<span class="syn-tag">!DOCTYPE</span> <span class="syn-attr">html</span>&gt;');

  // 3. Highlight HTML comments
  text = text.replace(/&lt;!--([\s\S]*?)--&gt;/g, '<span style="color: #6a9955; font-style: italic;">&lt;!--$1--&gt;</span>');

  // 4. Highlight closing tags
  text = text.replace(/&lt;\/([a-zA-Z0-9\-]+)&gt;/g, '&lt;/<span class="syn-tag">$1</span>&gt;');

  // 5. Highlight opening / self-closing tags
  text = text.replace(/&lt;([a-zA-Z0-9\-]+)(\s[\s\S]*?)?(\/?)&gt;/g, (match, tagName, attrs, selfClose) => {
    if (match.includes('color: #6a9955')) return match;

    let tag = `&lt;<span class="syn-tag">${tagName}</span>`;
    let highlightedAttrs = '';
    if (attrs) {
      highlightedAttrs = attrs.replace(/([a-zA-Z0-9\-]+)=(&quot;[\s\S]*?&quot;)/g, ' <span class="syn-attr">$1</span>=<span class="syn-string">$2</span>');
    }
    let slash = selfClose ? ' /' : '';
    return `${tag}${highlightedAttrs}${slash}&gt;`;
  });

  return text;
}

const files = [
  { source: 'index.html', target: 'index_code.html', title: 'Wanderlist — Home' },
  { source: 'destinations.html', target: 'destinations_code.html', title: 'Wanderlist — Destinations' },
  { source: 'gallery.html', target: 'gallery_code.html', title: 'Wanderlist — Gallery' }
];

files.forEach(({ source, target, title }) => {
  const sourcePath = path.join(projectDir, source);
  const rawContent = fs.readFileSync(sourcePath, 'utf8');

  // Extract body content for live preview
  const bodyMatch = rawContent.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
  const bodyContent = bodyMatch ? bodyMatch[1].trim() : rawContent;

  const highlightedCode = highlightHTML(rawContent);

  const outputHtml = `<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} — Code & Preview</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="css/style.css" />
    <style type="text/css">
        body {
            background-color: #f1f5f9;
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            margin: 0;
            padding: 20px;
            color: #1f2937;
        }
        .container { max-width: 1100px; margin: 0 auto; }

        /* VS Code Source Code Window */
        .vscode-window { background-color: #1e1e1e; border-radius: 8px; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3); overflow: hidden; margin-bottom: 30px; border: 1px solid #333; }
        .vscode-header { background-color: #252526; color: #cccccc; padding: 0 15px; font-size: 0.85em; border-bottom: 1px solid #333; display: flex; align-items: center; justify-content: space-between; height: 35px; }
        .vscode-tabs { display: flex; height: 100%; }
        .vscode-tab { background-color: #1e1e1e; padding: 0 15px; color: white; display: flex; align-items: center; gap: 8px; font-family: 'Inter', sans-serif; font-size: 12px; border-top: 1px solid #007acc; cursor: pointer; }
        .vscode-content { margin: 0; padding: 24px; color: #d4d4d4; overflow-x: auto; font-family: 'Consolas', 'Monaco', 'Courier New', monospace; font-size: 14px; line-height: 1.5; white-space: pre; }
        
        .syn-tag { color: #569cd6; }       /* Blue */
        .syn-attr { color: #9cdcfe; }      /* Light Blue */
        .syn-string { color: #ce9178; }    /* Orange */
        .syn-selector { color: #d7ba7d; }  /* Yellow */
        .syn-prop { color: #9cdcfe; }      /* Light Blue */
        .syn-val { color: #ce9178; }       /* Orange */
        .syn-unit { color: #b5cea8; }      /* Light Green */

        /* VS Code Live Preview Window */
        .preview-section { margin-top: 40px; }
        .preview-label { font-weight: bold; font-size: 1.1em; color: #1f2937; margin-bottom: 12px; display: flex; align-items: center; gap: 10px; }
        
        .preview-toolbar { background-color: #252526; padding: 8px 15px; display: flex; align-items: center; border-bottom: 1px solid #333; }
        .preview-address-bar { background-color: #3c3c3c; color: #cccccc; padding: 5px 12px; border-radius: 4px; font-family: 'Inter', sans-serif; font-size: 12px; flex-grow: 1; margin-left: 15px; display: flex; align-items: center; gap: 8px; }
        
        .browser-preview { background-color: #ffffff; position: relative; width: 100%; min-height: 400px; overflow: hidden; }
    </style>
</head>
<body>
<div class="container">
    <div class="vscode-window">
        <div class="vscode-header">
            <div class="vscode-tabs"><div class="vscode-tab">📄 ${source}</div></div>
            <div style="opacity: 0.5; color: #cccccc;">● ○ ◍</div>
        </div>
        <pre class="vscode-content">${highlightedCode}</pre>
    </div>

    <div class="preview-section">
        <span class="preview-label">🌐 Browser Output (Live Preview)</span>
        <div class="vscode-window" style="margin-bottom: 0;">
            <div class="vscode-header">
                <div class="vscode-tabs"><div class="vscode-tab">🌐 Simple Browser</div></div>
                <div style="opacity: 0.5; color: #cccccc;">● ○ ◍</div>
            </div>
            <div class="preview-toolbar">
                <span style="color: #cccccc; cursor: pointer; font-size: 16px;">↻</span>
                <div class="preview-address-bar">
                    <span>🔒</span> http://127.0.0.1:5500/${source}
                </div>
            </div>
            <div class="browser-preview">
                ${bodyContent}
            </div>
        </div>
    </div>
</div>
</body>
</html>`;

  const targetPath = path.join(projectDir, target);
  fs.writeFileSync(targetPath, outputHtml, 'utf8');
  console.log(`Generated ${target}`);
});
