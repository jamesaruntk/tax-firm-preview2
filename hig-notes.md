# Apple HIG — distilled rules for the tax firm website

Source: Apple Human Interface Guidelines, fetched 2026-10-30 via Apple's JSON data endpoints
(`https://developer.apple.com/tutorials/data/design/human-interface-guidelines/<slug>.json`), which hold the full page text.
Base URL for every page below: `https://developer.apple.com/design/human-interface-guidelines/<slug>`.
Secondary reference: apple.com home page markup and CSS (fetched the same day) for marketing-page conventions.

Pages read (37): accessibility, app-icons, branding, color, dark-mode, icons, images, inclusion, layout, materials,
motion, privacy, right-to-left, sf-symbols, typography, writing · onboarding, entering-data, feedback, loading,
searching, modality, launching · buttons, lists-and-tables, toolbars (*navigation-bars* returns 404; Apple has folded
navigation bars into **Toolbars**), tab-bars, menus, sheets, text-fields, toggles, segmented-controls,
disclosure-controls, labels, collections · designing-for-ios, designing-for-ipados, designing-for-macos.

Note: The HIG is written for native apps. On a website, "points" become CSS px. Native-only APIs such as Dynamic Type,
SF Symbols, and Liquid Glass become their closest web equivalents: rem-based type, inline SVG strokes, and
`backdrop-filter`.

---

## 1. Typography — /typography, /accessibility
- **System font stack, no embedded SF files.** HIG: "don't embed system fonts". Stack:
  `-apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Helvetica Neue", Helvetica, Arial, sans-serif`.
  Apple devices render SF Pro. Other devices fall back to a clean sans. The site uses one typeface family only
  ("Minimize the number of typefaces").
- **Body text 17px, never below 11px.** The iOS default text size is 17pt and the minimum is 11pt (typography & accessibility tables).
- **iOS "Large (default)" text styles → CSS scale** (size / leading):
  Large Title 34/41 · Title 1 28/34 · Title 2 22/28 · Title 3 20/25 · Headline 17/22 semibold · Body 17/22 ·
  Callout 16/21 · Subhead 15/20 · Footnote 13/18 · Caption 12/16. The marketing hero goes past Large Title to match
  apple.com (48–80px, weight 600–700, slight negative tracking -0.015em to -0.003em; apple.com body 17px / -0.022em,
  section heads 40–56px / 600).
- **Avoid light weights.** Use Regular, Medium, Semibold, and Bold. Never Ultralight, Thin, or Light.
- **Build hierarchy from weight, size, and color** (label → secondaryLabel), not from extra fonts.
- **Support text enlargement up to 200%.** Size everything in rem/clamp so browser zoom and text size work.
  Layouts reflow and stack rather than truncate ("Keep text truncation to a minimum"; "use a stacked layout").
- **Leading:** looser for long passages. Never set three or more lines tight.

## 2. Color — /color, /dark-mode, /accessibility
- **Semantic, adaptive colors** defined as CSS custom properties: `--label`, `--secondary-label`, `--bg`,
  `--bg-secondary`, `--grouped-bg`, `--separator`, `--fill`, `--accent`. "Each dynamic color is semantically defined
  by its purpose." Never reuse a role: no separator color for text, no secondaryLabel color for backgrounds.
- **One accent: system blue, applied judiciously** (/branding: "Apply your app's accent color judiciously";
  /color: "Avoid using the same color to mean different things"). Blue means interactive and nothing else.
  Light: links #0066CC (apple.com; 5.6:1 on white). Filled buttons #0071E3 with white text (≈4.6:1).
  Dark: links #2997FF (apple.com dark). The raw iOS systemBlue #007AFF is only ≈4.0:1 on white, which fails AA for
  body text, so the darker web blue is used for text.
- **Neutrals (apple.com palette):** label #1D1D1F, secondary #6E6E73, background #FFFFFF and #F5F5F7.
  Dark: #000000 and #161617, cards #1C1C1E, label #F5F5F7, secondary #A1A1A6.
- **Contrast (WCAG AA per HIG table):** at least 4.5:1 for text up to 17pt, at least 3:1 for text 18pt+ or bold.
  /dark-mode says to aim for 7:1 with custom colors on small text where possible. Check both appearances.
- **Never rely on color alone.** Errors use an icon, text, and color together. Links in body copy are underlined.
- **Increase Contrast:** honor `prefers-contrast: more` with stronger separators and secondary text.

## 3. Dark Mode — /dark-mode
- **Follow the system setting automatically** (`prefers-color-scheme`). "Avoid offering an app-specific appearance
  setting", so the site has no theme toggle.
