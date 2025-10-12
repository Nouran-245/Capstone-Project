document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.getElementById('main-navbar');
    const scrollThreshold = 50;

    function toggleNavbarClass() {
        if (window.scrollY > scrollThreshold) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }

    window.addEventListener('scroll', toggleNavbarClass);
    toggleNavbarClass();
});