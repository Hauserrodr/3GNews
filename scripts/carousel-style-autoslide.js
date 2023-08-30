let currentImageIndex = 0;
const apiUrl = "http://54.197.18.85:7777/get_all_user_news";

function populateMainNews(data) {
  const container = document.querySelector("#mainnews");

  data.forEach(item => {
    const userContainer = document.createElement('div');
    userContainer.className = 'mainnews-container';

    item.images.forEach(imgSrc => {
      const img = document.createElement('img');
      img.src = imgSrc;
      userContainer.appendChild(img);
    });

    container.appendChild(userContainer);
  });

  populateCarousel(data);
}

function populateCarousel(data) {
  const carouselContainer = document.querySelector("#mainnews");

  const carouselImage = document.createElement('img');
  carouselImage.className = 'mainnews-container'; // Reusing the same class
  carouselContainer.innerHTML = ''; // Clear existing content
  carouselContainer.appendChild(carouselImage);

  const images = data.reduce((acc, item) => acc.concat(item.images), []);
  carouselImage.src = images[currentImageIndex];

  currentImageIndex = (currentImageIndex + 1) % images.length;

  setTimeout(() => populateCarousel(data), 3000); // Auto slide every 3 seconds
}

// Fetch the data from the API
fetch(apiUrl)
  .then(response => response.json()) // Parse the response as JSON
  .then(data => {
    // Extract the fields you want
    const extractedData = data.map(item => ({
      day_str: item.day_str,
      headline: item.headline,
      region: item.region,
      news: item.news,
      news_source: item.news_source,
      images: item.images,
      thumbnails: item.thumbnails
    }));

    // Call the populateMainNews function with the extracted data
    populateMainNews(extractedData);
  })
  .catch(error => {
    console.error("Fetch error:", error);
  });
