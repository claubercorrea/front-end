// slider.js - Slider Dinâmico para Projetos

// Dados dos projetos (pode vir de uma API no futuro)
const projetosData = [
    {
        id:1,
        image: "/v1016-b-09.jpg",
        title: "Projeto Web Moderno",
        description: "Desenvolvimento de site responsivo com tecnologias modernas",
        link: "#"
    },
    {
        id: 2,
        image: "/v1016-b-09.jpg",
        image: ""   ,
        title: "Aplicativo Mobile",
        description: "App nativo desenvolvido com React Native",
        link: "#"
    },
    {
        id: 3,
        image: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop",
        title: "E-commerce Completo",
        description: "Plataforma de vendas online com sistema de pagamento",
        link: "#"
    },
    {
        id: 4,
        image: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop",
        title: "Dashboard Analytics",
        description: "Painel administrativo com gráficos em tempo real",
        link: "#"
    },
    {
        id: 5,
        image: "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800&auto=format&fit=crop",
        title: "API RESTful",
        description: "Desenvolvimento de API robusta com documentação",
        link: "#"
    }
];

class DynamicSlider {
    constructor() {
        this.sliderElement = document.querySelector('.carousel-inner');
        this.controlsElement = document.querySelector('.carousel-controls');
        this.currentSlide = 0;
        this.totalSlides = 0;
        this.autoSlideInterval = null;
        this.indicatorsContainer = null;
        
        this.init();
    }
    
    init() {
        this.createSlides();
        this.createIndicators();
        this.setupEventListeners();
        this.startAutoSlide();
        this.updateSlidePosition();
    }
    
    createSlides() {
        this.sliderElement.innerHTML = '';
        
        projetosData.forEach((projeto, index) => {
            const slide = document.createElement('div');
            slide.className = 'carousel-slide';
            slide.dataset.index = index;
            
            // Criar imagem
            const img = document.createElement('img');
            img.src = projeto.image;
            img.alt = projeto.title;
            img.loading = index < 2 ? 'eager' : 'lazy';
            
            // Criar conteúdo overlay
            const content = document.createElement('div');
            content.className = 'slide-content';
            content.innerHTML = `
                <h3 class="slide-title">${projeto.title}</h3>
                <p class="slide-description">${projeto.description}</p>
                <a href="${projeto.link}" class="slide-link" target="_blank">Ver Projeto</a>
            `;
            
            slide.appendChild(img);
            slide.appendChild(content);
            this.sliderElement.appendChild(slide);
        });
        
        this.totalSlides = projetosData.length;
    }
    
    createIndicators() {
        // Criar container de indicadores se não existir
        if (!this.indicatorsContainer) {
            this.indicatorsContainer = document.createElement('div');
            this.indicatorsContainer.className = 'carousel-indicators';
            this.sliderElement.parentNode.appendChild(this.indicatorsContainer);
        }
        
        this.indicatorsContainer.innerHTML = '';
        
        for (let i = 0; i < this.totalSlides; i++) {
            const dot = document.createElement('div');
            dot.className = `carousel-dot ${i === 0 ? 'active' : ''}`;
            dot.dataset.index = i;
            dot.addEventListener('click', () => this.goToSlide(i));
            this.indicatorsContainer.appendChild(dot);
        }
    }
    
