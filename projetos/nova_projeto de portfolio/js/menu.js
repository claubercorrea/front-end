document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navmenu');
    
    // Verifica se os elementos existem na página antes de rodar
    if (menuToggle && navMenu) {
        
        // Abre e fecha o menu ao clicar no ícone
        menuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            // Opcional: animação no ícone se desejar
            menuToggle.classList.toggle('active');
        });
        
        // Fecha o menu automaticamente ao clicar em um link
        const links = document.querySelectorAll('.link_lista');
        links.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                menuToggle.classList.remove('active');
            });
        });
    }
});