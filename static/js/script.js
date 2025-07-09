
document.addEventListener('DOMContentLoaded', function () {
  const editModal = document.getElementById("editModal");
  const statusModal = document.getElementById("statusModal");

  const editClose = document.getElementById("editModalClose");
  const statusClose = document.getElementById("statusModalClose");

  const form = document.getElementById("editForm");
  const deleteBtn = document.getElementById("deleteBtn");
  const saveStatusBtn = document.getElementById("saveStatusBtn");

  // Open edit modal
  document.querySelectorAll('.open-edit-modal').forEach(button => {
    button.addEventListener('click', () => {
      document.getElementById('post_id').value = button.dataset.id;
      document.getElementById('edit_title').value = button.dataset.title;
      document.getElementById('edit_text').value = button.dataset.text;
      document.getElementById('edit_date').value = button.dataset.date;
      editModal.style.display = "block";
    });
  });

  editClose.onclick = () => editModal.style.display = "none";
  statusClose.onclick = () => statusModal.style.display = "none";

  window.onclick = function(event) {
    if (event.target == editModal) editModal.style.display = "none";
    if (event.target == statusModal) statusModal.style.display = "none";
  };

  // Submit update
  form.onsubmit = function (e) {
    e.preventDefault();
    const postId = document.getElementById('post_id').value;
    const title = document.getElementById('edit_title').value;
    const text = document.getElementById('edit_text').value;
    const date = document.getElementById('edit_date').value;

    fetch(`/update-post/${postId}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
      },
      body: JSON.stringify({ title, text, date })
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        const row = document.querySelector(`tr[data-post-id="${postId}"]`);
        row.querySelector(".post-title").innerText = title;
        row.querySelector(".post-date").innerText = date;
        editModal.style.display = "none";
      } else {
        alert("Xatolik: " + data.error);
      }
    });
  };

  // Delete
  deleteBtn.addEventListener('click', function () {
    const postId = document.getElementById('post_id').value;
    if (!confirm("Postni o‘chirishga ishonchingiz komilmi?")) return;

    fetch(`/delete-post/${postId}/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
      }
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        document.querySelector(`tr[data-post-id="${postId}"]`).remove();
        editModal.style.display = "none";
      } else {
        alert("Xatolik: " + data.error);
      }
    });
  });

  // Open status modal
  document.querySelectorAll('.open-status-modal').forEach(button => {
    button.addEventListener('click', () => {
      const currentStatus = button.dataset.status === 'true';
      document.getElementById("newStatusSelect").value = currentStatus ? "true" : "false";
      document.getElementById("newStatusSelect").dataset.id = button.dataset.id;
      statusModal.style.display = "block";
    });
  });

  // Save status
  saveStatusBtn.addEventListener('click', function () {
    const select = document.getElementById("newStatusSelect");
    const postId = select.dataset.id;
    const status = select.value;

    fetch(`/update-status/${postId}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
      },
      body: JSON.stringify({ status: status })
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        const button = document.querySelector(`.open-status-modal[data-id="${postId}"]`);
        button.innerText = data.new_status ? 'Bajarildi' : 'Bajarilmadi';
        button.dataset.status = data.new_status.toString();
        statusModal.style.display = "none";
      } else {
        alert("Xatolik: " + data.error);
      }
    });
  });
});
