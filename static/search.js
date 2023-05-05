//alert("Is this file connected?");

const searchButton = document.querySelector('#search-email');

searchButton.addEventListener("submit", evt => {
    evt.preventDefault(); // default event will not happen
    console.log("default preventing");
  
    const email = document.querySelector("#email-search").value;
  
    const formInput = {
        email: email,
  };
  
  fetch('/searchResult.text', {
    method: 'POST',
    body: JSON.stringify(formInput),
    headers: {
      'Content-Type': 'application/json',
    },
  })
  .then ((response) => response.json()) //in server.py return a dictionary - cannot convert to text, only to json
  .then ((result) => {
    // if email found in database, print email address
    const email = result['email']
    const user_id = result['user_id']
    document.querySelector("#searchResult").innerHTML = `<a href="/users/${user_id}">${email}</a>` //refer to server.py line 84
  },

  
)})