document.addEventListener('DOMContentLoaded', () => {

  // Subcategory
  const modalTrigger = document.querySelectorAll('[data-subCategory]');
  const subCategory = document.querySelector('.subcategory');

  function openSubcategory() {
    subCategory.classList.toggle('show');
  }

  function closeSubcategory() {
    subCategory.classList.add('show');
  }

  modalTrigger.forEach(btn => {
    btn.addEventListener('click', openSubcategory);
  });

  document.addEventListener('keydown', (e) => {
    if (e.code === 'Escape' && subCategory.classList.contains('show')) {
      closeSubcategory();
    }
  });

  // modal.addEventListener('click', (e) => {
  //   if (e.target === modal || e.target.getAttribute('data-close') == '') {
  //     closeModal();
  //   }
  // });

});