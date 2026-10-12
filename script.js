// Accessible single-page navigation.
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener('click', (event) => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (!target) return;
    event.preventDefault();
    target.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  });
});

// Search and category filters for recruiter-facing project cards.
(() => {
  const search = document.getElementById('project-search');
  const buttons = [...document.querySelectorAll('[data-filter]')];
  const cards = [...document.querySelectorAll('.work[data-category]')];
  const result = document.getElementById('project-results');
  if (!search || !buttons.length || !cards.length || !result) return;

  let activeFilter = 'all';
  const applyFilters = () => {
    const query = search.value.trim().toLowerCase();
    let visible = 0;
    cards.forEach((card) => {
      const categoryMatch = activeFilter === 'all' || card.dataset.category === activeFilter;
      const textMatch = !query || (card.innerText + ' ' + (card.dataset.search || '')).toLowerCase().includes(query);
      const show = categoryMatch && textMatch;
      card.hidden = !show;
      if (show) visible += 1;
    });
    result.textContent = `Showing ${visible} of ${cards.length} projects`;
  };

  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      activeFilter = button.dataset.filter || 'all';
      buttons.forEach((item) => {
        const selected = item === button;
        item.classList.toggle('active', selected);
        item.setAttribute('aria-pressed', String(selected));
      });
      applyFilters();
    });
  });
  search.addEventListener('input', applyFilters);
  applyFilters();
})();
