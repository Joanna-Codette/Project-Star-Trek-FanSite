alert("Is this file connected?");

const searchButton = document.querySelector('#search-email');

searchButton.addEventListener("submit", evt => {
    evt.preventDefault(); // default event will not happen
    console.log("default preventing");
  
    const email = document.querySelector("email-search").value;
  
    const formInput = {
        email: email,
  };
  
  fetch('/searchResult.json', {
    method: 'POST',
    body: JSON.stringify(formInput),
    hearders: {
      'Content-Type': 'application/json',
    },
  })
  .then ((response) => response.json())
  .then ((result) => {
    // if email found in database, print email address
    let email = '<p>${email}</p>';
  },
  
  document.querySelector("#searchResult").innerHTML = "<p>${email}</p>"  
)})