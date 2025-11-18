// Weighted random navigation on click.
// Reads outcomes and weights from data attributes for easy tweaking.
(function () {
  const link = document.getElementById('surprise-link');
  if (!link) return;

  const outcomes = (link.dataset.outcomes || '').split(',').map(s => s.trim());
  let weights = (link.dataset.weights || '').split(',').map(s => parseFloat(s.trim()));
  if (outcomes.length < 2) return;

  // Fallback: if weights invalid, default to [90,10]
  if (weights.length !== outcomes.length || weights.some(w => !isFinite(w) || w < 0)) {
    weights = [90, 10];
  }

  // Normalize weights
  const total = weights.reduce((a, b) => a + b, 0) || 1;
  const probs = weights.map(w => w / total);

  // Build cumulative distribution
  const cumulative = [];
  probs.reduce((acc, p, i) => {
    const v = acc + p;
    cumulative[i] = v;
    return v;
  }, 0);

  link.addEventListener('click', (e) => {
    // Progressive enhancement—if JS is disabled, default href works.
    e.preventDefault();

    // Simple pick
    const r = Math.random();
    let idx = cumulative.findIndex(c => r < c);
    if (idx < 0) idx = outcomes.length - 1;

    // Optional: show a tiny “thinking” delay for flair
    link.classList.add('busy');
    setTimeout(() => {
      window.location.href = outcomes[idx];
    }, 200); // tweak or remove
  }, { passive: false });
})();
