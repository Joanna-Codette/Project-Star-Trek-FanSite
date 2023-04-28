searchButtons = document.querySelectorAll('.');
editButtons = document.querySelectorAll('.edit-movie-rating');

button.addEventListener('click', () => {
    // send a fetch a request to the get_user email 
    const searchInputs = { 
        user_email: user.email
    };
    fetch('/all_users', {
        method: 'POST',
        body: JSON.stringify(searchInputs),
        headers:{
            'Content-Type': 'application/json',
        },
    }).then((response) => {
        if (response.ok) {
            document.querySelector(user.email)
        }
    })
});


for (const button of editButtons) {
  button.addEventListener('click', () => {
    // first ask the user what they want the new rating to be
    const newScore = prompt('What is your new score for this movie?');
    const formInputs = {
      updated_score: newScore,
      rating_id: button.id,
    };

    // send a fetch request to the update_rating route
    fetch('/update_rating', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    }).then((response) => {
      if (response.ok) {
        document.querySelector(`span.rating_num_${button.id}`).innerHTML = newScore;
      } else {
        alert('Failed to update rating.');
      }
    });
  });
}
