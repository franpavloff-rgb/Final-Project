# Functional Specification — Final Project Website

## Overview

Purpose: Describe functional behavior, pages, UX, assets, and acceptance criteria for the final project website so developers and testers can implement and verify features.

Audience: Developer, reviewer/teacher, tester.

## Goals

- Deliver a responsive, accessible single-page marketing site with sections: Landing, Features, Values, Pricing, Testimonials, CTA, Footer.
- Support easy local development (Live Server) and deployment to GitHub Pages.

## Scope

In-scope:

- UI components, navigation, responsive layout, image assets, client-side interactions (menu, smooth scroll), SEO metadata.

Out-of-scope:

- Backend, authentication, server-side APIs, databases.

## Personas

- Visitor (prospect): Wants product overview, pricing, and contact.
- Admin/Developer: Edits content and pushes updates to GitHub.

## User Flows

1. Open site → view hero + nav.
2. Click a nav link → smooth-scroll to section.
3. On mobile, open the menu → choose a link → navigate.
4. Click CTA → follow to contact or external link.

## Pages & Sections (single-page structure)

- Landing (hero + nav)
- Features
- Quality / Steps (process)
- Values (description, list, illustration)
- Pricing
- Testimonials
- Start / CTA
- Footer

## Components

- `NavBar`: logo, links, mobile menu trigger.
- `Menu Modal`: modal for mobile links; focus trap and keyboard controls.
- `Hero`: H1, subtext, primary CTA.
- `Value Card`: icon, title, paragraph.
- `Image`: use `alt` and correct hashed filenames from `assets/`.
- `Buttons/Links`: consistent classes (`btn`, `nav__link`).

## Behavior & Interaction Requirements

- Breakpoints: mobile ≤600px, tablet 601–1024px, desktop >1024px.
- Menu: open/close on click; ESC closes; clicking overlay closes; focus returns to trigger.
- Smooth scroll to targets; offset for fixed header if used.
- Images: `loading="lazy"` for non-hero images where helpful.
- Scripts: load with `defer` and attach DOM-ready handlers.
- Accessibility: semantic HTML, `alt` text, `aria-label` on controls, keyboard navigable, color contrast >= WCAG AA.

## Data & Assets

- Assets are in the `assets/` folder and referenced with relative paths (e.g. `./assets/prototype-illustration.21bc4b3f612a2f257c3d361067582485.svg`).
- Metadata: `title`, `description`, `viewport`, and basic Open Graph tags.

## Non-functional Requirements

- Performance: reasonable load times locally; avoid blocking resources.
- Browser support: latest two versions of Chrome, Edge, Firefox.
- Security: no inline evals; serve static assets only.

## Acceptance Criteria

- AC-1: Page loads locally at `http://127.0.0.1:5500/` without 404s for referenced assets.
- AC-2: Nav links scroll to correct sections; active state updates on scroll.
- AC-3: Mobile menu opens and closes; ESC closes and focus handling works.
- AC-4: Images render and have meaningful `alt` attributes.
- AC-5: No console errors on load and after typical interactions.
- AC-6: Layout is responsive at defined breakpoints.
- AC-7: Fix is committed and pushed to `origin/main` with descriptive message.

## Testing Checklist

- Manual: load page, click nav links, open/close menu, keyboard navigation, inspect console, verify images.
- Automated suggestions: run W3C HTML validator; run Lighthouse/Axe for accessibility.

## Deployment & CI

- Local preview: Live Server or `python -m http.server 5500`.
- Remote: GitHub Pages via `main` branch (or GH Pages configuration).
- Optional CI: GitHub Action to run linters and Lighthouse on PRs.

## Deliverables

- `SPEC.md` (this file)
- `TESTS.md` (acceptance checklist and commands)
- (Optional) `.github/workflows/lint-and-lh.yml`

## Timeline (suggested)

- Day 1: Finalize spec and basic content.
- Day 2: Implement responsive layout and components.
- Day 3: Accessibility fixes, testing, deploy.
