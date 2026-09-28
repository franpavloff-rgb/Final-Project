import pathlib
import sys
try:
    import markdown
except Exception:
    print('markdown module not found; please run: python -m pip install --user markdown')
    sys.exit(2)
md = pathlib.Path('SPEC.md').read_text(encoding='utf-8')
html_body = markdown.markdown(md, extensions=['fenced_code','tables'])
html = """<!doctype html>
<html>
<head>
<meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>Functional Specification</title>
<style>
body{font-family:Arial, Helvetica, sans-serif; margin:28px; line-height:1.5}
pre{background:#f6f8fa;padding:12px;border-radius:6px;overflow:auto}
code{background:#f2f4f6;padding:2px 4px;border-radius:4px}
h1,h2,h3{color:#111}
</style>
</head>
<body>
""" + html_body + """
</body>
</html>"""
pathlib.Path('SPEC.html').write_text(html, encoding='utf-8')
print('WROTE SPEC.html')
