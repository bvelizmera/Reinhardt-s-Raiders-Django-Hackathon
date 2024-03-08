const editButtons = document.getElementsByClassName('btn-edit');
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById('commentForm');
const submitButton = document.getElementById('submitButton');

const deleteModal = new bootstrap.Modal(document.getElementById("delete_Modal"));
const deleteButtons = document.getElementsByClassName("delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");
console.log('Hello from JS!')
for (let button of deleteButtons) {
    
    button.addEventListener("click", (e) => {
      let reviewId = e.srcElement.id;
      deleteConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
  }