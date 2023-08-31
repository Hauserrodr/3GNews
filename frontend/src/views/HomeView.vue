<template>
  <main>
    <G3Header :doneLoading="doneLoading" />
    <div class='content' :style="{ opacity: doneLoading ? '1' : '0' }">
      <h1 class="header-title">
        Últimas Notícias na Mídia
      </h1>
      <div class="news-section">
        <div class="image-scroll-container">
          <div class="image-container" v-for="(newsItem, index) in newsItems" :key="index">
            <img v-lazy="newsItem.images[currentImageIndex[index]]" @click="openModal(index)" @load="imageLoaded">
            <div class="headline-container">
              <div class="headline" 
                  :class="{ scroll: needsScroll(newsItem.headline, index) }" 
                  :data-content="newsItem.headline">{{ newsItem.headline }}
              </div>
            </div>
            <h4 class="region">{{ newsItem.region }}</h4>
            <h4 class="date">{{ newsItem.day_str }}</h4>
            <div class="arrow-container">
              <button class="arrow-button" @click="prevImage(index)" aria-label="Show previous image">
                <img src="../assets/left-arrow.svg" alt="Previous Image">
              </button>

              <button class="arrow-button" @click="nextImage(index)" aria-label="Show next image">
                <img src="../assets/right-arrow.svg" alt="Next Image">
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="modal" v-if="showModal">
        <div class="modal-content">
          <span class="close" @click="closeModal">&times;</span>
          <h1>{{ newsItems[selectedNewsIndex].headline }}</h1>
          <p>Data: {{ newsItems[selectedNewsIndex].day_str }}  |   Cidade: {{ newsItems[selectedNewsIndex].region }}</p>
          <!-- Slideshow -->
          <div class="slideshow-container">
            <img :src="newsItems[selectedNewsIndex].images[modalImageIndex]" class="modal-image">
            <button class="modal-arrow-button arrow-left" @click="prevModalImage">
              <img src="../assets/left-arrow.svg" alt="Previous Image">
            </button>
            <button class="modal-arrow-button arrow-right" @click="nextModalImage">
              <img src="../assets/right-arrow.svg"  alt="Next Image">
            </button>
          </div>
          <h1> Notícias: </h1>
          <h3>{{ newsItems[selectedNewsIndex].news }}</h3>
          <br><br>
          <h1> Fontes: </h1>
          <p v-for="(link, index) in newsItems[selectedNewsIndex].news_links" :key="index">{{ link }}</p>
        </div>
      </div>
      <h1 class="user-news-title">
        Notícias dos Usuários
      </h1>
      <div class="user-news-section">
        <!-- Next 3 User News -->
        <div class="next-news" v-if="userNews && userNews.length > 1">
          <div class="news-item" v-for="(news, index) in userNews.slice(1, 4)" :key="index">
            <img class="thumbnail" :src="news.images[0]" alt="news thumbnail" @load="imageLoaded">
            <div class="text-content">
              <h5>{{ news.headline }}</h5>
              <h3>{{ news.user_name }} - {{ news.user_region }}, {{ news.day_str }}</h3>
              <p v-if="news.user_short_history">
                {{ news.user_short_history }}
                <a v-if="news.isTruncated" 
                  href="#" 
                  @click.prevent="toggleHistory(news)">Ver mais</a>
                <a v-else-if="!news.isTruncated && news.user_history.length > 500" 
                  href="#" 
                  @click.prevent="toggleHistory(news)">Ver menos</a>
              </p>

              <p v-else>
                {{ news.user_history }} 
              </p>
            </div>
          </div>
        </div>
        <!-- Most Recent User News -->
        <div class="recent-news" v-if="userNews && userNews.length > 0">
          <h3 style="font-size:2.5rem; font-style:bold;width:90%;text-transform: uppercase">{{ userNews[0].headline }}</h3>
          <h4 style="font-size:1rem; font-style:bold;">{{ userNews[0].user_name }} - {{ userNews[0].user_region }},  {{ userNews[0].day_str }}</h4>
          <img v-lazy="userNews[0].images[0]" style="width:45%; padding-right:5px" @load="imageLoaded">
          <img v-lazy="userNews[0].images[1]" style="width:45%; padding-right:5px" @load="imageLoaded">
          <img v-lazy="userNews[0].images[2]" style="width:45%; padding-right:5px" @load="imageLoaded">
          <img v-lazy="userNews[0].images[3]" style="width:45%; padding-right:5px" @load="imageLoaded">
          <h2 style="width:90%" v-if="userNews[0].user_short_history">
                {{ userNews[0].user_short_history }}
                <a v-if="userNews[0].isTruncated" 
                  href="#" 
                  @click.prevent="toggleHistory(userNews[0])">Ver mais</a>
                <a v-else-if="!userNews[0].isTruncated && userNews[0].user_history.length > 500" 
                  href="#" 
                  @click.prevent="toggleHistory(userNews[0])">Ver menos</a>
              </h2>

              <h2 style="width:90%" v-else>
                {{ userNews[0].user_history }} 
              </h2>
        </div>
      </div>
      <UserNewsForm/>
    </div>
  </main>
