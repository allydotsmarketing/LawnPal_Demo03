// LawnPal Demo 03 — navigation + demo quote form
(function () {
  // Mobile menu
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('is-open', !open);
    });
  }

  // Services dropdown
  var subBtn = document.querySelector('[data-submenu]');
  var sub = document.getElementById('services-menu');
  if (subBtn && sub) {
    var setSub = function (open) {
      subBtn.setAttribute('aria-expanded', String(open));
      sub.classList.toggle('is-open', open);
    };
    subBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      setSub(subBtn.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('click', function (e) {
      if (!sub.contains(e.target)) setSub(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { setSub(false); subBtn.focus(); }
    });
  }

  // Service-area map: choosing a city moves the Google map there.
  var map = document.getElementById('area-map');
  if (map) {
    var areaBtns = document.querySelectorAll('.area[data-map]');
    document.querySelectorAll('[data-map]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        map.src = btn.getAttribute('data-map');
        areaBtns.forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
      });
    });
  }

  // Gallery filters + photo viewer
  var gallery = document.getElementById('gallery');
  if (gallery) {
    var filters = document.querySelectorAll('.filter');
    var empty = document.querySelector('.gallery-empty');
    filters.forEach(function (f) {
      f.addEventListener('click', function () {
        var cat = f.getAttribute('data-filter');
        var shown = 0;
        filters.forEach(function (o) { o.setAttribute('aria-pressed', String(o === f)); });
        gallery.querySelectorAll('.g-item').forEach(function (item) {
          var show = cat === 'all' || item.getAttribute('data-cat') === cat;
          item.hidden = !show;
          if (show) shown++;
        });
        if (empty) empty.hidden = shown > 0;
      });
    });

    var box = document.getElementById('lightbox');
    if (box && typeof box.showModal === 'function') {
      var boxImg = box.querySelector('img');
      var boxCap = box.querySelector('.lightbox-caption');
      gallery.querySelectorAll('.g-open').forEach(function (b) {
        b.addEventListener('click', function () {
          boxImg.src = b.getAttribute('data-full');
          boxImg.alt = b.getAttribute('data-caption');
          boxCap.textContent = b.getAttribute('data-caption');
          box.showModal();
        });
      });
      box.addEventListener('click', function (e) { if (e.target === box) box.close(); });
    }
  }

  // Demo quote form: validates on screen, sends nothing.
  var form = document.getElementById('quote-form');
  if (!form) return;
  var success = document.getElementById('form-success');

  var rules = {
    name: function (v) { return v.trim() ? '' : 'Enter your name.'; },
    phone: function (v) {
      var digits = v.replace(/\D/g, '');
      if (!digits) return 'Enter your phone number so we can call you back.';
      return digits.length >= 10 ? '' : 'Enter a 10-digit phone number, like (954) 555-0123.';
    },
    email: function (v) {
      if (!v.trim()) return '';
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) ? '' : 'Check the email address, or leave it blank.';
    },
    address: function (v) { return v.trim() ? '' : 'Enter your street address or ZIP code.'; },
    service: function (v) { return v ? '' : 'Choose the service you need.'; }
  };

  function check(name) {
    var input = form.elements[name];
    var msg = rules[name](input.value);
    var err = document.getElementById(name + '-error');
    input.setAttribute('aria-invalid', msg ? 'true' : 'false');
    if (err) err.textContent = msg;
    return !msg;
  }

  Object.keys(rules).forEach(function (name) {
    form.elements[name].addEventListener('blur', function () {
      if (this.value) check(name);
    });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var firstBad = null;
    Object.keys(rules).forEach(function (name) {
      if (!check(name) && !firstBad) firstBad = form.elements[name];
    });
    if (firstBad) { firstBad.focus(); return; }

    var first = form.elements.name.value.trim().split(/\s+/)[0];
    document.getElementById('success-name').textContent = first;
    form.hidden = true;
    success.hidden = false;
    success.focus();
  });
})();
