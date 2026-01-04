document.addEventListener('DOMContentLoaded', function() {
                const menuToggle = document.getElementById('menuToggle');
                const navMenu = document.getElementById('navmenu');
                
                if (menuToggle && navMenu) {
                    menuToggle.addEventListener('click', function() {
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
                }
                
                // Ajustar animação do carrossel baseado na largura da tela
                function adjustCarouselAnimation() {
                    const items = document.querySelectorAll('.item');
                    const screenWidth = window.innerWidth;
                    
                    items.forEach((item, index) => {
                        if (screenWidth < 768) {
                            // Animação mais lenta em mobile
                            item.style.animationDuration = '15s';
                        } else {
                            // Animação normal em desktop
                            item.style.animationDuration = '10s';
                        }
                    });
                }
                
                // Executar na carga e no redimensionamento
                adjustCarouselAnimation();
                window.addEventListener('resize', adjustCarouselAnimation);
            });