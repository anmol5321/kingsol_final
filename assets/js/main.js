// Sunergy Custom JavaScript Logic

document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. Sticky Navbar scroll listener ---
    const header = document.querySelector('.main-navbar');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.classList.add('shadow-md');
            } else {
                header.classList.remove('shadow-md');
            }
        });
    }

    // --- 2. Testimonial Slider ---
    let currentTestimonial = 0;
    const testimonials = document.querySelectorAll('.testimonial-item');

    function showTestimonial(index) {
        if (testimonials.length === 0) return;
        testimonials.forEach((item, i) => {
            if (i === index) {
                item.style.display = 'block';
                // Trigger a reflow to restart transition
                item.offsetHeight;
                item.style.opacity = '1';
                item.classList.add('testimonial-active');
                item.classList.remove('testimonial-inactive');
            } else {
                item.style.opacity = '0';
                item.style.display = 'none';
                item.classList.remove('testimonial-active');
                item.classList.add('testimonial-inactive');
            }
        });
    }

    window.nextTestimonial = function() {
        if (testimonials.length === 0) return;
        currentTestimonial = (currentTestimonial + 1) % testimonials.length;
        showTestimonial(currentTestimonial);
    };

    window.prevTestimonial = function() {
        if (testimonials.length === 0) return;
        currentTestimonial = (currentTestimonial - 1 + testimonials.length) % testimonials.length;
        showTestimonial(currentTestimonial);
    };

    // Initialize first testimonial
    showTestimonial(0);

    // --- 3. Projects Category Filter ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    if (filterBtns.length > 0 && projectCards.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active styling from all buttons
                filterBtns.forEach(b => {
                    b.classList.remove('active-filter');
                });
                
                // Add active styling to clicked button
                btn.classList.add('active-filter');

                const filterValue = btn.textContent.trim().toLowerCase();

                projectCards.forEach(card => {
                    // Find card category
                    const categoryEl = card.querySelector('.font-label-caps.text-primary, .project-badge, p.font-label-caps');
                    const categoryText = categoryEl ? categoryEl.textContent.trim().toLowerCase() : '';

                    if (filterValue === 'all projects' || categoryText === filterValue) {
                        // Fade in transition
                        card.style.display = 'block';
                        setTimeout(() => {
                            card.style.opacity = '1';
                            card.style.transform = 'scale(1)';
                        }, 50);
                    } else {
                        // Fade out transition
                        card.style.opacity = '0';
                        card.style.transform = 'scale(0.95)';
                        setTimeout(() => {
                            card.style.display = 'none';
                        }, 300);
                    }
                });
            });
        });
    }

    // --- 4. Forms Submission Handlers ---
    const contactForms = document.querySelectorAll('form');
    contactForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            // Find the submit button
            const submitBtn = form.querySelector('button[type="submit"]');
            if (!submitBtn) return;

            const originalContent = submitBtn.innerHTML;
            
            // Show sending state
            submitBtn.innerHTML = `
                <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                SENDING...
            `;
            submitBtn.disabled = true;

            // Simulate server network delay
            setTimeout(() => {
                // Show success state
                submitBtn.innerHTML = `
                    <span class="material-symbols-outlined me-2">check_circle</span>
                    MESSAGE SENT!
                `;
                submitBtn.classList.remove('btn-custom-primary', 'btn-custom-dark', 'custom-gradient');
                submitBtn.style.backgroundColor = '#28a745';
                submitBtn.style.color = '#ffffff';

                // Reset form fields
                form.reset();

                // Re-enable button with original text after a few seconds
                setTimeout(() => {
                    submitBtn.innerHTML = originalContent;
                    submitBtn.disabled = false;
                    submitBtn.style.backgroundColor = '';
                    submitBtn.style.color = '';
                    if (submitBtn.classList.contains('btn-custom-white')) {
                        // Keep white classes
                    } else {
                        submitBtn.classList.add('btn-custom-primary');
                    }
                }, 3000);

            }, 1500);
        });
    });
});
