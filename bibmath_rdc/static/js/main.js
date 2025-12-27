// static/js/main.js
// BibMath RDC - Script principal (2025)
// Auteur: L'équipe BibMath RDC 🇨🇩

document.addEventListener('DOMContentLoaded', function () {
    console.log('%c🚀 BibMath RDC est prêt ! Bienvenue en 2025 !', 'color: #e63946; font-size: 1.2rem; font-weight: bold;');

    // =============================================
    // 1. Navbar : effet au scroll + transparence
    // =============================================
    const navbar = document.querySelector('.navbar');
    const navbarBrand = document.querySelector('.navbar-brand');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 80) {
            navbar.classList.add('scrolled');
            navbarBrand.style.fontSize = '1.4rem';
        } else {
            navbar.classList.remove('scrolled');
            navbarBrand.style.fontSize = '1.6rem';
        }
    });

    // =============================================
    // 2. Bouton "Retour en haut"
    // =============================================
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTopBtn.setAttribute('aria-label', 'Retour en haut');
    backToTopBtn.className = 'btn btn-danger rounded-circle shadow-lg position-fixed border-0';
    backToTopBtn.style.cssText = `
        display: none;
        width: 50px;
        height: 50px;
        bottom: 30px;
        right: 30px;
        z-index: 1000;
        font-size: 1.3rem;
        transition: all 0.3s ease;
    `;
    document.body.appendChild(backToTopBtn);

    window.addEventListener('scroll', function () {
        if (window.scrollY > 400) {
            backToTopBtn.style.display = 'block';
            backToTopBtn.style.opacity = '0.9';
        } else {
            backToTopBtn.style.opacity = '0';
            setTimeout(() => {
                if (window.scrollY <= 400) backToTopBtn.style.display = 'none';
            }, 300);
        }
    });

    backToTopBtn.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // =============================================
    // 3. Préchargement des pages principales au hover
    // =============================================
    const prefetchLinks = document.querySelectorAll('a[href^="/"]');
    prefetchLinks.forEach(link => {
        link.addEventListener('mouseenter', function () {
            const prefetch = document.createElement('link');
            prefetch.rel = 'prefetch';
            prefetch.href = this.href;
            prefetch.as = 'document';
            document.head.appendChild(prefetch);
        });
    });

    // =============================================
    // 4. Animation simple au scroll (sans bibliothèque lourde)
    // =============================================
    const animateOnScroll = document.querySelectorAll('.card, .accordion-item, .hero-section, section');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    animateOnScroll.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
        observer.observe(el);
    });

    // =============================================
    // 5. Toast personnalisé (ex: newsletter, copie, etc.)
    // =============================================
    window.showToast = function (message, type = 'success') {
        const toast = document.createElement('div');
        toast.className = `alert alert-${type === 'success' ? 'success' : 'danger'} alert-dismissible fade show position-fixed shadow-lg`;
        toast.style.cssText = `
            top: 100px;
            right: 20px;
            z-index: 9999;
            min-width: 300px;
            border-radius: 12px;
            backdrop-filter: blur(10px);
        `;
        toast.innerHTML = `
            <strong>${type === 'success' ? '✓' : '✗'} ${type === 'success' ? 'Succès !' : 'Erreur'}</strong><br>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        document.body.appendChild(toast);

        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 4000);
    };

    // Exemple d'utilisation : pour la newsletter
    const newsletterForm = document.querySelector('form[action="/newsletter"]');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            if (email.includes('@')) {
                showToast(`Merci ! Vous recevrez bientôt nos résumés à ${email}`, 'success');
                this.reset();
            } else {
                showToast('Veuillez entrer un email valide.', 'danger');
            }
        });
    }

    // =============================================
    // 6. Mode sombre (toggle activé)
    // =============================================
    const themeToggle = document.createElement('button');
    themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
    themeToggle.className = 'theme-toggle';
    themeToggle.setAttribute('aria-label', 'Basculer le mode sombre');
    document.body.appendChild(themeToggle);

    themeToggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        const icon = themeToggle.querySelector('i');
        icon.classList.toggle('fa-moon');
        icon.classList.toggle('fa-sun');
        localStorage.setItem('theme', newTheme);
        
        showToast(`Mode ${newTheme === 'dark' ? 'sombre' : 'clair'} activé !`, 'success');
    });

    // Chargement du thème sauvegardé
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    if (savedTheme === 'dark') {
        themeToggle.querySelector('i').classList.replace('fa-moon', 'fa-sun');
    }

    // =============================================
    // 7. Amélioration du rendu MathJax après chargement
    // =============================================
    if (typeof MathJax !== 'undefined') {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        console.log('MathJax re-typeset terminé.');
    }

    // =============================================
    // 8. Easter egg congolais 😎
    // =============================================
    let konamiCode = [];
    const konami = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65]; // ↑↑↓↓←→←→BA

    document.addEventListener('keydown', function (e) {
        konamiCode.push(e.keyCode);
        if (konamiCode.length > konami.length) konamiCode.shift();

        if (JSON.stringify(konamiCode) === JSON.stringify(konami)) {
            showToast('🇨🇩 Indépendance ! Tu es un vrai Congolais ! 💪', 'success');
            document.body.style.filter = 'hue-rotate(90deg)';
            setTimeout(() => document.body.style.filter = '', 3000);
            konamiCode = [];
        }
    });

    console.log('%c🔥 BibMath RDC – Fait avec amour à Kinshasa pour toute la RDC 🇨🇩', 'color: #e63946; font-size: 1rem;');
});