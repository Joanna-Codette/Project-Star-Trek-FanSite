alert("Is this file connected?");

const searchButton = document.querySelector('#search-id');

searchButton.addEventListener('submit', evt => {
    evt.preventDefault();  //don't do anything, STOP!
    console.log("default preventing");

    const email = document.querySelector('#email-search').value
    //get the values and put that in an object
    const formInput = {
        email: email,
    };

    // fetch - package up in the back-end (mailing it to the address)
    fetch('/searchResult.json', {
        method: 'POST',
        body: JSON.stringify(formInput),
        headers: {
            'Content-Type': 'application/json',
        },
    })
        // . when the mail arrives, and then response
        .then((response) => response.json())
        .then((result) => {
            let display = `<p>${email}</p>`;
            for (const review of result) {
              display = display + `<p>${review.review_title}</p>` 
              display = display + `<p>${review.user_review}</p>` 
            }
            console.log(result);
            document.querySelector("#searchResult").innerHTML = `<p>${display}</p>`
        }) 
})

// editButtons = document.querySelectorAll('.edit-movie-rating');

// for (const button of editButtons) {
//   button.addEventListener('click', () => {
//     // first ask the user what they want the new rating to be
//     const newScore = prompt('What is your new score for this movie?');
//     const formInputs = {
//       updated_score: newScore,
//       rating_id: button.id,
//     };

//     // send a fetch request to the update_rating route
//     fetch('/update_rating', {
//       method: 'POST',
//       body: JSON.stringify(formInputs),
//       headers: {
//         'Content-Type': 'application/json',
//       },
//     }).then((response) => {
//       if (response.ok) {
//         document.querySelector(`span.rating_num_${button.id}`).innerHTML = newScore;
//       } else {
//         alert('Failed to update rating.');
//       }
//     });
//   });
// }


