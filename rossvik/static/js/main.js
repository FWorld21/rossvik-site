document.addEventListener('DOMContentLoaded', () => {
  // Subcategory
  const categoryTop = document.querySelectorAll('[data-category-top]');
  const categoryBottom = document.querySelectorAll('[data-category-bottom]');
  const subCategoryTop = document.querySelectorAll('.subcategory-top');
  const subCategoryBottom = document.querySelectorAll('.subcategory-bottom');
  const subCategoryClose = document.querySelectorAll('.subcategory-close');
  // const hamburgerButton = document.querySelector('.hamburger-menu');
  // const hamburger = document.querySelector('.hamburger');

  for (let i = 0; i < subCategoryClose.length; i++) {
    subCategoryClose[i].addEventListener('click', () => {
      hideSubCategory();
    });
  }

  for (let i = 0; i < categoryTop.length; i++) {
    subCategoryTop[i].classList.remove('show');
    subCategoryBottom[i].classList.remove('show');
  }

  const hideSubCategory = () => {
    for (let i = 0; i < categoryTop.length; i++) {
      subCategoryTop[i].classList.remove('show');
      subCategoryBottom[i].classList.remove('show');
    }
  };

  for (let i = 0; i < categoryTop.length; i++) {
    categoryTop[i].addEventListener('click', (event) => {
      const target = event.target;
      hideSubCategory();
      subCategoryTop[i].classList.toggle('show');
      if (target.classList.contains('show')) {
        subCategoryTop[i].classList.remove('show');
      }
    });
  }

  for (let i = 0; i < categoryBottom.length; i++) {
    categoryBottom[i].addEventListener('click', () => {
      hideSubCategory();
      subCategoryBottom[i].classList.toggle('show');
    });
  }

  // Закрытие модалки через ESC
  document.addEventListener('keydown', (e) => {
    for (let i = 0; i < categoryTop.length; i++) {
      if (e.code === 'Escape' && subCategoryTop[i].classList.contains('show')) {
        hideSubCategory();
      } else if (
        e.code === 'Escape' &&
        subCategoryBottom[i].classList.contains('show')
      ) {
        hideSubCategory();
      }
    }
  });

  // function openSubcategory() {
  //   subCategory.classList.toggle('show');
  // }

  // function closeSubcategory() {
  //   for (let i = 0; i < categoryTop.length; i++) {
  //     subCategoryTop[i].classList.remove('show');
  //     subCategoryBottom[i].classList.remove('show');
  //   }
  // }

  // modalTop.forEach((btn) => {
  //   btn.addEventListener('click', openSubcategory);
  // });

  // modalBottom.forEach((btn) => {
  //   btn.addEventListener('click', openSubcategory);
  // });

  // hamburgerButton.addEventListener('click', function () {
  //   hamburger.classList.toggle('show');
  // });

  // // Aside

  // asideTitle.forEach((elem, i) => {
  //   elem.addEventListener('click', () => {
  //     // elem.classList.toggle('active');
  //     asideList[i].classList.toggle('show');
  //   });
  // });

  // const accordion = () => {
  //   const asideList = document.querySelector('.aside-list');
  //   const asideItem = document.querySelectorAll('.aside-list__item');

  //   const open = (button, dropDown) => {
  //     dropDown.style.height = `${dropDown.scrollHeight}px`;
  //     button.classList.add('show');
  //     dropDown.classList.add('show');
  //   };

  //   const close = (button, dropDown) => {
  //     button.classList.remove('show');
  //     dropDown.classList.remove('show');
  //     dropDown.style.height = '';
  //   };

  //   asideList.addEventListener('click', (e) => {
  //     const target = e.target;
  //     if (target.classList.contains('aside-title')) {
  //       const parent = target.closest('.aside-list__item');
  //       console.log(parent);
  //     }
  //   });
  // };

  // accordion();
});
