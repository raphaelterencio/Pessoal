let currentPhotoIndex = 0;
let noButtonClickCount = 0;
const totalPhotos = 4;

// --- Carrossel de fotos personalizado ---
let currentCarouselIndex = 0;
const totalCarouselPhotos = 4;
let carouselInterval;

// Função para controlar o áudio
let isPlaying = true;
const audio = document.getElementById('backgroundMusic');
const audioButton = document.getElementById('audioControl');

// Inicialização
document.addEventListener("DOMContentLoaded", function() {
    startPhotoSlideshow();
    setupDotNavigation();
    startCustomCarousel();
    setupCarouselDotNavigation();
    audio.play().then(() => {
        isPlaying = true;
        audioButton.textContent = '🔊';
    }).catch(() => {
        isPlaying = false;
        audioButton.textContent = '🔇';
    });
});

// Slideshow automático das fotos
function startPhotoSlideshow() {
    setInterval(() => {
        nextPhoto();
    }, 3000); // Muda a foto a cada 3 segundos
}

// Próxima foto
function nextPhoto() {
    const photos = document.querySelectorAll(".user-photo");
    const dots = document.querySelectorAll(".dot");
    
    // Remove active da foto atual
    photos[currentPhotoIndex].classList.remove("active");
    dots[currentPhotoIndex].classList.remove("active");
    
    // Próximo índice
    currentPhotoIndex = (currentPhotoIndex + 1) % totalPhotos;
    
    // Adiciona active na nova foto
    photos[currentPhotoIndex].classList.add("active");
    dots[currentPhotoIndex].classList.add("active");
}

// Navegação por pontos
function setupDotNavigation() {
    const dots = document.querySelectorAll(".dot");
    dots.forEach((dot, index) => {
        dot.addEventListener("click", () => {
            goToPhoto(index);
        });
    });
}

// Ir para foto específica
function goToPhoto(index) {
    const photos = document.querySelectorAll(".user-photo");
    const dots = document.querySelectorAll(".dot");
    
    // Remove active de todos
    photos.forEach(photo => photo.classList.remove("active"));
    dots.forEach(dot => dot.classList.remove("active"));
    
    // Adiciona active no selecionado
    photos[index].classList.add("active");
    dots[index].classList.add("active");
    
    currentPhotoIndex = index;
}

// Ir para seção da mensagem
function goToMessage() {
    document.getElementById("photoSection").classList.add("hidden");
    document.getElementById("messageSection").classList.remove("hidden");
    
    // Adiciona efeito de entrada
    const messageSection = document.getElementById("messageSection");
    messageSection.style.opacity = "0";
    messageSection.style.transform = "translateY(50px)";
    
    setTimeout(() => {
        messageSection.style.transition = "all 0.5s ease";
        messageSection.style.opacity = "1";
        messageSection.style.transform = "translateY(0)";
    }, 100);
}

// Mostrar filmes
function showMovies() {
    document.getElementById("messageSection").classList.add("hidden");
    document.getElementById("moviesSection").classList.remove("hidden");
    
    // Adiciona efeito de entrada
    const moviesSection = document.getElementById("moviesSection");
    moviesSection.style.opacity = "0";
    moviesSection.style.transform = "translateY(50px)";
    
    setTimeout(() => {
        moviesSection.style.transition = "all 0.5s ease";
        moviesSection.style.opacity = "1";
        moviesSection.style.transform = "translateY(0)";
    }, 100);
}

// Mover botão "Não"
function moveNoButton() {
    const noButton = document.getElementById("noButton");
    noButtonClickCount++;
    
    if (noButtonClickCount < 4) {
        // Adiciona classe de animação
        noButton.classList.add("moving");
        
        // Remove a classe após a animação
        setTimeout(() => {
            noButton.classList.remove("moving");
        }, 500);
        
        // Define posições específicas para cantos da tela (mobile-friendly)
        const positions = [
            { x: -120, y: -80 },   // Canto superior esquerdo
            { x: 120, y: -80 },    // Canto superior direito
            { x: -120, y: 80 },    // Canto inferior esquerdo
            { x: 120, y: 80 }      // Canto inferior direito
        ];
        
        const position = positions[noButtonClickCount - 1];
        noButton.style.transform = `translate(${position.x}px, ${position.y}px)`;
        
        // Mantém apenas "Não" no texto
        noButton.innerHTML = "Não 😢";
    } else {
        // Após 4 cliques, o botão desaparece
        noButton.style.transition = "all 0.5s ease";
        noButton.style.opacity = "0";
        noButton.style.transform = "scale(0)";
        
        setTimeout(() => {
            noButton.style.display = "none";
            
            // Mostra mensagem especial
            const messageContainer = document.querySelector(".message-container");
            const specialMessage = document.createElement("div");
            specialMessage.innerHTML = `
                <p style="color: #ff6b9d; font-size: 1.2rem; margin-top: 1rem;">
                    Essa não tem como escapar! Eu sei que você quer assistir um filmezinho comigo! 😉💕
                </p>
                <button onclick="showMovies()" style="
                    background: linear-gradient(45deg, #4CAF50, #66BB6A);
                    color: white;
                    border: none;
                    padding: 1rem 2rem;
                    border-radius: 25px;
                    font-size: 1.2rem;
                    font-weight: bold;
                    cursor: pointer;
                    margin-top: 1rem;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
                ">
                    Tá bom, vamos assistir! ❤️
                </button>
            `;
            messageContainer.appendChild(specialMessage);
        }, 500);
    }
}