</template>

<script>
import G3Header from '@/components/G3Header.vue';
import UserNewsForm from '@/components/UserNewsForm.vue';

export default {
  components: { G3Header, UserNewsForm },
  data() {
    return {
      newsItems: [],
      userNews: [],
      currentImageIndex: [],
      showModal: false,
      selectedNewsIndex: null,
      modalImageIndex: 0,
      doneLoading: false,
      numberOfImagesLoaded: 0
    }
  },
  mounted() {
    // Reset numberOfImagesLoaded to 0 each time component mounts
    this.numberOfImagesLoaded = 0;
    
    let imagesToPreload = [];
    this.doneLoading = false; // Initialize it to false
    
    const preloadImage = (url) => {
      return new Promise((resolve, reject) => {
        const img = new Image();
        img.src = url;
        img.onload = resolve;
        img.onerror = reject;
      });
    };
    
    const fetchUserNews = fetch('http://localhost:7777/get_all_user_news')
      .then(response => response.json())
      .then(data => {
        this.userNews = data.reverse();
        data.forEach(newsItem => {
          newsItem.images.forEach(image => {
            imagesToPreload.push(preloadImage(image));
          });
        });
        this.userNews.forEach(news => {
          if(news.user_history.length > 500) {
            news.user_short_history = news.user_history.substring(0, 500) + '...';
            news.isTruncated = true; // Flag for truncated text
          } else {
            news.user_short_history = news.user_history;
            news.isTruncated = false; // Flag for not truncated text
          }
        });
      });
      
    const fetchAllNews = fetch('http://localhost:7777/get_all_news?news_number=6')
      .then(response => response.json())
      .then(data => {
        this.newsItems = data.reverse();
        this.currentImageIndex = Array(data.length).fill(0);
        
        // Preload images
        data.forEach(newsItem => {
          newsItem.images.forEach(image => {
            imagesToPreload.push(preloadImage(image));
          });
        });
      });

    // Wait for all fetches and image preloads to complete
    Promise.all([fetchUserNews, fetchAllNews, ...imagesToPreload])
      .then(() => {
        // Do not set doneLoading to true here.
        // It will be handled by the imageLoaded() method.
      })
      .catch(err => {
        console.error("There was an error:", err);
      });
  },
  methods: {
    imageLoaded() {
      this.numberOfImagesLoaded++;
      const totalNumberOfImages = 8;

      if (this.numberOfImagesLoaded >= totalNumberOfImages) {
        this.doneLoading = true;
      }
    },
    prevImage(index) {
      if (this.currentImageIndex[index] > 0) {
        this.currentImageIndex[index]--;
      }
    },
    toggleHistory(news) {
      if (news.isTruncated) {
        news.user_short_history = news.user_history;
        news.isTruncated = false;
      } else {
        news.user_short_history = news.user_history.substring(0, 500) + '...';
        news.isTruncated = true;
      }
    },

    nextImage(index) {
      if (this.currentImageIndex[index] < this.newsItems[index].images.length - 1) {
        this.currentImageIndex[index]++;
      } else {
        // Loop back to the first image
        this.currentImageIndex[index] = 0;
      }
    },
    needsScroll(headline, index) {
      let measureDiv = document.createElement("div");
      measureDiv.style.position = "absolute";
      measureDiv.style.left = "-9999px";
      measureDiv.style.whiteSpace = "nowrap";
      measureDiv.innerHTML = headline;
      document.body.appendChild(measureDiv);

      // Measure an actual container for more accurate width
      let actualContainer = document.querySelectorAll('.image-container')[index];
      const containerWidth = actualContainer ? actualContainer.offsetWidth : 0;

      const isOverflowing = measureDiv.offsetWidth > containerWidth;
      document.body.removeChild(measureDiv);
      return isOverflowing;
    },

    openModal(index) {
      this.showModal = true;
      this.selectedNewsIndex = index;
    },
    closeModal() {
      this.showModal = false;
      this.selectedNewsIndex = null;
      this.modalImageIndex = 0;
    },
    prevModalImage() {
      if (this.modalImageIndex > 0) {
        this.modalImageIndex--;
      }
    },

    // Function to show the next image in the modal
    nextModalImage() {
      if (this.modalImageIndex < this.newsItems[this.selectedNewsIndex].images.length - 1) {
        this.modalImageIndex++;
      }
    },
  }
}

</script>

<style>

.content {
  min-height: 100vh;
  position: relative; 
}

