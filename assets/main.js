/* Minimal progressive enhancement: mobile menu + contact form validation. */
(function () {
  document.documentElement.classList.add('js');

  // ----- Mobile menu (a lightweight modal: obvious dismiss, Esc, focus return) -----
  var nav = document.querySelector('.nav');
  var btn = document.querySelector('.menu-btn');
  var menu = document.getElementById('site-menu');
  if (nav && btn && menu) {
    var mq = window.matchMedia('(max-width: 900px)');
    function setOpen(open, returnFocus) {
      nav.classList.toggle('nav--open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      document.body.classList.toggle('menu-open', open);
      if (mq.matches) { menu.toggleAttribute('inert', !open); }
      if (open) {
        var first = menu.querySelector('a');
        if (first) first.focus();
      } else if (returnFocus) {
        btn.focus();
      }
    }
    function sync() {
      if (mq.matches) { menu.toggleAttribute('inert', !nav.classList.contains('nav--open')); }
      else { menu.removeAttribute('inert'); setOpen(false); }
    }
    btn.addEventListener('click', function () {
      setOpen(btn.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('nav--open')) setOpen(false, true);
    });
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });
    (mq.addEventListener ? mq.addEventListener('change', sync) : mq.addListener(sync));
    sync();
  }

  // ----- Contact form: inline, blame-free validation; front-end only -----
  var form = document.getElementById('contact-form');
  if (!form) return;
  var status = document.getElementById('form-status');
  var sensitive = /\b\d{3}[- ]?\d{2}[- ]?\d{4}\b/; // looks like an SSN/ITIN

  var rules = {
    name: function (v) { return v.trim() ? '' : 'Enter your name.'; },
    email: function (v) {
      if (!v.trim()) return 'Enter an email address.';
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) ? '' : 'Enter an email address, like name@example.com.';
    },
    phone: function (v) {
      if (!v.trim()) return '';
      return v.replace(/\D/g, '').length >= 10 ? '' : 'Enter a 10-digit phone number, or leave this blank.';
    },
    message: function (v) {
      if (!v.trim()) return 'Add a short message about what you need.';
      if (sensitive.test(v)) return 'Remove the Social Security or tax ID number. Share it only in a secure meeting.';
      return '';
    }
  };

  function check(field) {
    var rule = rules[field.name];
    if (!rule) return true;
    var msg = rule(field.value);
    var err = document.getElementById(field.id + '-error');
    field.setAttribute('aria-invalid', msg ? 'true' : 'false');
    if (err) {
      err.querySelector('span').textContent = msg;
      err.classList.toggle('is-visible', !!msg);
    }
    return !msg;
  }

  Array.prototype.forEach.call(form.elements, function (el) {
    if (!rules[el.name]) return;
    el.addEventListener('blur', function () { if (el.value) check(el); });
    el.addEventListener('input', function () { if (el.getAttribute('aria-invalid') === 'true') check(el); });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var firstBad = null;
    Array.prototype.forEach.call(form.elements, function (el) {
      if (rules[el.name] && !check(el) && !firstBad) firstBad = el;
    });
    if (firstBad) { firstBad.focus(); status.classList.remove('is-visible'); return; }
    var submit = form.querySelector('[type="submit"]');
    submit.disabled = true; submit.textContent = 'Sending…';
    // Demo only: no backend is connected. Nothing leaves the browser.
    setTimeout(function () {
      form.reset();
      Array.prototype.forEach.call(form.elements, function (el) { el.removeAttribute('aria-invalid'); });
      submit.disabled = false; submit.textContent = 'Send Message';
      status.classList.add('is-visible');
      status.querySelector('p').innerHTML = '<strong>Message ready.</strong> This is a demo form, so nothing was sent. Connect a form service before launch.';
      status.focus();
    }, 600);
  });
})();