- **Dark palette = dimmer backgrounds, brighter foregrounds.** It is not a plain inversion. Elevated cards are lighter
  than the base (#1C1C1E on #000).
- Set `color-scheme: light dark` so form controls and scrollbars adapt too.

## 4. Layout & spacing — /layout, /designing-for-ios, /accessibility, apple.com
- **Most important content first, top-leading** (the hero is the value proposition and the primary action).
- **Group related items** with negative space and container shapes (rounded cards, grouped list insets).
- **Progressive disclosure:** the FAQ uses disclosure controls, and service details sit on their own page.
- **Adapt by available width (size classes), not device.** Breakpoints follow apple.com's 734px (compact→regular)
  and 1068px (wide). Content max-width is 980px for text and 1068px for grids. Side margins are 16–20px on phones and
  grow on larger screens.
- **Respect safe areas:** `viewport-fit=cover` + `env(safe-area-inset-*)` padding on the nav and footer.
- **Section rhythm (apple.com):** generous vertical padding (64px mobile → 112px desktop) with alternating
  white and #F5F5F7 bands.
- **Limit on-screen controls** (designing-for-ios): one primary action per view. Put controls within easy reach
  and keep a full-width CTA on phones.

## 5. Touch targets & control spacing — /accessibility, /buttons
- **44×44pt default minimum hit target on iOS/iPadOS** (28×28 absolute minimum). Every link, button, menu item,
  summary row, and input is at least 44px tall.
- **Spacing:** about 12pt of padding around bezeled controls and about 24pt around bezel-less ones.
- **Buttons:** a prominent (filled) style for the single most likely action, and style rather than size to set it
  apart from secondary actions. Always include a pressed state. Labels start with a verb ("Book a consultation",
  "Send message"). The submit button shows progress when an action isn't instant.

## 6. Materials & navigation — /materials, /toolbars, /tab-bars
- **Controls float on a translucent material layer above content.** Liquid Glass is "a distinct functional layer
  for controls and navigation". Do not use the material in the content layer. Use it sparingly.
- **Web equivalent (apple.com):** `background: rgba(250,250,252,.8)` plus `backdrop-filter: saturate(180%) blur(20px)`.
  Dark: `rgba(22,22,23,.8)`. Solid fallback when unsupported, and with `prefers-reduced-transparency`.
- **Nav bar height 44px** (apple.com globalnav). Items are chosen deliberately to avoid crowding. On narrow widths
  they collapse into a menu (/toolbars: "Add a More menu", /menus). Labels are short title-case nouns.
- Navigation is for going places, not actions (/tab-bars). The one action, "Book a consultation", is a prominent
  button.
- **Mobile menu = a lightweight modal** (/modality). It has an obvious way to dismiss: the close button, Esc, or a
  link tap. Focus moves in and back out, and it never stacks with another modal.

## 7. Motion — /motion, /accessibility
- **Motion is purposeful and optional.** Use short fades only (~200–300ms) for the menu, the disclosure chevron, and
  the button press. No parallax, auto-play, or looping.
- **Honor Reduce Motion:** `prefers-reduced-motion: reduce` turns off transforms, smooth scroll, and transitions,
  swapping movement for instant or fade changes.
- No timed auto-dismiss UI (/accessibility, Cognitive).

## 8. Writing & tone — /writing, /inclusion, /branding
- **Voice for a financial firm: trust and stability** (/writing gives a banking app as its example). Copy is clear,
  calm, and plain. Cut every unneeded word.
- **Plain, inclusive language.** Define tax jargon (e.g. "estimated taxes", "IRS notice"). No gendered terms, no
  colloquialisms, no "oops".
- **Action-oriented labels** with verbs. Never "Click here"; links say where they go.
- **Consistent capitalization:** Title Case for nav and buttons, Sentence case for headlines and body.
- **Error messages sit next to the field,** don't blame, and say how to fix the problem
  ("Enter an email address, like name@example.com"). Avoid "we" in error and status messages.
- **Possessives used sparingly.**
- **Branding defers to content.** No logo everywhere, only a text wordmark in the nav.

## 9. Forms — /entering-data, /text-fields, /privacy, /feedback
- **Ask only for data you need** (/privacy): name, email, optional phone, and message. **No SSNs, no
  account/financial numbers**, and the form says so plainly.
- Each field has a visible label and a hint. Use `type=email` / `type=tel` and `autocomplete` so the right keyboard
  appears and system autofill can supply data ("Get information from the system whenever possible").
- Offer a choice instead of typing where possible (an optional "Topic" select).
- Mark required fields clearly. Validate on blur and submit, and show errors inline with `aria-invalid` and
  `aria-describedby`.
- Confirm completion with a polite live-region status message (/feedback). Be transparent about data use with a
  privacy note next to the submit button.

## 10. Disclosure, lists, collections — /disclosure-controls, /lists-and-tables, /collections
- The FAQ uses native `<details>/<summary>`. Each chevron points trailing when closed and down when open, and every
  row has a descriptive label (the question itself).
- **Text belongs in lists, not image collections.** Services are cards with short succinct titles, and longer
  service detail uses lists.

## 11. Icons & images — /icons, /sf-symbols, /images
- Icons are simple and consistent: inline SVG line icons in an SF-Symbols-like style, with stroke weight matched
  to the adjacent text weight. Decorative icons use `aria-hidden="true"`, and meaningful ones get text labels.
- Vector (SVG) only, so everything is sharp at every pixel density. No replicas of Apple hardware or Apple logos.

## 12. Accessibility (general) — /accessibility, /inclusion
- **Semantic HTML:** landmarks (`header`, `nav`, `main`, `footer`), one `h1` per page, ordered headings, and a skip
  link.
- **Full keyboard access** with a visible `:focus-visible` ring (3px accent). No keyboard traps.
- **VoiceOver:** `aria-expanded`/`aria-controls` on the menu button, `aria-current="page"` on the current nav item,
  labelled regions, and alt text.
- Text stays selectable (/labels: "Make useful label text selectable").
- **RTL readiness** (/right-to-left): CSS logical properties (`margin-inline`, `padding-inline-start`,
  `inset-inline-end`).

## 13. Launch/loading — /launching, /loading, /onboarding
- **Show content instantly.** No splash screen, no preloader, no interstitial pop-ups, and no "advertising" overlays.
  Static HTML with system fonts means no font download delay.
