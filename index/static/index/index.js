// mobile nav menue 

const burgerIcon = document.querySelector('#burger')
const navbarMenu = document.querySelector('#my-navbar')

burgerIcon.addEventListener('click', () => {
    navbarMenu.classList.toggle('is-active');
})