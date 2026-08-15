<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
<link href="https://fonts.googleapis.com" rel="preconnect" />
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect" />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet" />
<style type="text/css">/* --- RESET & BASE --- */
        * {
            box-sizing: border-box;
        }

        body {
            background-color: #ffffff;
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #334155;
        }

        /* --- HEADER --- */
        header {
            background: #ffffff;
            padding: 50px 20px 30px;
            text-align: center;
            border-bottom: 1px solid #e2e8f0;
        }

        header h1 {
            margin: 0;
            font-size: 2.5em;
            font-weight: 800;
            color: #50aae0;
        }

        header p {
            font-size: 1.1em;
            color: #64748b;
            max-width: 700px;
            margin: 15px auto 0;
        }

        /* --- DASHBOARD --- */
        .dashboard {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(480px, 1fr));
            gap: 30px;
        }

        @media (max-width: 520px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
        }

        /* --- CARD --- */
        .card {
            background-color: #f8fafc;
            border: 1px solid #cbd5e1;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 25px -5px rgba(0, 0, 0, 0.1);
        }

        .card-header {
            background-color: #f1f5f9;
            padding: 15px 25px;
            border-bottom: 1px solid #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .card-header h2 {
            margin: 0;
            font-size: 1.25em;
            color: #1e293b;
            font-weight: 700;
        }

        .icon-badge {
            background: white;
            padding: 8px;
            border-radius: 8px;
            font-size: 1.2em;
            border: 1px solid #e2e8f0;
        }

        .card-body {
            padding: 25px;
        }

        /* --- UTILITIES --- */
        .full-width {
            grid-column: 1 / -1;
        }

        .section-title {
            grid-column: 1 / -1;
            font-size: 1.5em;
            font-weight: 700;
            color: #1e293b;
            margin-top: 20px;
            margin-bottom: -10px;
            padding-left: 10px;
            border-left: 5px solid #50aae0;
        }

        .tag {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.75em;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 12px;
        }

        .tag-blue {
            background: #e0f2fe;
            color: #0284c7;
            border: 1px solid #bae6fd;
        }

        .tag-green {
            background: #dcfce7;
            color: #16a34a;
            border: 1px solid #bbf7d0;
        }

        .tag-red {
            background: #fee2e2;
            color: #dc2626;
            border: 1px solid #fca5a5;
        }

        .tag-orange {
            background: #ffedd5;
            color: #c2410c;
            border: 1px solid #fdba74;
        }

        code {
            background: #f1f5f9;
            color: #db2777;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            border: 1px solid #e2e8f0;
        }

        /* --- CODE BLOCK --- */
        pre {
            background: #1e293b;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Consolas', monospace;
            font-size: 0.9em;
            margin: 15px 0;
        }

        .code-comment {
            color: #6a9955;
        }

        .code-keyword {
            color: #569cd6;
        }

        .code-string {
            color: #ce9178;
        }

        .code-function {
            color: #dcdcaa;
        }

        .code-number {
            color: #b5cea8;
        }

        /* --- TABLE --- */
        .table-responsive {
            overflow-x: auto;
            margin-top: 15px;
        }

        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
            min-width: 400px;
        }

        thead {
            background-color: #50aae0;
        }

        thead th {
            color: #fff;
            padding: 14px 16px;
            text-align: left;
            font-weight: 600;
        }

        tbody td {
            padding: 14px 16px;
            border-bottom: 1px solid #e6eaf0;
            color: #475569;
        }

        tbody tr:last-child td {
            border-bottom: none;
        }

        tbody tr:nth-child(even) {
            background-color: #f9fbff;
        }

        /* --- WARNING / INFO BOX --- */
        .warning-box {
            background: #fef2f2;
            border: 1px solid #fecaca;
            border-left: 4px solid #ef4444;
            padding: 15px 20px;
            border-radius: 8px;
            margin-top: 15px;
            color: #991b1b;
        }

        .info-box {
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            border-left: 4px solid #3b82f6;
            padding: 15px 20px;
            border-radius: 8px;
            margin-top: 15px;
            color: #1e40af;
        }

        /* --- VISUAL: FLOWCHART --- */
        .flowchart {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            padding: 25px;
            background: #f0f9ff;
            border-radius: 12px;
            margin-top: 15px;
        }

        .flow-box {
            background: white;
            border: 2px solid #50aae0;
            border-radius: 8px;
            padding: 12px 25px;
            font-weight: 600;
            color: #1e293b;
            text-align: center;
            min-width: 150px;
        }

        .flow-box.diamond {
            background: #fef9c3;
            border-color: #eab308;
        }

        .flow-box.action {
            background: #dcfce7;
            border-color: #22c55e;
        }

        .flow-box.danger {
            background: #fee2e2;
            border-color: #ef4444;
        }

        .flow-arrow {
            font-size: 1.5em;
            color: #94a3b8;
        }

        .flow-row {
            display: flex;
            gap: 30px;
            align-items: center;
        }

        /* --- COMPARE --- */
        .compare-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 15px;
        }

        @media (max-width: 600px) {
            .compare-grid {
                grid-template-columns: 1fr;
            }
        }

        .compare-box {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 15px;
        }

        .compare-box.good {
            border-color: #86efac;
            background: #f0fdf4;
        }

        .compare-box.bad {
            border-color: #fca5a5;
            background: #fef2f2;
        }

        .compare-label {
            font-weight: 700;
            margin-bottom: 10px;
        }

        /* --- VISUAL: TERMINAL OUTPUT --- */
        .terminal-demo {
            background: #0f172a;
            border-radius: 10px;
            overflow: hidden;
            margin-top: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }

        .terminal-header {
            background: #1e293b;
            padding: 10px 15px;
            display: flex;
            gap: 8px;
        }

        .terminal-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }

        .dot-red { background: #ef4444; }
        .dot-yellow { background: #eab308; }
        .dot-green { background: #22c55e; }

        .terminal-body {
            padding: 20px;
            font-family: 'Consolas', monospace;
            color: #22c55e;
            font-size: 0.95em;
        }

        .terminal-prompt { color: #64748b; }
        .terminal-output { color: #e2e8f0; margin-top: 5px; }

        footer {
            text-align: center;
            padding: 40px 20px 60px;
            color: #94a3b8;
            font-size: 0.85em;
        }
</style>
<header>
<h1>&nbsp;The While Loop</h1>

<p>Repeat code as long as a condition remains true.</p>
</header>

<div class="dashboard"><!-- ======== INTRO ======== -->
<div class="section-title">What is a While Loop?</div>

<div class="card full-width">
<div class="card-content">
<div class="card-header">
<h2>Repeating If Statement</h2>
<span class="icon-badge">🔄</span></div>

<div class="card-body"><span class="tag tag-blue">Definition</span>

<p>A <strong>while loop</strong> repeatedly executes code <strong>as long as</strong> a condition is <code>True</code>.</p>

<p>Think: <em>&quot;If condition is true, do this. Check again. If still true, do again.&quot;</em></p>

<div class="flowchart">
<div class="flow-box">Start</div>

<div class="flow-arrow">&darr;</div>

<div class="flow-box diamond">Condition True?</div>

<div class="flow-row">
<div>
<div style="color: #22c55e; font-weight: bold;">Yes &darr;</div>

<div class="flow-box action">Run Body</div>

<div class="flow-arrow">&darr;</div>

<div style="color: #50aae0;">&uarr; Loop back</div>
</div>

<div>
<div style="color: #ef4444; font-weight: bold;">No &rarr;</div>

<div class="flow-box">Exit</div>
</div>
</div>
</div>

<p style="margin-top: 18px;">Notice the flowchart checks the condition <strong>before</strong> every single run of the body &mdash; including the very first one. If the condition starts out <code>False</code>, the body never runs at all:</p>

<pre>
count = <span class="code-number">10</span>

<span class="code-keyword">while</span> count &lt; <span class="code-number">5</span>:
    <span class="code-function">print</span>(<span class="code-string">&quot;This never prints&quot;</span>)

<span class="code-function">print</span>(<span class="code-string">&quot;Loop skipped entirely&quot;</span>)</pre>

<div class="terminal-demo">
<div class="terminal-header">
<div class="terminal-dot dot-red">&nbsp;</div>

<div class="terminal-dot dot-yellow">&nbsp;</div>

<div class="terminal-dot dot-green">&nbsp;</div>
</div>

<div class="terminal-body">
<div><span class="terminal-prompt">$ python main.py</span></div>

<div class="terminal-output">Loop skipped entirely</div>
</div>
</div>

<div class="info-box"><strong>💡 for vs. while:</strong> Use a <code>for</code> loop when you know how many times to repeat (a fixed sequence). Use a <code>while</code> loop when you don&#39;t know in advance &mdash; you just want to keep going until some condition changes.</div>
</div>
</div>
</div>
<!-- ======== BASICS ======== -->

<div class="section-title">1. While Loop Basics</div>

<div class="card full-width">
<div class="card-content">
<div class="card-header">
<h2>Countdown Example</h2>
<span class="icon-badge">⏱️</span></div>

<div class="card-body"><span class="tag tag-green">Example</span>

<pre>
<span class="code-comment"># Countdown</span>
count = <span class="code-number">5</span>

<span class="code-keyword">while</span> count &gt; <span class="code-number">0</span>:      <span class="code-comment"># Condition</span>
    <span class="code-function">print</span>(count)     <span class="code-comment"># Body</span>
    count -= <span class="code-number">1</span>       <span class="code-comment"># Update (CRUCIAL!)</span>

<span class="code-function">print</span>(<span class="code-string">&quot;Liftoff!&quot;</span>)

<span class="code-comment"># Output: 5 4 3 2 1 Liftoff!</span></pre>

<div class="terminal-demo">
<div class="terminal-header">
<div class="terminal-dot dot-red">&nbsp;</div>

<div class="terminal-dot dot-yellow">&nbsp;</div>

<div class="terminal-dot dot-green">&nbsp;</div>
</div>

<div class="terminal-body">
<div><span class="terminal-prompt">$ python main.py</span></div>

<div class="terminal-output">5<br />
4<br />
3<br />
2<br />
1<br />
Liftoff!</div>
</div>
</div>

<div class="table-responsive">
<table>
	<thead>
		<tr>
			<th>Part</th>
			<th>Purpose</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><code>while</code></td>
			<td>Loop keyword</td>
		</tr>
		<tr>
			<td><strong>Condition</strong></td>
			<td>Boolean checked before each repetition</td>
		</tr>
		<tr>
			<td><strong>Body</strong></td>
			<td>Indented code that runs if True</td>
		</tr>
		<tr>
			<td><strong>Update</strong></td>
			<td>Modifies variable to eventually stop loop</td>
		</tr>
	</tbody>
</table>
</div>

<p style="margin-top: 18px;"><strong>Tracing through it step by step</strong> helps make the mechanics click:</p>

<div class="table-responsive">
<table>
	<thead>
		<tr>
			<th>Iteration</th>
			<th>Check: <code>count &gt; 0</code></th>
			<th>Prints</th>
			<th>After update</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>5 &gt; 0 &rarr; True</td>
			<td>5</td>
			<td>count = 4</td>
		</tr>
		<tr>
			<td>2</td>
			<td>4 &gt; 0 &rarr; True</td>
			<td>4</td>
			<td>count = 3</td>
		</tr>
		<tr>
			<td>3</td>
			<td>3 &gt; 0 &rarr; True</td>
			<td>3</td>
			<td>count = 2</td>
		</tr>
		<tr>
			<td>4</td>
			<td>2 &gt; 0 &rarr; True</td>
			<td>2</td>
			<td>count = 1</td>
		</tr>
		<tr>
			<td>5</td>
			<td>1 &gt; 0 &rarr; True</td>
			<td>1</td>
			<td>count = 0</td>
		</tr>
		<tr>
			<td>6</td>
			<td>0 &gt; 0 &rarr; <strong>False</strong></td>
			<td>&mdash;</td>
			<td>loop exits</td>
		</tr>
	</tbody>
</table>
</div>

<p style="margin-top: 18px;"><strong>A while loop that builds something up</strong>, rather than counting down &mdash; accumulating a total until it crosses a threshold:</p>

<pre>
savings = <span class="code-number">0</span>
target = <span class="code-number">100</span>
week = <span class="code-number">0</span>

<span class="code-keyword">while</span> savings &lt; target:
    savings += <span class="code-number">25</span>
    week += <span class="code-number">1</span>
    <span class="code-function">print</span>(<span class="code-string">&quot;Week&quot;</span>, week, <span class="code-string">&quot;- saved:&quot;</span>, savings)

<span class="code-function">print</span>(<span class="code-string">&quot;Goal reached!&quot;</span>)</pre>

<div class="terminal-demo">
<div class="terminal-header">
<div class="terminal-dot dot-red">&nbsp;</div>

<div class="terminal-dot dot-yellow">&nbsp;</div>

<div class="terminal-dot dot-green">&nbsp;</div>
</div>

<div class="terminal-body">
<div><span class="terminal-prompt">$ python main.py</span></div>

<div class="terminal-output">Week 1 - saved: 25<br />
Week 2 - saved: 50<br />
Week 3 - saved: 75<br />
Week 4 - saved: 100<br />
Goal reached!</div>
</div>
</div>
</div>
</div>
</div>
<!-- ======== INFINITE LOOPS ======== -->

<div class="section-title">2. Avoiding Infinite Loops</div>

<div class="card full-width">
<div class="card-content">
<div class="card-header">
<h2>The Update Step</h2>
<span class="icon-badge">⚠️</span></div>

<div class="card-body"><span class="tag tag-red">Danger</span>

<div class="warning-box"><strong>⚠️ Infinite Loop:</strong> If you forget the <strong>Update</strong> step, the condition stays true forever and your program crashes (or hangs) until you force-stop it!</div>

<div class="compare-grid">
<div class="compare-box good">
<div class="compare-label">✅ Safe Pattern</div>

<pre style="margin: 0; font-size: 0.85em;">
value = <span class="code-number">0</span>

<span class="code-keyword">while</span> value &lt; <span class="code-number">10</span>:
    <span class="code-function">print</span>(value)
    value += <span class="code-number">1</span>  <span class="code-comment"># Updates!</span></pre>
</div>

<div class="compare-box bad">
<div class="compare-label">❌ Infinite (Don&#39;t Run!)</div>

<pre style="margin: 0; font-size: 0.85em;">
<span class="code-keyword">while</span> <span class="code-keyword">True</span>:
    <span class="code-function">print</span>(<span class="code-string">&quot;Stuck!&quot;</span>)
<span class="code-comment"># No way to stop</span></pre>
</div>
</div>

<p style="margin-top: 18px;"><strong>A sneakier version of the same bug</strong> &mdash; the update step exists, but it never actually moves the condition toward False:</p>

<pre>
count = <span class="code-number">5</span>

<span class="code-keyword">while</span> count &gt; <span class="code-number">0</span>:
    <span class="code-function">print</span>(count)
    count += <span class="code-number">1</span>  <span class="code-comment"># Oops &mdash; going up, not down!</span>
    <span class="code-comment"># count &gt; 0 will NEVER become False now</span></pre>

<div class="warning-box"><strong>⚠️ Common mistake:</strong> Updating the wrong direction (<code>+=</code> instead of <code>-=</code>, or vice versa) is one of the most common causes of infinite loops. Always double-check that your update actually pushes the condition toward becoming <code>False</code>.</div>

<p style="margin-top: 18px;"><strong><code>while True</code> is sometimes intentional</strong> &mdash; for example, a menu that keeps asking until the user chooses to quit &mdash; but it always needs an escape hatch, usually a <code>break</code> statement:</p>

<pre>
attempts = <span class="code-number">0</span>

<span class="code-keyword">while</span> <span class="code-keyword">True</span>:
    attempts += <span class="code-number">1</span>
    <span class="code-function">print</span>(<span class="code-string">&quot;Attempt&quot;</span>, attempts)
    <span class="code-keyword">if</span> attempts == <span class="code-number">3</span>:
        <span class="code-function">print</span>(<span class="code-string">&quot;Done!&quot;</span>)
        <span class="code-keyword">break</span>  <span class="code-comment"># Exits the loop manually</span></pre>

<div class="terminal-demo">
<div class="terminal-header">
<div class="terminal-dot dot-red">&nbsp;</div>

<div class="terminal-dot dot-yellow">&nbsp;</div>

<div class="terminal-dot dot-green">&nbsp;</div>
</div>

<div class="terminal-body">
<div><span class="terminal-prompt">$ python main.py</span></div>

<div class="terminal-output">Attempt 1<br />
Attempt 2<br />
Attempt 3<br />
Done!</div>
</div>
</div>

<div class="info-box"><strong>💡 Tip:</strong> Whenever you write <code>while True:</code>, immediately ask yourself: &quot;Where&#39;s the <code>break</code>?&quot; If you can&#39;t answer that, the loop is probably a bug waiting to happen.</div>
</div>
</div>
</div>
</div>
