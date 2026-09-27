/* Carrousels : fondu automatique, flèches, points, glisser au doigt.
   Pas d'animation automatique si l'utilisateur a demandé moins de mouvement. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.carousel').forEach(function (car) {
    var slides = car.querySelectorAll('.car-slide');
    if (slides.length < 2) return;
    var dots = car.querySelectorAll('.car-dots button');
    var delay = parseInt(car.dataset.interval, 10) || 4500;
    var i = 0, timer = null, paused = false, visible = true;

    function show(n) {
      slides[i].classList.remove('is-active');
      slides[i].setAttribute('aria-hidden', 'true');
      if (dots[i]) dots[i].removeAttribute('aria-selected');
      i = (n + slides.length) % slides.length;
      slides[i].classList.add('is-active');
      slides[i].removeAttribute('aria-hidden');
      if (dots[i]) dots[i].setAttribute('aria-selected', 'true');
      var next = slides[(i + 1) % slides.length].querySelectorAll('img[loading="lazy"]');
      next.forEach(function (im) { im.loading = 'eager'; });
    }
    function stop() { clearInterval(timer); timer = null; }
    function start() {
      stop();
      if (reduce || paused || !visible) return;
      timer = setInterval(function () { show(i + 1); }, delay);
    }

    car.querySelector('.car-prev').addEventListener('click', function () { show(i - 1); start(); });
    car.querySelector('.car-next').addEventListener('click', function () { show(i + 1); start(); });
    dots.forEach(function (d, n) { d.addEventListener('click', function () { show(n); start(); }); });

    car.addEventListener('mouseenter', function () { paused = true; stop(); });
    car.addEventListener('mouseleave', function () { paused = false; start(); });
    car.addEventListener('focusin', function () { paused = true; stop(); });
    car.addEventListener('focusout', function () { paused = false; start(); });
    car.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { show(i - 1); }
      if (e.key === 'ArrowRight') { show(i + 1); }
    });

    var x0 = null;
    car.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    car.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 40) { show(dx < 0 ? i + 1 : i - 1); start(); }
      x0 = null;
    });

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting; visible ? start() : stop();
      }, { threshold: 0.2 }).observe(car);
    }
    document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
    start();
  });
})();
