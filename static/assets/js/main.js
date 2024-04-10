/**
* Template Name: Day
* Template URL: https://bootstrapmade.com/day-multipurpose-html-template-for-free/
* Updated: Mar 19 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .has-dropdown i').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      if (document.querySelector('.mobile-nav-active')) {
        e.preventDefault();
        this.parentNode.classList.toggle('active');
        this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
        e.stopImmediatePropagation();
      }
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll('.swiper').forEach(function(swiper) {
      let config = JSON.parse(swiper.querySelector('.swiper-config').innerHTML.trim());
      new Swiper(swiper, config);
    });
  }
  window.addEventListener('load', initSwiper);

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

    let initIsotope;
    imagesLoaded(isotopeItem.querySelector('.isotope-container'), function() {
      initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });
    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
      filters.addEventListener('click', function() {
        isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
        this.classList.add('filter-active');
        initIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        if (typeof aosInit === 'function') {
          aosInit();
        }
      }, false);
    });

  });

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function(e) {
    if (window.location.hash) {
      const section = document.querySelector(window.location.hash);
      if (section) {
        section.scrollIntoView({
          behavior: "smooth",
          block: "start"
        });
      }
    }
  });

  /**
   * Auto-Active Navmenu Links
   */
  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuActive() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navmenuActive);
  document.addEventListener('scroll', navmenuActive);

})();

document.addEventListener('DOMContentLoaded', function() {
  const armstrongForm = document.getElementById('armstrongForm');
  const armstrongForm2 = document.getElementById('armstrongForm2');
  const resultDiv = document.querySelector('.result');
  const resultDiv2 = document.querySelector('.result2');
  const resultDiv3 = document.querySelector('.result3');

  armstrongForm.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent the default form submission behavior

      const formData = new FormData(armstrongForm);
      const number = formData.get('number');
      console.log(number)

      fetch('/check-armstrong/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,  // Replace with your template variable if needed
          },
          body: JSON.stringify({ number: number }),
      })
      .then(response => response.json())
      .then(data => {
          if (data.result) {
              resultDiv.innerText = `${number} is an Armstrong number`;
              resultDiv.classList.add('green');
              resultDiv.classList.remove('red');
          } else {
              resultDiv.innerText = `${number} is not an Armstrong number`;
              resultDiv.classList.add('red');
              resultDiv.classList.remove('green');
          }
      })
      .catch(error => console.error('Error:', error));
  });

  armstrongForm2.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const formData2 = new FormData(armstrongForm2);
    const frome = formData2.get('frome');
    const to = formData2.get('to');
    
    console.log(frome)
    console.log(2)

    fetch('check_armstrongRange/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,  // Replace with your template variable if needed
        },
        body: JSON.stringify({ frome : frome , to: to}),
    })
    .then(response => response.json())
    .then(data => {
      if (Array.isArray(data.result) && data.result.length > 0) {
        resultDiv2.innerHTML = data.result.join(', ');
        resultDiv2.style.height = 'auto';
        resultDiv2.classList.add('green');
        resultDiv3.innerHTML = data.result.length + " Armstrong Numbers Found";
        resultDiv3.classList.add('green');
        resultDiv2.classList.remove('red');
    } else {
        resultDiv3.classList.remove('green', 'red');
        resultDiv2.innerHTML = `No Armstrong numbers found in the range.`;
        resultDiv2.style.height = 'auto';
        resultDiv2.classList.add('red');
        resultDiv2.classList.remove('green');
    }
    })
    .catch(error => console.error('Error:', error));
});




});
clearBtn = document.querySelector('.clear');
clearBtn2 = document.querySelector('.clear2');
clearBtn.addEventListener('click', function() {
  const resultDiv = document.querySelector('.result');
  
    document.querySelector('#number').value = '';
    resultDiv.innerText = '';
    resultDiv.classList.remove('green', 'red');
});

clearBtn2.addEventListener('click', function() {
  const resultDiv2 = document.querySelector('.result2');
  const resultDiv3 = document.querySelector('.result3');
  
    document.querySelector('#to').value = '';
    document.querySelector('#frome').value = '';
    resultDiv2.innerText = '';
    resultDiv2.classList.remove('green', 'red');
    resultDiv3.innerText = '';
    resultDiv3.classList.remove('green', 'red');
});

document.addEventListener('DOMContentLoaded', function() {
  const feedbackForm = document.getElementById('feedbackForm');
  const loadingMessage = document.querySelector('.loading');
  const errorMessage = document.querySelector('.error-message');
  const successMessage = document.querySelector('.sent-message');

  feedbackForm.addEventListener('submit', function(event) {
      event.preventDefault();
      loadingMessage.style.display = 'block';
      errorMessage.style.display = 'none';
      successMessage.style.display = 'none';

      const formData = new FormData(feedbackForm);
      fetch('sendFeedback', {
          method: 'POST',
          body: formData,
      })
      .then(response => {
          loadingMessage.style.display = 'none';
          if (response.ok) {
              successMessage.style.display = 'block';
          } else {
              errorMessage.style.display = 'block';
          }
      })
      .catch(error => {
          loadingMessage.style.display = 'none';
          errorMessage.style.display = 'block';
      });
  });
});
