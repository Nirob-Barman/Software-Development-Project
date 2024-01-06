const loadUsers = () => {
    fetch("https://fakestoreapi.com/users")
      .then((res) => res.json())
      .then((users) => {
        const userListContainer = document.getElementById("userListContainer");

        // Create a row container
        let rowContainer;

        users.forEach((user, index) => {
          // Create a new row for every three cards
          if (index % 3 === 0) {
            rowContainer = document.createElement("div");
            rowContainer.className = "row";
            userListContainer.appendChild(rowContainer);
          }

          const userCard = document.createElement("div");
          userCard.className = "col-md-4 mb-3"; // Adjust the column size based on your layout

          userCard.innerHTML = `
              <div class="card text-center">
                  <div class="card-body">
                      <h5 class="card-title">${user.name.firstname} ${user.name.lastname}</h5>
                      <p class="card-text"><strong>Email:</strong> ${user.email}</p>
                      <p class="card-text"><strong>Username:</strong> ${user.username}</p>
                      <a href="singleUser.html?id=${user.id}" class="btn btn-primary">Details</a>
                  </div>
              </div>
          `;

          // Append the card to the current row
          rowContainer.appendChild(userCard);
        });
      });
  };



const loadSingleUser = () => {
    const params = new URLSearchParams(window.location.search).get("id");
    
    fetch(`https://fakestoreapi.com/users/${params}`)
    .then((res) => res.json())
    .then((user) => {
        const userCard = document.getElementById("userCard");
        userCard.innerHTML = `
            <div class="card mb-3 w-50 mx-auto">
                <div class="card-body">
                    <p class="card-text text-center">Hey, ${user.username}</p>
                    <h5 class="card-title">Name: ${user.name.firstname} ${user.name.lastname}</h5>
                    <p class="card-text"><strong>Email:</strong> ${user.email}</p>
                    <p class="card-text"><strong>Phone:</strong> ${user.phone}</p>
                    <p class="card-text"><strong>Address:</strong> ${user.address.city}, ${user.address.street}, ${user.address.number}, ${user.address.zipcode}</p>
                    <div class="d-flex justify-content-around">
                        <p class="card-text"><strong>Latitude:</strong> ${user.address.geolocation.lat}</p>
                        <p class="card-text"><strong>Longitude:</strong> ${user.address.geolocation.long}</p>
                    </div>
                </div>
            </div>
        `;
    })
}



loadSingleUser();
loadUsers();