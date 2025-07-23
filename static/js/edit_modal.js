document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("form[id^='editForm']").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const formData = new FormData(form);
      fetch(form.action, {
        method: "POST",
        body: formData,
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        },
      })
        .then((res) => {
          if (res.redirected) {
            window.location.href = res.url;
          } else {
            window.location.reload(); // yoki modalni yopish
          }
        })
        .catch((err) => console.error("Xatolik:", err));
    });
  });
});
