// check for IntersectionObserver support
if ('IntersectionObserver' in window) {
    // create observer and add it to the hidden elements
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        entry.target.classList.toggle('show', entry.isIntersecting);
      });
    });
  
    const hiddenElements = document.querySelectorAll('.hidden');
    hiddenElements.forEach((el) => observer.observe(el));
  } else {
    // fallback for browsers that do not support IntersectionObserver
    hiddenElements.forEach((el) => el.classList.add('show'));
  }  