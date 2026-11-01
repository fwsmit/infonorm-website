// infonorm — small progressive-enhancement script
(function () {
  document.documentElement.classList.add('js');

  var toggle = document.querySelector('.nav-toggle');
  var links = document.getElementById('nav-links');

  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
    });

    // Close the menu after choosing a link (mobile).
    links.addEventListener('click', function (event) {
      if (event.target.closest('a')) {
        links.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    // Close on Escape and return focus to the button.
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && links.classList.contains('is-open')) {
        links.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  var year = document.getElementById('year');
  if (year) {
    year.textContent = new Date().getFullYear();
  }
})();
