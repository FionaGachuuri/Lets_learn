// Fetch JSON data asynchronously
fetch("https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json")
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json(); // Parse the JSON response
  })
  .then(data => {
    console.log("Fetched Data:", data); // Log the data to check it
    displaySuperheroes(data); // Call a function to update the page
  })
  .catch(error => console.error("Error fetching JSON:", error));

// Function to display superheroes on the webpage
function displaySuperheroes(data) {
  const section = document.querySelector("section");

  const heading = document.createElement("h2");
  heading.textContent = data.squadName;
  section.appendChild(heading);

  data.members.forEach(member => {
    const article = document.createElement("article");
    const name = document.createElement("h3");
    const age = document.createElement("p");
    const powers = document.createElement("p");

    name.textContent = `Name: ${member.name}`;
    age.textContent = `Age: ${member.age}`;
    powers.textContent = `Powers: ${member.powers.join(", ")}`;

    article.appendChild(name);
    article.appendChild(age);
    article.appendChild(powers);
    section.appendChild(article);
  });
}
