// update ratings
const searchButton = document.getElemetnById('search-email')
const editButtons = document.querySelectorAll('.edit-movie-rating');

searchButton.addEventListener("submit", evt => {
  evt.preventDefault(); //cancels the event if it is cancelable, 
                        //meaning that the default action that belongs to the event will not occur. 
  console.log("")
})


for (const button of editButtons) {
  button.addEventListener('click', () => {
    // first ask the user what they want the new rating to be
    const newScore = prompt('What is your new score for this movie?');
    const ratingID = button.id;
    const formInputs = {
      "rating_id": ratingID,
      "updated_score": newScore,
    };

    // send a fetch request to the update_rating route
    fetch('/update_rating', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then(response => response.text())
    .then((responseText) => {
        const scoreHTML = document.querySelector(`#score_${ratingID}`);
        scoreHTML.innerHTML = newScore; //using the DOM manipulation to change what's on the page
    })
  })
}
