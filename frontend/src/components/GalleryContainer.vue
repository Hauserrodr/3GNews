<!-- GalleraContainer.vue -->
<template>
    <div class="content">
        <div class="gallery">
        <h2 class="title"> Galeria de Notícias </h2><br />
        <div class="gallery-container">
            <!-- Gallery items will be rendered here -->
            <div
            v-for="(item, index) in extractedData"
            :key="index"
            class="user-container"
            >
            <img v-for="imgSrc in item.images" :src="imgSrc" />
            </div>
        </div><br />
        </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        extractedData: [],
      };
    },
    mounted() {
      this.fetchData();
    },
    methods: {
      async fetchData() {
        const apiUrl = "http://localhost:7777/get_all_user_news";
        try {
          const response = await fetch(apiUrl);
          const data = await response.json();
          this.extractedData = data.map((item) => ({
            day_str: item.day_str,
            headline: item.headline,
            region: item.region,
            news: item.news,
            news_source: item.news_source,
            images: item.images,
            thumbnails: item.thumbnails,
          }));
        } catch (error) {
          console.error("Fetch error:", error);
        }
      },
    },
  };
  </script>
  
<style scoped>
.content{
    position: flex;
}
.gallery {
width: 92%;
text-align:center;
align-content: center;
align-items: center;
}
.gallery h2{
    color: #FFF;
    text-align: center;
    align-content: center;
    width: 25%;
    font-size: 7vw;
    padding: 20px;
}
.title {
    text-align: center;
    width: 100%;
}

.gallery-container {
position: relative;
}
.overlay {
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.5);
display: none;
justify-content: center;
align-items: center;
}

#enlargedImg {
max-width: 80%;
max-height: 80%;
object-fit: contain;
}

@media (max-width: 768px) {
/* You can add styles specific to screens smaller than 768px here */
.gallery {
    background-color: #f00;
    align-items: center;
    margin: 0 auto;
}
.gallery h2{
    color: #FFF;
    text-align: center;
    align-content: center;
    width: 25%;
    font-size: 7vw;
    padding: 20px;
}
.gallery-container {

    display: grid;
    grid-template-columns: 1fr;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
}
.user-container {
    display: grid;
    grid-template-columns: 1fr;
    justify-content: space-evenly;
    justify-items: center;
    align-content: space-evenly;
    align-items: center;
    margin: 0 auto
}

.user-container>img {
    max-width: 90%;
    max-height: 90%;
    gap: 20px;
    margin: 0 auto;
    border: #FFF solid 2px;

}
}


@media (min-width: 769px) {
    .gallery {
        background-color: #f00;
        align-items: center;
        margin: 0 auto;
    }
    .title{
        text-align:center;
        align-content: center;
        align-items: center;
    }
    .gallery h2{
        margin-top: 20hv;
        color: #FFF;
        text-align: center;
        width: 25%;
        font-size: 64px;
        padding: 20px;
    }
    .gallery-container {
        display: grid;
        grid-template-columns: 1fr;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
    }
    .user-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        justify-content: space-evenly;
        justify-items: center;
        align-content: space-evenly;
        align-items: center;
        margin: 0 auto
    }
    
    img {
        max-width: 90%;
        max-height: 90%;
    }
}

</style>
