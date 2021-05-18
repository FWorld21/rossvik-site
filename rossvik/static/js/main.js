document.addEventListener('DOMContentLoaded', () => {
  const subCategory = document.querySelectorAll('.subcategory');
  const category = document.querySelectorAll('[data-category]');
  const subCategoryClose = document.querySelectorAll('.subcategory-close');
  const hamburger = document.querySelector('.hamburger-menu');
  const navigation = document.querySelector('.navigation');
  const body = document.querySelector('body');

  // Скрытие подкатегории
  const hideAll = () => {
    for (let i = 0; i < category.length; i++) {
      subCategory[i].classList.remove('show');
    }
  };

  // Закрытие модалки через ESC
  document.addEventListener('keydown', (e) => {
    for (let i = 0; i < category.length; i++) {
      if (e.code === 'Escape' && subCategory[i].classList.contains('show')) {
        hideAll();
      }
    }
  });

  // Закрытие подкатегории через крестик
  for (let i = 0; i < subCategoryClose.length; i++) {
    subCategoryClose[i].addEventListener('click', () => {
      hideAll();
    });
  }

  // Открытие подкатегории
  for (let i = 0; i < category.length; i++) {
    category[i].addEventListener('click', () => {
      hideAll();
      subCategory[i].classList.add('show');
    });
  }

  // Бургер меню
  hamburger.addEventListener('click', () => {
    navigation.classList.toggle('change');
    body.classList.toggle('hide');
  });
});