    setupEventListeners() {
        // Botões de navegação
        const prevBtn = document.querySelector('[data-carousel-prev]');
        const nextBtn = document.querySelector('[data-carousel-next]');
        
        if (prevBtn) {
            prevBtn.addEventListener('click', () => this.prevSlide());
        }
        
        if (nextBtn) {
            nextBtn.addEventListener('click', () => this.nextSlide());
        }
        
        // Navegação por teclado
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') this.prevSlide();
            if (e.key === 'ArrowRight') this.nextSlide();
            if (e.key === 'Escape') this.stopAutoSlide();
        });
        
        // Swipe para mobile
        this.setupTouchEvents();
        
        // Pausar auto-slide ao passar o mouse
        this.sliderElement.addEventListener('mouseenter', () => this.stopAutoSlide());
        this.sliderElement.addEventListener('mouseleave', () => this.startAutoSlide());
    }
    
    setupTouchEvents() {
        let startX = 0;
        let endX = 0;
        const threshold = 50;
        
        this.sliderElement.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
            this.stopAutoSlide();
        });
        
        this.sliderElement.addEventListener('touchmove', (e) => {
            endX = e.touches[0].clientX;
        });
        
        this.sliderElement.addEventListener('touchend', () => {
            const diff = startX - endX;
            
            if (Math.abs(diff) > threshold) {
                if (diff > 0) {
                    this.nextSlide();
                } else {
                    this.prevSlide();
                }
            }
            
            this.startAutoSlide();
        });
    }
    
    goToSlide(index) {
        this.currentSlide = index;
        this.updateSlidePosition();
        this.updateIndicators();
        this.resetAutoSlide();
    }
    
    nextSlide() {
        this.currentSlide = (this.currentSlide + 1) % this.totalSlides;
        this.updateSlidePosition();
        this.updateIndicators();
        this.resetAutoSlide();
    }
    
    prevSlide() {
        this.currentSlide = (this.currentSlide - 1 + this.totalSlides) % this.totalSlides;
        this.updateSlidePosition();
        this.updateIndicators();
        this.resetAutoSlide();
    }
    
    updateSlidePosition() {
        const translateX = -this.currentSlide * 100;
        this.sliderElement.style.transform = `translateX(${translateX}%)`;
    }
    
    updateIndicators() {
        const dots = document.querySelectorAll('.carousel-dot');
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === this.currentSlide);
        });
    }
    
    startAutoSlide() {
        this.stopAutoSlide();
        this.autoSlideInterval = setInterval(() => {
            this.nextSlide();
        }, 5000); // Muda a cada 5 segundos
    }
    
    stopAutoSlide() {
        if (this.autoSlideInterval) {
            clearInterval(this.autoSlideInterval);
            this.autoSlideInterval = null;
        }
    }
    
    resetAutoSlide() {
        this.stopAutoSlide();
        this.startAutoSlide();
    }
    
    // Método para adicionar slides dinamicamente
    addSlide(slideData) {
        projetosData.push(slideData);
        this.createSlides();
        this.createIndicators();
        this.updateSlidePosition();
    }
    
    // Método para remover slide
    removeSlide(index) {
        if (index >= 0 && index < projetosData.length) {
            projetosData.splice(index, 1);
            this.createSlides();
            this.createIndicators();
            this.currentSlide = Math.min(this.currentSlide, projetosData.length - 1);
            this.updateSlidePosition();
        }
    }
}

// Inicializar o slider quando a página carregar
document.addEventListener('DOMContentLoaded', () => {
    // Inicializar slider de projetos
    const slider = new DynamicSlider();
    
    // Expor slider globalmente para testes
    window.projetosSlider = slider;
    
    // Ajustar animação do carrossel de linguagens
    adjustCarouselAnimation();
    
    // Menu mobile
    setupMobileMenu();
});

// Função para ajustar animação do carrossel de linguagens
function adjustCarouselAnimation() {
    const items = document.querySelectorAll('.item');
    const screenWidth = window.innerWidth;
    
    items.forEach((item) => {
        if (screenWidth < 768) {
            item.style.animationDuration = '15s';
        } else if (screenWidth < 1024) {
            item.style.animationDuration = '12s';
        } else {
            item.style.animationDuration = '10s';
        }
    });
}

// Configurar menu mobile
function setupMobileMenu() {
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navmenu');
    
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });
        
        // Fechar menu ao clicar em um link
        document.querySelectorAll('.link_lista').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                menuToggle.classList.remove('active');
            });
        });
        
        // Fechar menu ao clicar fora
        document.addEventListener('click', (e) => {
            if (!navMenu.contains(e.target) && !menuToggle.contains(e.target)) {
                navMenu.classList.remove('active');
                menuToggle.classList.remove('active');
            }
        });
    }
}

// Redimensionamento da janela
window.addEventListener('resize', () => {
    adjustCarouselAnimation();
    
    // Se a tela for grande, garantir que o menu esteja visível
    if (window.innerWidth > 768) {
        const navMenu = document.getElementById('navmenu');
        const menuToggle = document.getElementById('menuToggle');
        
        if (navMenu) navMenu.classList.remove('active');
        if (menuToggle) menuToggle.classList.remove('active');
    }
});

// Adicionar CSS para conteúdo do slide
const slideStyles = document.createElement('style');
slideStyles.textContent = `
    .slide-content {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
        color: white;
        padding: 30px;
        border-radius: 0 0 10px 10px;
        transform: translateY(100%);
        transition: transform 0.3s ease;
    }
    
    .carousel-slide:hover .slide-content {
        transform: translateY(0);
    }
    
    .slide-title {
        font-size: clamp(1.5rem, 3vw, 2.2rem);
        margin-bottom: 10px;
        color: #ff6b6b;
    }
    
    .slide-description {
        font-size: clamp(1rem, 2vw, 1.2rem);
        opacity: 0.9;
        margin-bottom: 15px;
    }
    
    .slide-link {
        display: inline-block;
        background-color: #4d96ff;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .slide-link:hover {
        background-color: #357ae8;
        transform: translateY(-2px);
    }
    
    @media (max-width: 768px) {
        .slide-content {
            padding: 20px;
            transform: translateY(0);
            background: rgba(0, 0, 0, 0.7);
        }
        
        .slide-title {
            font-size: 1.3rem;
        }
        
        .slide-description {
            font-size: 0.9rem;
        }
    }
`;

document.head.appendChild(slideStyles);