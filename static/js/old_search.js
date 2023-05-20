alert("Is this file connected?");

const searchButton = document.querySelector('#search-id');


searchButton.addEventListener('submit', evt => {
    evt.preventDefault();  //don't do anything, STOP!
    console.log("default preventing");

    //get the values and put that in an object
    const formInput = {
        email: document.querySelector('#email-search').value,
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
        .then(alert(response));  // check if it is successful

})

// function orderMelons(evt) {
//     evt.preventDefault();
//     const formInputs = {
//       melon_type: document.querySelector('#melon-type-field').value,
//       qty: document.querySelector('#qty-field').value,
//     };
//     fetch('/order-melons.json', {
//       method: 'POST',
//       body: JSON.stringify(formInputs),
//       headers: {
//         'Content-Type': 'application/json',
//       },
//     })
//       .then((response) => response.json())
//       .then(updateMelons);
//   }
  