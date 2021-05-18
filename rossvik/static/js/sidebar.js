const asideTitle = document.querySelector('.aside-title');
const asideList = document.querySelector('.aside-list');

asideTitle.addEventListener('click', (e) => {
  asideList.classList.toggle('aside-show');
});
