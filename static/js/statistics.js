// static/js/statistics.js
console.log("loaded!");

// 1. Oy bo'yicha trend (Line Chart)
if (window.MONTHS && window.TIME_SERIES) {
  const lineCtx = document.getElementById('lineChart');
  if (lineCtx) {
    new Chart(lineCtx.getContext('2d'), {
      type: 'line',
      data: {
        labels: window.MONTHS,
        datasets: [{
          label: "Oy bo'yicha xarajatlar (so'm)",
          data: window.TIME_SERIES,
          borderWidth: 2,
          fill: false,
          tension: 0.3,
          pointRadius: 3,
          pointBackgroundColor: '#4e73df',
          borderColor: '#4e73df'
        }]
      },
      options: {
        responsive: true,
        plugins: {
          tooltip: { mode: 'index', intersect: false },
          legend: { display: false }
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: function(value) { return value.toLocaleString(); }
            }
          }
        }
      }
    });
  }
}

// 2. Kategoriya bo'yicha taqsimot (Doughnut Chart)
if (window.CAT_LABELS && window.CAT_DATA) {
  const donutCtx = document.getElementById('donutChart');
  if (donutCtx) {
    new Chart(donutCtx.getContext('2d'), {
      type: 'doughnut',
      data: {
        labels: window.CAT_LABELS.map(l => l.charAt(0).toUpperCase() + l.slice(1)),
        datasets: [{
          data: window.CAT_DATA,
          backgroundColor: [
            '#4e73df', // ovqat
            '#1cc88a', // transport
            '#36b9cc', // salomatlik
            '#f6c23e'  // boshqa
          ],
          hoverOffset: 6
        }]
      },
      options: {
        responsive: true,
        plugins: {
          tooltip: {
            callbacks: {
              label: function(ctx) {
                const v = ctx.parsed;
                const label = ctx.label;
                return label + ': ' + v.toLocaleString() + ' so\'m';
              }
            }
          },
          legend: {
            position: 'bottom',
            labels: { usePointStyle: true, padding: 20 }
          }
        }
      }
    });
  }
}


console.log("MONTHS:", window.MONTHS);
console.log("TIME_SERIES:", window.TIME_SERIES);
console.log("CAT_LABELS:", window.CAT_LABELS);
console.log("CAT_DATA:", window.CAT_DATA);
