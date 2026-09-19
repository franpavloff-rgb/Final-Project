# TESTS — Acceptance Checklist and Commands

## Manual Acceptance Tests

- AC-1: Start local server and load the page
  - Expected: Page loads without 404s for referenced assets.

- AC-2: Navigation links
  - Action: Click each nav link.
  - Expected: Smooth scroll to the correct section; check active state.

- AC-3: Mobile menu behavior
  - Action: Resize to mobile or emulate; click menu button, press ESC, click overlay.
  - Expected: Menu opens; ESC closes it; overlay click closes it; focus returns to menu button.

- AC-4: Images and alt text
  - Action: Inspect each `img` element.
  - Expected: Each image has an `alt` attribute and renders.

- AC-5: Console errors
  - Action: Open DevTools console and reload.
  - Expected: No uncaught errors or missing resource 404s.

- AC-6: Responsive layout
  - Action: Resize window to mobile/tablet/desktop or use device toolbar.
  - Expected: Layout adapts correctly without overlapping or layout breakage.

## Automated / Tool Checks (recommended)

- Run HTML validation (W3C): copy-paste `index.html` or use CLI validator.
- Run Lighthouse (Chrome) for accessibility and performance.
- Run axe-core for accessibility rules.

## Local commands

Start Live Server (VS Code Live Server extension):

```powershell
# In VS Code, press 'Go Live' or run command palette: Live Server: Open with Live Server
```

Start a simple Python server (alternative):

```powershell
cd "c:\Users\franp\OneDrive\Documents\GitHub\final project"
python -m http.server 5500
# then open http://127.0.0.1:5500/
```

Run Lighthouse from Chrome DevTools (manual):

- Open DevTools → Lighthouse → Generate report.

Run a basic axe check (npm):

```bash
# optional, requires node and axe-cli
npm install -g axe-cli
axe http://127.0.0.1:5500/
```

## How to mark tests as passed

- Update `TESTS.md` with the date and verifier's initials next to each passed AC.
