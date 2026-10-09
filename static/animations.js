/**
 * LearnGap — Lightweight UI Animation Engine
 * Pure Vanilla JS, zero dependencies, full prefers-reduced-motion accessibility.
 */

(function () {
    'use strict';

    const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /**
     * Easing function: Ease Out Cubic
     */
    function easeOutCubic(t) {
        return 1 - Math.pow(1 - t, 3);
    }

    /**
     * Animate a single numeric counter element
     */
    function animateCounterElement(el) {
        if (el.dataset.animated === 'true') return;

        const rawTarget = (el.getAttribute('data-counter') || el.innerText || '').trim();
        if (!rawTarget) return;

        // If reduced motion is requested, show immediately
        if (prefersReducedMotion) {
            el.innerText = rawTarget;
            el.dataset.animated = 'true';
            return;
        }

        // Case 1: Fraction like "6/6" or "7/10"
        const fractionMatch = rawTarget.match(/^(\d+(?:\.\d+)?)\s*\/\s*(\d+)$/);
        if (fractionMatch) {
            const startVal = 0;
            const endVal = parseFloat(fractionMatch[1]);
            const denom = fractionMatch[2];
            const duration = 650;
            el.innerText = `0/${denom}`;
            const startTime = performance.now();

            function updateFraction(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const eased = easeOutCubic(progress);
                const current = Math.round(startVal + (endVal - startVal) * eased);
                el.innerText = `${current}/${denom}`;

                if (progress < 1) {
                    requestAnimationFrame(updateFraction);
                } else {
                    el.innerText = rawTarget;
                    el.dataset.animated = 'true';
                }
            }
            requestAnimationFrame(updateFraction);
            return;
        }

        // Case 2: Percentage or float like "24.5%" or "85%" or integer "31"
        const numMatch = rawTarget.match(/^(\d+(?:\.\d+)?)(.*)$/);
        if (numMatch) {
            const endVal = parseFloat(numMatch[1]);
            const suffix = numMatch[2] || '';
            const isFloat = numMatch[1].includes('.');
            const decimals = isFloat ? (numMatch[1].split('.')[1] || '').length : 0;
            const duration = 650;
            el.innerText = (isFloat ? (0).toFixed(decimals) : '0') + suffix;
            const startTime = performance.now();

            function updateNumber(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const eased = easeOutCubic(progress);
                const current = (endVal * eased);
                el.innerText = (isFloat ? current.toFixed(decimals) : Math.round(current)) + suffix;

                if (progress < 1) {
                    requestAnimationFrame(updateNumber);
                } else {
                    el.innerText = rawTarget;
                    el.dataset.animated = 'true';
                }
            }
            requestAnimationFrame(updateNumber);
            return;
        }

        el.dataset.animated = 'true';
    }

    /**
     * Initialize Scroll-triggered Reveal Animations
     */
    function initScrollReveal() {
        const revealElements = document.querySelectorAll('.reveal-on-scroll');
        if (!revealElements.length) return;

        if (prefersReducedMotion || !('IntersectionObserver' in window)) {
            revealElements.forEach(el => {
                el.classList.add('is-revealed');
                // Trigger any counters inside
                el.querySelectorAll('[data-counter]').forEach(animateCounterElement);
            });
            return;
        }

        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-revealed');
                    // Animate counters inside revealed container
                    entry.target.querySelectorAll('[data-counter]').forEach(animateCounterElement);
                    if (entry.target.hasAttribute('data-counter')) {
                        animateCounterElement(entry.target);
                    }
                    // Trigger progress bars inside revealed container
                    entry.target.querySelectorAll('.bar-chart-fill, .subject-progress-fill').forEach(bar => {
                        bar.classList.add('is-animated');
                    });
                    obs.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.08,
            rootMargin: '0px 0px -40px 0px'
        });

        revealElements.forEach(el => observer.observe(el));
    }

    /**
     * Initialize all visible counters immediately (e.g. in hero section or score cards)
     */
    function initCounters() {
        const counters = document.querySelectorAll('[data-counter]');
        counters.forEach(el => {
            // If already inside an unrevealed container, wait for scroll reveal
            const parentReveal = el.closest('.reveal-on-scroll:not(.is-revealed)');
            if (!parentReveal) {
                animateCounterElement(el);
            }
        });
    }

    /**
     * Initialize progress bars smooth trigger
     */
    function initProgressBars() {
        const bars = document.querySelectorAll('.subject-progress-fill, .bar-chart-fill');
        bars.forEach(bar => {
            bar.classList.add('is-animated');
        });
    }

    /**
     * Initialize navigation bar interactions (Mobile drawer and touch dropdown)
     */
    function initNavigation() {
        const toggle = document.getElementById('mobileNavToggle');
        const drawer = document.getElementById('mobileDrawer');
        if (toggle && drawer) {
            // Avoid duplicate listeners
            if (!toggle.dataset.navBound) {
                toggle.dataset.navBound = 'true';
                toggle.addEventListener('click', function (e) {
                    e.stopPropagation();
                    drawer.classList.toggle('open');
                    const isOpen = drawer.classList.contains('open');
                    toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
                });

                document.addEventListener('click', function (e) {
                    if (!toggle.contains(e.target) && !drawer.contains(e.target)) {
                        drawer.classList.remove('open');
                        toggle.setAttribute('aria-expanded', 'false');
                    }
                });
            }
        }

        // Dropdown toggle click handling for mobile/touch
        const dropdownToggles = document.querySelectorAll('.nav-dropdown-toggle');
        dropdownToggles.forEach(btn => {
            if (!btn.dataset.dropBound) {
                btn.dataset.dropBound = 'true';
                btn.addEventListener('click', function (e) {
                    e.stopPropagation();
                    const parent = btn.closest('.nav-dropdown');
                    if (parent) {
                        const isOpen = parent.classList.contains('open');
                        document.querySelectorAll('.nav-dropdown.open').forEach(d => {
                            if (d !== parent) d.classList.remove('open');
                        });
                        parent.classList.toggle('open');
                        btn.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
                    }
                });
            }
        });

        document.addEventListener('click', function () {
            document.querySelectorAll('.nav-dropdown.open').forEach(d => {
                d.classList.remove('open');
                const btn = d.querySelector('.nav-dropdown-toggle');
                if (btn) btn.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            initNavigation();
            initScrollReveal();
            initCounters();
            initProgressBars();
        });
    } else {
        initNavigation();
        initScrollReveal();
        initCounters();
        initProgressBars();
    }

    // Export helpers to window for dynamic calls if needed
    window.LearnGapAnimations = {
        animateCounter: animateCounterElement,
        initCounters: initCounters,
        initScrollReveal: initScrollReveal,
        initNavigation: initNavigation
    };
})();