// Selecionar filme
function selectMovie(movieTitle) {
    document.getElementById("moviesSection").classList.add("hidden");
    document.getElementById("confirmationSection").classList.remove("hidden");
    document.getElementById("selectedMovie").textContent = `Você escolheu: ${movieTitle}`;
    
    // Adiciona efeito de entrada
    const confirmationSection = document.getElementById("confirmationSection");
    confirmationSection.style.opacity = "0";
    confirmationSection.style.transform = "translateY(50px)";
    
    setTimeout(() => {
        confirmationSection.style.transition = "all 0.5s ease";
        confirmationSection.style.opacity = "1";
        confirmationSection.style.transform = "translateY(0)";
    }, 100);
    
    // Adiciona confetes
    createConfetti();
}

// Voltar para mensagem
function goBackToMessage() {
    document.getElementById("moviesSection").classList.add("hidden");
    document.getElementById("messageSection").classList.remove("hidden");
}

// Reiniciar
function restart() {
    // Reset todas as variáveis
    currentPhotoIndex = 0;
    noButtonClickCount = 0;
    
    // Reset botão "Não"
    const noButton = document.getElementById("noButton");
    noButton.style.display = "inline-block";
    noButton.style.opacity = "1";
    noButton.style.transform = "translate(0, 0) scale(1)";
    noButton.innerHTML = "Não 😢";
    
    // Remove mensagem especial se existir
    const specialMessages = document.querySelectorAll(".message-container > div:last-child");
    specialMessages.forEach(msg => {
        if (msg.innerHTML.includes("Ah, que pena!")) {
            msg.remove();
        }
    });
    
    // Volta para a primeira seção
    document.getElementById("confirmationSection").classList.add("hidden");
    document.getElementById("moviesSection").classList.add("hidden");
    document.getElementById("messageSection").classList.add("hidden");
    document.getElementById("photoSection").classList.remove("hidden");
    
    // Reset fotos
    goToPhoto(0);
}

// Criar confetes
function createConfetti() {
    const colors = ["#ff6b9d", "#ff8e8e", "#ffa8a8", "#ffb3ba", "#ffc0cb"];
    
    for (let i = 0; i < 50; i++) {
        setTimeout(() => {
            const confetti = document.createElement("div");
            confetti.style.position = "fixed";
            confetti.style.left = Math.random() * 100 + "vw";
            confetti.style.top = "-10px";
            confetti.style.width = "10px";
            confetti.style.height = "10px";
            confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            confetti.style.borderRadius = "50%";
            confetti.style.pointerEvents = "none";
            confetti.style.zIndex = "1000";
            confetti.style.animation = "confettiFall 3s linear forwards";
            
            document.body.appendChild(confetti);
            
            setTimeout(() => {
                confetti.remove();
            }, 3000);
        }, i * 50);
    }
}

// Adiciona CSS para animação de confetes
const style = document.createElement("style");
style.textContent = `
    @keyframes confettiFall {
        to {
            transform: translateY(100vh) rotate(360deg);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

function startCustomCarousel() {
    carouselInterval = setInterval(() => {
        nextCarouselPhoto();
    }, 3000);
}

function nextCarouselPhoto() {
    const photos = document.querySelectorAll(".carousel-photo");
    const dots = document.querySelectorAll(".carousel-dot");
    photos[currentCarouselIndex].classList.remove("active");
    dots[currentCarouselIndex].classList.remove("active");
    currentCarouselIndex = (currentCarouselIndex + 1) % totalCarouselPhotos;
    photos[currentCarouselIndex].classList.add("active");
    dots[currentCarouselIndex].classList.add("active");
}

function goToCarouselPhoto(index) {
    const photos = document.querySelectorAll(".carousel-photo");
    const dots = document.querySelectorAll(".carousel-dot");
    photos[currentCarouselIndex].classList.remove("active");
    dots[currentCarouselIndex].classList.remove("active");
    currentCarouselIndex = index;
    photos[currentCarouselIndex].classList.add("active");
    dots[currentCarouselIndex].classList.add("active");
}

function setupCarouselDotNavigation() {
    const dots = document.querySelectorAll(".carousel-dot");
    dots.forEach((dot, index) => {
        dot.addEventListener("click", () => {
            goToCarouselPhoto(index);
            clearInterval(carouselInterval);
            startCustomCarousel();
        });
    });
}

function toggleAudio() {
    if (isPlaying) {
        audio.pause();
        audioButton.textContent = '🔇';
    } else {
        audio.play();
        audioButton.textContent = '🔊';
    }
    isPlaying = !isPlaying;
}


