document.addEventListener("DOMContentLoaded", function () {
  // 2. Xarajatlar trendi: Combo Chart (bar + line)
  const comboCtx = document.getElementById("comboChart");

  if (comboCtx && window.MONTHS && window.TIME_SERIES && window.RATIOS) {
    // 1. Oxirgi o‘sish foizi noto‘g‘ri (-100 yoki null) bo‘lsa, uni 0 ga almashtirish
    const lastIndex = window.RATIOS.length - 1;
    const lastRatio = window.RATIOS[lastIndex];
    if (lastRatio === -100 || lastRatio === null || lastRatio === undefined) {
      window.RATIOS[lastIndex] = 0;
    }

    new Chart(comboCtx.getContext("2d"), {
      type: "bar",
      data: {
        labels: window.MONTHS,
        datasets: [
          {
            type: "bar",
            label: "Jami xarajatlar (so'm)",
            data: window.TIME_SERIES,
            backgroundColor: "#4e73df",
            borderRadius: 5,
            barPercentage: 0.6,
            yAxisID: "y",
            order: 2 // Ko'k ustunlar orqada
          },
          {
            type: "line",
            label: "O‘sish foizi (%)",
            data: window.RATIOS,
            borderColor: "#f6c23e",
            backgroundColor: "#f6c23e",
            borderWidth: 3,
            tension: 0.4,
            yAxisID: "y1",
            pointRadius: 4,
            pointHoverRadius: 6,
            fill: false,
            order: 1, // Sariq chiziq ustida ko'rinadi
            segment: {
              borderWidth: 3,
              borderColor: "#f6c23e"
            }
          }
        ]
      },
      options: {
        responsive: true,
        interaction: {
          mode: "index",
          intersect: false
        },
        plugins: {
          tooltip: {
            mode: "index",
            intersect: false,
            callbacks: {
              label: function (context) {
                if (context.dataset.type === "line") {
                  return `${context.dataset.label}: ${context.formattedValue}%`;
                } else {
                  return `${context.dataset.label}: ${parseInt(context.raw).toLocaleString()} so'm`;
                }
              }
            }
          },
          legend: {
            position: "top"
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: "Xarajat (so'm)"
            },
            ticks: {
              callback: function (value) {
                return value.toLocaleString();
              }
            }
          },
          y1: {
            position: "right",
            min: -100,
            max: 100,
            title: {
              display: true,
              text: "O‘sish (%)"
            },
            ticks: {
              callback: function (value) {
                return value + "%";
              }
            },
            grid: {
              drawOnChartArea: false
            }
          }
        }
      }
    });
  }


  // 4. Kategoriya ulushi: Donut Chart
  const donutCtx = document.getElementById("donutChart");
  if (donutCtx && window.CAT_LABELS && window.CAT_DATA) {
    new Chart(donutCtx.getContext("2d"), {
      type: "doughnut",
      data: {
        labels: window.CAT_LABELS,
        datasets: [
          {
            label: "Kategoriya ulushi",
            data: window.CAT_DATA,
            backgroundColor: [
              "#4e73df", "#1cc88a", "#36b9cc", "#f6c23e", "#e74a3b", "#858796",
              "#fd7e14", "#20c997", "#6f42c1", "#00bcd4"
            ],
            borderWidth: 1
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: "bottom"
          },
          tooltip: {
            callbacks: {
              label: function (context) {
                const label = context.label || "";
                const value = context.raw || 0;
                return `${label}: ${value.toLocaleString()} so'm`;
              }
            }
          }
        }
      }
    });
  }
});
