const radios = document.querySelectorAll('input[name="theme"]');

radios.forEach(radio => {
  radio.addEventListener('change', (e) => {
    if (e.target.value === 'dark') {
      document.body.classList.add('dark');
    } else {
      document.body.classList.remove('dark');
    }
  });
});
