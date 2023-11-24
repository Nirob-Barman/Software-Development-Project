// alert()

const loadData = (defaulAlphabet) => {
  // const searchText = document.getElementById("search-box").value;
  const searchText = document
    .getElementById("search-box")
    .value.trim()
    .charAt(0)
    .toLowerCase();
  // console.log(searchText);
  // fetch(`https://www.themealdb.com/api/json/v1/1/search.php?f=a`)
  fetch(
    `https://www.themealdb.com/api/json/v1/1/search.php?f=${
      searchText ? searchText : defaulAlphabet
    }`
  )
    .then((res) => res.json())
    .then((data) => {
      //   console.log(data);
      //   console.log(data.meals);
      displayData(data.meals);
    });
};

const displayData = (data) => {
  //   console.log(data);
  document.getElementById("total-meals").innerText = data.length;

  const mealsContainer = document.getElementById("meals-container");
  data.forEach((meal) => {
    // console.log(meal);
    const card = document.createElement("div");
    card.classList.add("box");
    card.innerHTML = `
    <img class="box-img" src="${meal?.strMealThumb}" alt"">
    <h3>${meal?.strMeal}</h3>
    <p>${meal?.strInstructions.slice(0, 50)}</p>
    <button onclick="displayModal(${
      meal?.idMeal
    })" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
        Details
    </button>
    `;

    mealsContainer.appendChild(card);
  });
};

const displayModal = async (id) => {
  // console.log(id);
  // console.log("Modal");
  try {
    const response = await fetch(
      `https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`
    );
    const data = await response.json();
    // console.log(data);
  } catch (error) {
    console.log(error);
  }
};

loadData("a");
