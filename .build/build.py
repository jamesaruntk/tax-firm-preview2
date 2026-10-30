# Generates the static pages with a shared header/footer. Output: /workspace/tax-site/*.html
import os
OUT = "/workspace/tax-site"
FIRM = "[Your Firm Name] Tax &amp; Advisory"
FIRM_SHORT = "[Your Firm Name]"

def svg(path, extra=""):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"{extra}>{path}</svg>'

I = {
 "person": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-6.5 8-6.5s8 2.5 8 6.5"/>',
 "building": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M9 7h1M14 7h1M9 11h1M14 11h1M9 15h1M14 15h1M10 21v-3h4v3"/>',
 "book": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/><path d="M8 7h8M8 11h6"/>',
 "chart": '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/>',
 "shield": '<path d="M12 3 4 6v6c0 4.5 3.4 8.2 8 9 4.6-.8 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
 "check": '<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
 "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
 "lock": '<rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "doc": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
 "pin": '<path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.01"/>',
 "alert": '<circle cx="12" cy="12" r="9"/><path d="M12 7v6M12 16.5v.01"/>',
 "chev": '<path d="m9 6 6 6-6 6"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "close": '<path d="M6 6l12 12M18 6 6 18"/>',
 "mark": '<path d="M7 4h10M7 4v16M7 12h7"/><path d="M15 16l2 2 4-4" />',
 "people": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c0-3.6 2.9-6 6.5-6s6.5 2.4 6.5 6"/><path d="M16 4.6a3.5 3.5 0 0 1 0 6.8M18 14.3c2.1.7 3.5 2.6 3.5 5.7"/>',
}
def ic(name, cls="icon"):
    return f'<span class="{cls}">{svg(I[name])}</span>'
CHEV = svg(I["chev"])

NAV = [("index.html","Home"),("services.html","Services"),("about.html","About"),("faq.html","FAQ"),("contact.html","Contact")]