.header-title {
  text-align: center;
  padding-top: 6rem;
  font-size: 3rem;
}
.user-news-title {
  text-align: center;
  padding-top: 1rem;
  font-size: 3rem;
}

.region {
  position: absolute;
  top: 0;
  right: 0;
  color: black;
  font-weight: bold;
  background-color: white;
  padding: 0.5rem;
}

.date {
  position: absolute;
  top: 0;
  left: 5;
  color: black;
  font-weight: bold;
  padding: 0.5rem;
  text-shadow:
    -1px -1px 0 white,
    1px -1px 0 white,
    -1px 1px 0 white,
    1px 1px 0 white;
}

.news-content {
  padding: 1rem;
}

.news-section {
  display: flex;
  justify-content: space-between;
  padding: 0 1rem;
}

.image-scroll-container {
  display: flex;
  overflow-x: auto; /* Enable horizontal scrolling */
  width: calc(33.33% * 3); /* Display 3 items at a time */
  white-space: nowrap; /* Prevent wrapping */
}

.image-container {
  flex: 0 0 33.33%;
  position: relative;
  padding-left: 0.5rem;
}

.image-container img {
  width: 100%;
  height: auto;
}

.arrow-container {
  display: flex;
  justify-content: space-between;
  position: absolute;
  top: 50%;
  width: 100%;
  transform: translateY(-50%);
  pointer-events: none;  /* So that the container itself is not clickable */
}

.arrow-button {
  background-color: rgba(255, 255, 255, 0.5); /* Semi-transparent white background */
  border: none;
  cursor: pointer;
  padding: 0;
  width: 40px; /* Adjust to fit the circle size */
  height: 40px; /* Adjust to fit the circle size */
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%; /* Makes the button a circle */
  pointer-events: all; /* Makes the button clickable */
}

.arrow-button img {
  width: 20px;
  height: 20px;
}

.user-news-section {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
}

.recent-news {
  width: 40%;
  /* position: absolute; */
  right: 0;
}

.next-news {
  width: 50%;
  /* position: absolute; */
  left: 0;
}

.next-news div {
  border-bottom: 1px solid #ccc;
  padding: 0.5rem;
}

/*Transition of Lazy images*/
.fade-enter-active, .fade-leave-active {
  transition: opacity 1s;
}
.fade-enter, .fade-leave-active {
  opacity: 0;
}

/*Headline portion*/
.headline-container {
  position: absolute;
  bottom: 10px;
  left: 5%;
  width: 95%;
  overflow: hidden;
}

.headline {
  color: white;
  font-size: 1.3rem;
  display: inline-block;
  white-space: nowrap;
  padding-right: 20px; /* Separation between repeated headlines */
  text-shadow:
    -1px -1px 0 black,
    1px -1px 0 black,
    -1px 1px 0 black,
    1px 1px 0 black;
}

.headline.scroll::before {
  content: attr(data-content);
  position: absolute; /* Make sure this is absolute */
  top: 0; /* Align it with the top of the headline */
  left: 100%;
  white-space: nowrap;
}

.headline.scroll {
  position: relative;
  display: inline-flex;
  animation: scrollHeadline 30s linear infinite;
}


@keyframes scrollHeadline {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-100%);
  }
}

/* Modal styles */
.modal {
  display: block; /* Hidden by default */
  position: fixed; 
  z-index: 1; 
  left: 0;
  top: 0;
  width: 100%; 
  height: 100%; 
  overflow: auto; 
  background-color: rgba(0,0,0,0.4); 
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 70%;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

/* Slideshow styles */
.slideshow-container {
  position: relative;
}

.modal-image {
  width: 100%;
  height: auto;
}

.modal-arrow-button {
  position: absolute;
  top: 50%;  /* vertically center */
  transform: translateY(-50%);  /* vertically center */
  background-color: rgba(255, 255, 255, 0.5);
  border: none;
  cursor: pointer;
  padding: 0;
  width: 120px;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.arrow-left {
  left: 10px;  /* distance from the left edge */
}

.arrow-right {
  right: 10px;  /* distance from the right edge */
}

.news-item {
  display: flex;
  align-items: center;
}

.thumbnail {
  width: 20rem;  /* Adjust as needed */
  height: 20rem; /* Adjust as needed */
  margin-right: 10px;
}

.text-content {
  flex-grow: 1;
}

.text-content h5 {
  font-size: 2rem;
  padding-top: 1rem;
}
.text-content p {
  font-size: 1.3rem;
  padding-top: 2rem;
}

.loader {
  border: 5px solid #f3f3f3;
  border-radius: 50%;
  border-top: 5px solid #3498db;
  width: 50px;
  height: 50px;
  -webkit-animation: spin 2s linear infinite; /* Safari */
  animation: spin 2s linear infinite;
}

@-webkit-keyframes spin {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

</style>
