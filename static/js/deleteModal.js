// static/js/deleteModal.js

document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.btn-danger');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', () => {
            console.log('O‘chirish tugmasi bosildi');
        });
    });
});
