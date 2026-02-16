


// menu.js - Menu responsivo e funcionalidades

document.addEventListener('DOMContentLoaded', function() {
    // ===== MENU MOBILE =====
    const menuIcon = document.querySelector('.menu-icone');
    const menu = document.querySelector('.menu');
    
    if (menuIcon && menu) {
        // Alterna menu quando clica no ícone
        menuIcon.addEventListener('click', function(e) {
            e.stopPropagation();
            menu.classList.toggle('active');
            menuIcon.textContent = menu.classList.contains('active') ? '✕' : '☰';
        });
        
        // Fecha menu ao clicar fora dele
        document.addEventListener('click', function(e) {
            if (menu.classList.contains('active') && 
                !menu.contains(e.target) && 
                !menuIcon.contains(e.target)) {
                menu.classList.remove('active');
                menuIcon.textContent = '☰';
            }
        });
        
        // Fecha menu ao clicar em um link do menu
        const menuLinks = document.querySelectorAll('.link_menu');
        menuLinks.forEach(link => {
            link.addEventListener('click', function() {
                if (window.innerWidth <= 767) {
                    menu.classList.remove('active');
                    menuIcon.textContent = '☰';
                }
            });
        });
        
        // Fecha menu automaticamente ao redimensionar para desktop
        window.addEventListener('resize', function() {
            if (window.innerWidth > 767) {
                menu.classList.remove('active');
                menuIcon.textContent = '☰';
            }
        });
    }
    
    // ===== SCROLL SUAVE PARA ÂNCORAS =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Ignora links vazios ou que não são âncoras
            if (href === '#' || href === '') return;
            
            const targetElement = document.querySelector(href);
            
            if (targetElement) {
                e.preventDefault();
                
                // Calcula posição considerando o header fixo
                const headerHeight = document.querySelector('header')?.offsetHeight || 80;
                const targetPosition = targetElement.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // ===== ANIMAÇÃO DOS CARDS DE HABILIDADE =====
    function animateCardsOnScroll() {
        const cards = document.querySelectorAll('.card_habilidade');
        const windowHeight = window.innerHeight;
        
        cards.forEach(card => {
            const cardPosition = card.getBoundingClientRect().top;
            
            if (cardPosition < windowHeight - 100) {
                card.classList.add('show');
            }
        });
    }
    
    // Dispara animação ao carregar e ao rolar
    window.addEventListener('load', animateCardsOnScroll);
    window.addEventListener('scroll', animateCardsOnScroll);
    
    // ===== FORMULÁRIO DE CONTATO - Feedback visual =====
    const contactForm = document.querySelector('form[action*="formspree"]');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            // Feedback visual durante envio
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Enviando...';
            
            // Restaura botão após 5 segundos (caso haja erro)
            setTimeout(() => {
                submitBtn.disabled = false;
                submitBtn.textContent = originalText;
            }, 5000);
        });
    }
    
        // ===== ATUALIZAR ANO DO COPYRIGHT =====
        function updateCopyrightYear() {
            const copyrightElements = document.querySelectorAll('.port');
            const currentYear = new Date().getFullYear();
            
            copyrightElements.forEach(element => {
                if (element.textContent.includes('2026')) {
                    element.textContent = element.textContent.replace('2026', currentYear);
                }
            });
        }
        
    updateCopyrightYear();
    
    // ===== DETECTAR ORIENTAÇÃO MOBILE =====
    function handleOrientationChange() {
        if (window.innerHeight > window.innerWidth) {
            // Portrait
            document.body.classList.remove('landscape');
            document.body.classList.add('portrait');
        } else {
            // Landscape
            document.body.classList.remove('portrait');
            document.body.classList.add('landscape');
        }
    }
    
    window.addEventListener('resize', handleOrientationChange);
    handleOrientationChange(); 
});