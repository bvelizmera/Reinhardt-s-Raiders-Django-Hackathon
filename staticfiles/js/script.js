

const deleteModal = new bootstrap.Modal(document.getElementById("delete_Modal"));
const deleteButtons = document.getElementsByClassName("delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");
for (let button of deleteButtons) {
    
    button.addEventListener("click", (e) => {
      let reviewId = e.srcElement.id;
      deleteConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
  }