def page(fname, title, desc, body):
    links = "\n".join(
        f'          <li><a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="color-scheme" content="light dark">
  <meta name="theme-color" content="#fafafc" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#161617" media="(prefers-color-scheme: dark)">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/styles.css">
  <script>document.documentElement.classList.add('js')</script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  <header class="nav">
    <nav class="nav__bar" aria-label="Main">
      <a class="brand" href="index.html" aria-label="{FIRM}, home">
        <span class="brand__mark">{svg(I["mark"])}</span>
        <span class="brand__name">{FIRM_SHORT}</span>
      </a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-menu" aria-label="Open menu">
        <span class="icon-open">{svg(I["menu"])}</span>
        <span class="icon-close">{svg(I["close"])}</span>
      </button>
      <div class="nav__menu" id="site-menu">
        <ul class="nav__links">
{links}
        </ul>
        <div class="nav__cta"><a class="btn btn--primary btn--sm" href="contact.html">Book a Consultation</a></div>
      </div>
    </nav>
  </header>

  <main id="main" tabindex="-1">
{body}
  </main>

  <footer class="footer">
    <div class="wrap">
      <div class="footer__grid">
        <div>
          <h2>{FIRM}</h2>
          <p>Tax preparation, planning, and bookkeeping for individuals and small businesses in the Maryland and DC area.<span class="ph-tag">Placeholder</span></p>
          <p>[Street address], Hyattsville, MD [ZIP]<span class="ph-tag">Placeholder</span><br>
             (000) 000-0000 · hello@[yourfirm].com<span class="ph-tag">Placeholder</span></p>
        </div>
        <div>
          <h2>Explore</h2>
          <ul>
            <li><a href="services.html">Services</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="faq.html">FAQ</a></li>
          </ul>
        </div>
        <div>
          <h2>Get in Touch</h2>
          <ul>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="contact.html#contact-form">Book a Consultation</a></li>
          </ul>
        </div>
      </div>
      <div class="footer__legal">
        <p>Information on this site is general and isn’t tax, legal, or accounting advice for your situation. Please don’t send Social Security numbers or financial account details by email or web form.</p>
        <p>© <span data-year>2026</span> {FIRM}. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script src="assets/main.js" defer></script>
</body>
</html>
'''

def card(icon, title, text, href=None, link=None):
    l = f'<a class="text-link" href="{href}">{link}<span class="visually-hidden"> about {title}</span> {CHEV}</a>' if href else ""
    return f'''          <article class="card">
            {ic(icon)}
            <h3 class="title-3">{title}</h3>
            <p>{text}</p>
            {l}
          </article>'''

SERVICES = [
 ("person","Individual Tax Preparation","individual","Accurate federal and state returns for W-2 earners, families, retirees, and people with side income."),
 ("building","Small Business Tax","business","Returns for sole proprietors, LLCs, partnerships, and S corporations, plus quarterly estimated taxes."),
 ("book","Bookkeeping","bookkeeping","Monthly bookkeeping and clean financial statements, so tax time is calm and decisions are easier."),
 ("chart","Tax Planning","planning","Year-round planning that looks ahead, so you can make choices that lower what you owe, legally."),
 ("shield","IRS Notice &amp; Audit Help","irs","Got a letter from the IRS or state? Get a clear explanation, a plan, and help responding."),
]

# ------------------------------ HOME ------------------------------
home = f'''    <section class="hero" aria-labelledby="hero-title">
      <div class="wrap">
        <p class="eyebrow">Serving the Maryland and DC area<span class="ph-tag">Placeholder</span></p>
        <h1 id="hero-title" class="large-title">Taxes, made clear.</h1>
        <p class="lede">Tax preparation, planning, and bookkeeping for individuals and small businesses — explained in plain language.</p>
        <div class="btn-row btn-row--stack">
          <a class="btn btn--primary btn--lg" href="contact.html">Book a Consultation</a>
          <a class="btn btn--secondary btn--lg" href="services.html">Explore Services</a>
        </div>
        <div class="hero__panel" role="list" aria-label="At a glance">
          <div class="stat" role="listitem">{ic("calendar")}<div><p class="headline" style="margin:0">Year-round support</p><p class="footnote" style="margin:0">Not just in April.</p></div></div>
          <div class="stat" role="listitem">{ic("chat")}<div><p class="headline" style="margin:0">Plain-language answers</p><p class="footnote" style="margin:0">No jargon, no guesswork.</p></div></div>
          <div class="stat" role="listitem">{ic("lock")}<div><p class="headline" style="margin:0">Private by design</p><p class="footnote" style="margin:0">Sensitive documents are shared only through secure channels.</p></div></div>
        </div>
      </div>
    </section>

    <section class="section section--alt" aria-labelledby="services-title">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">Services</p>
          <h2 id="services-title" class="title-1">Help for every part of tax season.</h2>
          <p class="lede">Choose one service or combine them. Every engagement starts with a short conversation about what you need.</p>
        </div>
        <div class="grid grid--3">
{chr(10).join(card(i,t,d,f"services.html#{a}","Learn more") for i,t,a,d in SERVICES)}
          <article class="card">
            {ic("chat")}
            <h3 class="title-3">Not sure where to start?</h3>
            <p>Describe your situation and get pointed to the right service — no commitment.</p>
            <a class="text-link" href="contact.html">Ask a question {CHEV}</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="why-title">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">Why choose us</p>
          <h2 id="why-title" class="title-1">Careful work. Clear communication.</h2>
        </div>
        <div class="grid grid--2">
          <div>
            <ul class="checklist">
              <li>{svg(I["check"])}<div><p class="headline" style="margin:0">One point of contact</p><p class="secondary" style="margin:0">Work with the same person from first call to filed return.</p></div></li>
              <li>{svg(I["check"])}<div><p class="headline" style="margin:0">Upfront pricing</p><p class="secondary" style="margin:0">Know the fee before any work begins. No surprise invoices.</p></div></li>
              <li>{svg(I["check"])}<div><p class="headline" style="margin:0">Answers you can understand</p><p class="secondary" style="margin:0">Every return comes with a plain-language summary of what changed and why.</p></div></li>
              <li>{svg(I["check"])}<div><p class="headline" style="margin:0">Local and remote</p><p class="secondary" style="margin:0">Meet in person in the Hyattsville area or online, whichever is easier.<span class="ph-tag">Placeholder</span></p></div></li>
            </ul>
          </div>
          <div class="placeholder" role="note" aria-label="Placeholder for credentials">
            <p><strong>Credentials &amp; experience</strong><span class="ph-tag">Placeholder</span></p>
            <p>Add the firm’s real credentials here — for example CPA or Enrolled Agent status, IRS PTIN, professional memberships, and years in practice. Leave this out until the details are confirmed.</p>
            <p style="margin:0"><strong>Client testimonials</strong><span class="ph-tag">Placeholder</span><br>Add real, permission-granted client quotes. No sample testimonials are shown.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt" aria-labelledby="how-title">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">How it works</p>
          <h2 id="how-title" class="title-1">Four simple steps.</h2>
        </div>
        <ol class="steps">
          <li class="step"><h3 class="title-3">Book a consultation</h3><p>Pick a time that works. A short call covers your situation and the fee.</p></li>
          <li class="step"><h3 class="title-3">Share documents securely</h3><p>Get a checklist of what to gather, and upload it through a secure portal — never by email.</p></li>
          <li class="step"><h3 class="title-3">Review together</h3><p>Go over your return or plan line by line, with time for every question.</p></li>
          <li class="step"><h3 class="title-3">File with confidence</h3><p>Your return is filed electronically, and you get copies for your records.</p></li>
        </ol>
      </div>
    </section>

    <section class="section cta" aria-labelledby="cta-title">
      <div class="wrap">
        <h2 id="cta-title" class="title-1">Ready for a calmer tax season?</h2>
        <p class="lede">Start with a no-pressure conversation about what you need.</p>
        <div class="btn-row btn-row--stack">
          <a class="btn btn--primary btn--lg" href="contact.html">Book a Consultation</a>
          <a class="btn btn--secondary btn--lg" href="faq.html">Read the FAQ</a>
        </div>
      </div>
    </section>'''

# ------------------------------ SERVICES ------------------------------
DETAILS = {
 "individual": (["W-2, 1099, and self-employment income","Itemized deductions and credits, like the Child Tax Credit","Rental property, investments, and retirement income","Prior-year and amended returns","Federal, Maryland, DC, and Virginia returns<span class=\"ph-tag\">Confirm</span>"],
   "Good for people who want their return done right and explained clearly."),
 "business": (["Schedule C, partnership (1065), and S corporation (1120-S) returns","Quarterly estimated tax payments — money paid to the IRS during the year instead of all at once","Payroll and 1099 contractor reporting","Entity choice: whether an LLC or S corporation fits","Maryland business and personal property filings<span class=\"ph-tag\">Confirm</span>"],
   "Good for owners who want to spend less time on paperwork and more time on the business."),
 "bookkeeping": (["Monthly categorizing and bank reconciliation","Profit and loss statement and balance sheet each month","Cleanup of past months that fell behind","Setup help for common accounting software"],
   "Good for businesses that want clean numbers all year, not just at tax time."),
 "planning": (["A mid-year check-in to avoid surprises in April","Strategies for retirement contributions and deductions","Planning around big life events: a new job, home, child, or business","Projections so you know roughly what you’ll owe"],
   "Good for anyone whose income or life is changing."),
 "irs": (["A plain-language explanation of what the notice means","Response letters and documentation","Payment plans and penalty relief requests","Representation during an audit<span class=\"ph-tag\">Requires credential — confirm</span>"],
   "Good for anyone who opened a letter from the IRS or state and isn’t sure what to do next."),
}
svc_blocks = []
for i,t,a,d in SERVICES:
    items, fit = DETAILS[a]
    lis = "\n".join(f'              <li>{svg(I["check"])}<span>{x}</span></li>' for x in items)
    svc_blocks.append(f'''        <article class="service" id="{a}" aria-labelledby="{a}-title">
          <div class="service__intro">
            {ic(i)}
            <h2 id="{a}-title" class="title-2">{t}</h2>
            <p class="secondary">{d}</p>
            <p class="footnote">{fit}</p>
          </div>
          <div>
            <h3 class="headline">What’s included</h3>
            <ul class="checklist">
{lis}
            </ul>
            <p class="footnote" style="margin-top:1rem">Pricing: [Add starting price or “quoted after consultation”]<span class="ph-tag">Placeholder</span></p>
          </div>
        </article>''')

services = f'''    <section class="page-hero" aria-labelledby="page-title">
      <div class="wrap">
        <p class="eyebrow">Services</p>
        <h1 id="page-title" class="large-title">What we can help with.</h1>
        <p class="lede">Five core services for individuals and small businesses. Each one starts with a free conversation about your situation.</p>
      </div>
    </section>
    <nav class="wrap" aria-label="Services on this page" style="margin-bottom:2rem">
      <ul class="btn-row" style="list-style:none;padding:0;margin:0">
{chr(10).join(f'        <li><a class="btn btn--secondary btn--sm" href="#{a}">{t}</a></li>' for i,t,a,d in SERVICES)}
      </ul>
    </nav>
    <section class="section" style="padding-top:2rem" aria-label="Service details">
      <div class="wrap">
{chr(10).join(svc_blocks)}
      </div>
    </section>
    <section class="section section--alt cta" aria-labelledby="cta-title">
      <div class="wrap">
        <h2 id="cta-title" class="title-1">Not sure which service fits?</h2>
        <p class="lede">Describe your situation, and you’ll get a recommendation — no commitment.</p>
        <div class="btn-row btn-row--stack"><a class="btn btn--primary btn--lg" href="contact.html">Book a Consultation</a></div>
      </div>
    </section>'''

# ------------------------------ ABOUT ------------------------------
about = f'''    <section class="page-hero" aria-labelledby="page-title">
      <div class="wrap wrap--narrow">
        <p class="eyebrow">About</p>
        <h1 id="page-title" class="large-title">A local firm that explains things.</h1>
        <p class="lede">{FIRM} helps people and small businesses in the Maryland and DC area file accurately, plan ahead, and feel confident about their taxes.<span class="ph-tag">Placeholder</span></p>
      </div>
    </section>

    <section class="section" style="padding-top:1rem" aria-labelledby="values-title">
      <div class="wrap">
        <h2 id="values-title" class="title-2">What guides the work</h2>
        <div class="grid grid--3">
{card("chat","Clarity","Every number gets explained in plain language. You should never sign something you don’t understand.")}
{card("lock","Privacy","Your information is shared only through secure channels and used only for your engagement.")}
{card("calendar","Availability","Questions come up all year. So does support — not just during filing season.")}
        </div>
      </div>
    </section>

    <section class="section section--alt" aria-labelledby="team-title">
      <div class="wrap">
        <div class="section-head">
          <h2 id="team-title" class="title-1">The team</h2>
          <p class="lede">Real bios and photos go here once confirmed.</p>
        </div>
        <div class="grid grid--2">
          <div class="placeholder" role="note">
            {ic("person")}
            <p style="margin-top:1rem"><strong>[Founder name], [Credential]</strong><span class="ph-tag">Placeholder</span></p>
            <p style="margin:0">Add a short, friendly bio: background, areas of focus, and why you started the firm. Include credentials (CPA, EA, PTIN) only once verified.</p>
          </div>
          <div class="placeholder" role="note">
            {ic("people")}
            <p style="margin-top:1rem"><strong>[Team member name], [Role]</strong><span class="ph-tag">Placeholder</span></p>
            <p style="margin:0">Add team members as needed, or remove this card.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="facts-title">
      <div class="wrap">
        <h2 id="facts-title" class="title-2">Firm details</h2>
        <div class="placeholder" role="note">
          <ul class="info-list">
            <li><span class="label">Credentials and licenses</span>[Add verified credentials]<span class="ph-tag">Placeholder</span></li>
            <li><span class="label">Years in practice</span>[Add year founded]<span class="ph-tag">Placeholder</span></li>
            <li><span class="label">Service area</span>Hyattsville, Prince George’s County, and the greater DC area<span class="ph-tag">Placeholder</span></li>
            <li><span class="label">Client testimonials</span>[Add real, permission-granted quotes]<span class="ph-tag">Placeholder</span></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section section--alt cta" aria-labelledby="cta-title">
      <div class="wrap">
        <h2 id="cta-title" class="title-1">Let’s talk.</h2>
        <p class="lede">A short conversation is the best way to see if it’s a good fit.</p>
        <div class="btn-row btn-row--stack"><a class="btn btn--primary btn--lg" href="contact.html">Book a Consultation</a></div>
      </div>
    </section>'''

# ------------------------------ FAQ ------------------------------
FAQ = [
 ("Getting started", [
   ("What should I bring to my first appointment?","Last year’s tax return, a photo ID, and any tax forms you’ve received this year — like W-2s, 1099s, and 1098s. After booking, you’ll get a personalized checklist."),
   ("Do I need to meet in person?","No. Meetings can be in person in the Hyattsville area or online by video. Documents are shared through a secure portal either way.<span class=\"ph-tag\">Confirm</span>"),
   ("How much does tax preparation cost?","It depends on how complex your return is. You’ll get a clear quote before any work begins.<span class=\"ph-tag\">Add pricing</span>"),
 ]),
 ("Taxes and deadlines", [
   ("When is the filing deadline?","For most individuals, federal returns are due April 15. If that date falls on a weekend or holiday, it moves to the next business day. An extension gives you more time to file, but not more time to pay."),
   ("What are estimated taxes?","If you earn income that doesn’t have tax withheld — like self-employment or rental income — the IRS expects payments during the year, usually four times. Paying on time helps avoid penalties."),
   ("Can you help with past-year returns I never filed?","Yes. Prior-year returns can be prepared and filed, and a plan can be made to handle any balance owed."),
 ]),
 ("IRS notices and privacy", [
   ("I got a letter from the IRS. What should I do?","Don’t ignore it, and don’t panic. Most notices ask for a simple correction or more information. Check the response date on the letter, then reach out so it can be reviewed with you."),
   ("How is my personal information protected?","Sensitive documents are exchanged only through a secure, encrypted portal. Please don’t send Social Security numbers or account numbers by email or through the contact form on this site."),
 ]),
]
faq_html = []
for gi,(g,qs) in enumerate(FAQ):
    items = "\n".join(f'''            <details>
              <summary>{q}{svg(I["chev"], ' class="chev"')}</summary>
              <div class="answer"><p>{a}</p></div>
            </details>''' for q,a in qs)
    faq_html.append(f'''        <div class="faq-group">
          <h2 class="title-2" id="faq-g{gi}">{g}</h2>
          <div class="faq" role="group" aria-labelledby="faq-g{gi}">
{items}
          </div>
        </div>''')
faq = f'''    <section class="page-hero" aria-labelledby="page-title">
      <div class="wrap wrap--narrow">
        <p class="eyebrow">FAQ</p>
        <h1 id="page-title" class="large-title">Questions, answered.</h1>
        <p class="lede">Quick answers to common questions. Don’t see yours? Just ask.</p>
      </div>
    </section>
    <section class="section" style="padding-top:1rem" aria-label="Frequently asked questions">
      <div class="wrap wrap--narrow">
{chr(10).join(faq_html)}
      </div>
    </section>
    <section class="section section--alt cta" aria-labelledby="cta-title">
      <div class="wrap">
        <h2 id="cta-title" class="title-1">Still have a question?</h2>
        <p class="lede">Send a message and get a clear answer.</p>
        <div class="btn-row btn-row--stack"><a class="btn btn--primary btn--lg" href="contact.html">Contact Us</a></div>
      </div>
    </section>'''

# ------------------------------ CONTACT ------------------------------
def err(id_):
    return f'<p class="error" id="{id_}-error" aria-live="polite">{svg(I["alert"])}<span></span></p>'
contact = f'''    <section class="page-hero" aria-labelledby="page-title">
      <div class="wrap">
        <p class="eyebrow">Contact</p>
        <h1 id="page-title" class="large-title">Let’s talk taxes.</h1>
        <p class="lede">Send a short message and get a reply within [one business day].<span class="ph-tag">Placeholder</span></p>
      </div>
    </section>
    <section class="section" style="padding-top:1rem" aria-label="Contact form and details">
      <div class="wrap contact-grid">
        <div>
          <form class="form" id="contact-form" novalidate aria-describedby="privacy-note">
            <div class="notice" id="privacy-note">{svg(I["lock"])}<p><strong>Please don’t include Social Security numbers, tax ID numbers, or bank or account details.</strong> Those are collected later through a secure portal.</p></div>
            <div class="form-row form-row--2">
              <div class="field">
                <label for="name">Name</label>
                <input class="input" id="name" name="name" type="text" autocomplete="name" required aria-describedby="name-error">
                {err("name")}
              </div>
              <div class="field">
                <label for="email">Email</label>
                <input class="input" id="email" name="email" type="email" inputmode="email" autocomplete="email" autocapitalize="off" spellcheck="false" required aria-describedby="email-error">
                {err("email")}
              </div>
            </div>
            <div class="form-row form-row--2">
              <div class="field">
                <label for="phone">Phone <span class="opt">(optional)</span></label>
                <input class="input" id="phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" aria-describedby="phone-hint phone-error">
                <p class="hint" id="phone-hint">Only if you’d prefer a call back.</p>
                {err("phone")}
              </div>
              <div class="field">
                <label for="topic">Topic <span class="opt">(optional)</span></label>
                <select class="select" id="topic" name="topic">
                  <option value="">Choose a topic</option>
                  <option>Individual tax preparation</option>
                  <option>Small business tax</option>
                  <option>Bookkeeping</option>
                  <option>Tax planning</option>
                  <option>IRS notice or audit</option>
                  <option>Something else</option>
                </select>
              </div>
            </div>
            <div class="field">
              <label for="message">Message</label>
              <textarea class="textarea" id="message" name="message" rows="5" required aria-describedby="message-hint message-error"></textarea>
              <p class="hint" id="message-hint">A sentence or two about what you need is plenty.</p>
              {err("message")}
            </div>
            <div class="btn-row btn-row--stack">
              <button class="btn btn--primary btn--lg" type="submit">Send Message</button>
            </div>
            <p class="footnote">Your name, email, and message are used only to reply to you.</p>
            <div class="status" id="form-status" role="status" tabindex="-1">{svg(I["check"])}<p></p></div>
          </form>
        </div>
        <aside aria-labelledby="details-title">
          <h2 id="details-title" class="title-3">Office details</h2>
          <ul class="info-list">
            <li><span class="label">Phone</span>(000) 000-0000<span class="ph-tag">Placeholder</span></li>
            <li><span class="label">Email</span>hello@[yourfirm].com<span class="ph-tag">Placeholder</span></li>
            <li><span class="label">Office</span>[Street address]<br>Hyattsville, MD [ZIP]<span class="ph-tag">Placeholder</span></li>
            <li><span class="label">Hours</span>[Mon–Fri, 9 a.m.–5 p.m.]<span class="ph-tag">Placeholder</span></li>
            <li><span class="label">Service area</span>Maryland, Washington DC, and nearby<span class="ph-tag">Placeholder</span></li>
          </ul>
        </aside>
      </div>
    </section>'''

pages = [
 ("index.html", f"{FIRM} — Tax Preparation &amp; Planning in Maryland and DC", "Tax preparation, planning, bookkeeping, and IRS notice help for individuals and small businesses in the Maryland and DC area.", home),
 ("services.html", f"Services — {FIRM}", "Individual tax preparation, small business tax, bookkeeping, tax planning, and IRS notice and audit help.", services),
 ("about.html", f"About — {FIRM}", f"About {FIRM}, a tax firm serving the Maryland and DC area.", about),
 ("faq.html", f"FAQ — {FIRM}", "Answers to common questions about tax preparation, deadlines, IRS notices, and privacy.", faq),
 ("contact.html", f"Contact — {FIRM}", "Send a message or book a consultation.", contact),
]
for f,t,d,b in pages:
    open(os.path.join(OUT,f),"w").write(page(f,t,d,b))
open(os.path.join(OUT,"assets/favicon.svg"),"w").write(
 '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#0071e3"/><g fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" transform="translate(4 4)"><path d="M7 4h10M7 4v16M7 12h7"/></g></svg>')
print("built")
