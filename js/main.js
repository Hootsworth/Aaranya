/**
 * AARANYA UNIVERSITY — MASTER INTERACTIVE ENGINE (V2.0)
 * Script: main.js
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initStickyHeader();
  initStatCounters();
  initAccordions();
  initTabSwitchers();
  initInquiryForms();
  initLightbox();
});

/* Navigation & Mobile Drawer */
function initNavigation() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const drawer = document.querySelector('.mobile-nav-drawer');
  const backdrop = document.querySelector('.drawer-backdrop');
  const closeBtn = document.querySelector('.drawer-close');

  if (!toggleBtn || !drawer || !backdrop) return;

  function openDrawer() {
    drawer.classList.add('open');
    backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    backdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  toggleBtn.addEventListener('click', openDrawer);
  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  backdrop.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });
}

/* Sticky Header Scroll Effect */
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* Stat Number Counter Animation */
function initStatCounters() {
  const statNumbers = document.querySelectorAll('.stat-number');
  if (!statNumbers.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const rawTarget = el.getAttribute('data-target') || el.innerText;
        animateNumber(el, rawTarget);
        obs.unobserve(el);
      }
    });
  }, { threshold: 0.4 });

  statNumbers.forEach(num => observer.observe(num));
}

function animateNumber(element, rawTarget) {
  const matches = rawTarget.match(/(\D*)(\d+[\.\d]*)(\D*)/);
  if (!matches) return;

  const prefix = matches[1] || '';
  const targetVal = parseFloat(matches[2]);
  const suffix = matches[3] || '';
  const isDecimal = matches[2].includes('.');

  let start = 0;
  const duration = 1600;
  const frameRate = 1000 / 60;
  const totalFrames = Math.round(duration / frameRate);
  let frame = 0;

  const timer = setInterval(() => {
    frame++;
    const progress = easeOutExpo(frame / totalFrames);
    const current = (progress * targetVal);

    element.innerText = `${prefix}${isDecimal ? current.toFixed(1) : Math.round(current)}${suffix}`;

    if (frame === totalFrames) {
      clearInterval(timer);
      element.innerText = rawTarget;
    }
  }, frameRate);
}

function easeOutExpo(x) {
  return x === 1 ? 1 : 1 - Math.pow(2, -10 * x);
}

/* Accordions */
function initAccordions() {
  const accordionItems = document.querySelectorAll('.accordion-item');
  if (!accordionItems.length) return;

  accordionItems.forEach(item => {
    const header = item.querySelector('.accordion-header');
    if (!header) return;

    header.addEventListener('click', () => {
      const isOpen = item.classList.contains('active');

      const parent = item.closest('.accordion');
      if (parent) {
        parent.querySelectorAll('.accordion-item').forEach(sibling => {
          if (sibling !== item) sibling.classList.remove('active');
        });
      }

      item.classList.toggle('active', !isOpen);
    });
  });
}

/* Tab Switcher */
function initTabSwitchers() {
  const tabContainers = document.querySelectorAll('[data-tabs]');
  tabContainers.forEach(container => {
    const tabButtons = container.querySelectorAll('.tab-btn');
    const tabPanes = container.querySelectorAll('.tab-pane');

    tabButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-tab-target');

        tabButtons.forEach(b => b.classList.remove('active'));
        tabPanes.forEach(p => p.classList.remove('active'));

        btn.classList.add('active');
        const targetPane = container.querySelector(targetId);
        if (targetPane) targetPane.classList.add('active');
      });
    });
  });
}

/* Form Handling */
function initInquiryForms() {
  const forms = document.querySelectorAll('.university-form');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.innerHTML : 'Submit';

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Submitting...';
      }

      setTimeout(() => {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = 'Submission Received';
        }

        let alertBox = form.querySelector('.form-alert');
        if (!alertBox) {
          alertBox = document.createElement('div');
          alertBox.className = 'form-alert';
          alertBox.style.marginTop = '1.25rem';
          alertBox.style.padding = '1rem 1.25rem';
          alertBox.style.borderRadius = '4px';
          alertBox.style.backgroundColor = '#e3ebe4';
          alertBox.style.color = '#163024';
          alertBox.style.fontSize = '0.9rem';
          alertBox.style.fontWeight = '500';
          form.appendChild(alertBox);
        }
        alertBox.innerHTML = `<strong>Thank you.</strong> Your inquiry has been registered with Aaranya University Academic Directorate. An admissions counselor will connect with you within 24 hours.`;
        form.reset();

        setTimeout(() => {
          if (submitBtn) submitBtn.innerHTML = originalText;
        }, 5000);
      }, 900);
    });
  });
}

/* Image Lightbox Viewer */
function initLightbox() {
  let lightbox = document.querySelector('.image-lightbox');
  if (!lightbox) {
    lightbox = document.createElement('div');
    lightbox.className = 'image-lightbox';
    lightbox.innerHTML = `
      <div class="lightbox-content">
        <button class="lightbox-close" aria-label="Close Lightbox">&times;</button>
        <img src="" alt="Aaranya University Document">
        <div class="lightbox-caption"></div>
      </div>
    `;
    document.body.appendChild(lightbox);
  }

  const lightboxImg = lightbox.querySelector('img');
  const lightboxCaption = lightbox.querySelector('.lightbox-caption');
  const closeBtn = lightbox.querySelector('.lightbox-close');

  function openLightbox(src, caption) {
    lightboxImg.src = src;
    lightboxCaption.innerText = caption || 'Aaranya University Official Publication';
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  closeBtn.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox.classList.contains('active')) {
      closeLightbox();
    }
  });

  // Attach to trigger buttons or clickable images
  document.querySelectorAll('[data-lightbox-src]').forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      const src = trigger.getAttribute('data-lightbox-src');
      const caption = trigger.getAttribute('data-lightbox-caption') || trigger.getAttribute('title');
      openLightbox(src, caption);
    });
  });
}
