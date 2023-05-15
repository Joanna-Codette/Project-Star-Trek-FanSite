//update review
const editReviewButtons = document.querySelectorAll('.edit-movie-review');

for (const button of editReviewButtons) {
  button.addEventListener('click', () => {
    // first ask the user what they want the new rating to be
    const newReview = prompt('Please update your review');
    const reviewID = button.id;
    const formInputs = {
      "review_id": reviewID,
      "updated_review": newReview,
    };

    // send a fetch request to the update_review route
    fetch('/update_review', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then(response => response.text())
    .then((responseText) => {
        const reviewHTML = document.querySelector(`#review_${reviewID}`);
        reviewHTML.innerHTML = newReview; //using the DOM manipulation to change what's on the page
    })
  })
}