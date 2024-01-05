const handleRegistration = (event) => {
  event.preventDefault();

  const username = getValue("inputUsername");
  const first_name = getValue("inputFirstname");
  const last_name = getValue("inputLastname");
  const email = getValue("inputEmail");
  const password = getValue("inputPassword");
  const city = getValue("inputCity");
  const street = getValue("inputStreet");
  const number = getValue("inputNum");
  const zipcode = getValue("inputZip");
  const phone = getValue("Phone");
  const latitude = getValue("Latitude");
  const longitude = getValue("Longitude");
  const userDetails = {
    email,
    username,
    password,
    name: {
      first_name,
      last_name,
    },
    address: {
      city,
      street,
      number,
      zipcode,
      geolocation: {
        latitude,
        longitude,
      },
    },
    phone,
  };

  // console.log(userDetails);
  fetch('https://fakestoreapi.com/users',{
    method:"POST",
    body: JSON.stringify(userDetails),
  })
    .then((res) => res.json())
    .then((json) => console.log(json));
};

const getValue = (id) => {
  const value = document.getElementById(id).value;
  return value;
};


const handleLogin = (event) => {
    event.preventDefault();
    const username = getValue("InputUsername");
    const password = getValue("InputPassword");
    const userDetails = {
      username,
      password,
    }
    // console.log(userDetails);
    if ((username, password)) {
        fetch('https://fakestoreapi.com/auth/login',{
          method:'POST',
          headers: { "content-type": "application/json" },
          body: JSON.stringify({ username, password }),
        })
          .then((res) => res.json())
          .then((data) => {
            console.log(data);
    
            // if (data.token && data.user_id) {
            //   localStorage.setItem("token", data.token);
            //   localStorage.setItem("user_id", data.user_id);
            //   window.location.href = "index.html";
            // }
          });
      }
  };