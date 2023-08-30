function populateGallery(data) {
    const container = document.querySelector(".mainnews");
  
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
  }
  
  const apiUrl = "http://54.197.18.85:7777/get_news_for_date";
  
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
      
      // Call the populateGallery function with the extracted data
      populateGallery(extractedData);
    })
    .catch(error => {
      console.error("Fetch error:", error);
    });
  