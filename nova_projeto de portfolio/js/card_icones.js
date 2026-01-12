const observerHabilidades = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
            // Delay de 600ms por card para uma cadência bem lenta
            setTimeout(() => {
                entry.target.classList.add('show');
            }, index * 600); 
        }
    });
}, { threshold: 0.1 });

// Seleciona todos os cards com a classe padronizada
document.querySelectorAll('.card_habilidade').forEach(card => {
    observerHabilidades.observe(card);
});