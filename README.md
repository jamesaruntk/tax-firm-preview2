# Tax firm preview

A mobile-first marketing site for a tax firm, styled after Apple’s Human Interface Guidelines. Firm name, contact details, and credentials are clearly marked placeholders (`[Your Firm Name]`, address, phone, email, and credential blocks tagged Placeholder). Replace those before launch.

## Pages

- `index.html` — home
- `services.html` — services
- `about.html` — about
- `faq.html` — FAQ
- `contact.html` — contact

Shared styles, script, and icon live in `assets/`. Design notes are in `hig-notes.md`. Preview screenshots are in `screenshots/`.

## Preview locally

Open `index.html` in a browser, or from this directory:

```bash
python3 -m http.server
```

Then visit `http://localhost:8000`.

## Contact form

The contact form is front-end only. It checks the fields in the browser and shows a confirmation, but it does not send a message. Connect a form service before launch.
