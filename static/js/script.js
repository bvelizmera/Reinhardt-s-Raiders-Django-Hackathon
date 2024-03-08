const editButtons = document.getElementsByClassName('btn-edit');
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById('reviewForm');
const submitButton = document.getElementById('submitButton');

const deleteModal = new bootstrap.Modal(document.getElementById("delete_Modal"));
const deleteButtons = document.getElementsByClassName("delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
      console.log(`Event triggered: ${e.target.id}`)
      let reviewId = e.target.id;
      reviewId = reviewId.replace("edit_", "")
      let reviewContent = document.getElementById(`review${reviewId}`).innerText;
      reviewText.value = reviewContent;
      submitButton.innerText = "Update";
      reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

for (let button of deleteButtons) {
    
    button.addEventListener("click", (e) => {
      let reviewId = e.srcElement.id;
      deleteConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
  }