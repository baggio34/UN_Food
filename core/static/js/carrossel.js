let currentIndex = 0;
const totalItems = 8;
const itemsPerView = 4;

function moveNext() {
    if (currentIndex < totalItems - itemsPerView) {
        currentIndex++;
        updateCarousel();
    }
}

function movePrev() {
    if (currentIndex > 0) {
        currentIndex--;
        updateCarousel();
    }
}

function updateCarousel() {
    const track = document.querySelector('.carousel-itens');
    const itemWidth = document.querySelector('.carousel-item').clientWidth;
    const newPosition = -(itemWidth) * currentIndex;
    track.style.transform = `translateX(${newPosition}px)`;
}
let currentIndex2 = 0;
const totalItems2 = 8;
const itemsPerView2 = 4;

function moveNext2() {
    if (currentIndex2 < totalItems2 - itemsPerView2) {
        currentIndex2++;
        updateCarousel2();
    }
}

function movePrev2() {
    if (currentIndex2 > 0) {
        currentIndex2--;
        updateCarousel2();
    }
}

function updateCarousel2() {
    const track2 = document.querySelector('.carousel-itens2');
    const itemWidth2 = document.querySelector('.carousel-item2').clientWidth;
    const newPosition2 = -(itemWidth2) * currentIndex2;
    track2.style.transform = `translateX(${newPosition2}px)`;
}

