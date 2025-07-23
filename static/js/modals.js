// static/js/modals.js
document.addEventListener('DOMContentLoaded', function () {
    // Modal ochilganda inputlarni tozalash yoki fokus qilish uchun kerak bo'lishi mumkin
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.addEventListener('hidden.bs.modal', () => {
            const form = modal.querySelector('form');
            if (form) form.reset();
        });
    });
});
