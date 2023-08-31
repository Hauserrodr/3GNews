<template>
  <div>
    <div class="red-bar">
      <h3 v-if="doneLoading" class="text">g3</h3>
      <div v-if="!doneLoading" class="loading-container">
        <span class="loader"></span>
        <p>Carregando, por favor aguarde...</p>
      </div>
      <!-- Menu button -->
      <div class="menu-button" @click="toggleMenu">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>
      <!-- Menu options -->
      <div v-if="showMenu" class="menu-options">
        <div @click="goTo('home')">Home</div>
        <div @click="goTo('gallery')">Gallery</div>
        <div @click="goTo('about')">About</div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  name: 'G3Header',
  props: {
    doneLoading: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      showMenu: false,
    };
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  methods: {
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
    goTo(routeName) {
      this.router.push({ name: routeName });
      this.toggleMenu();
    }
  }
};
</script>

<style scoped>
.loading-container {
  display: flex;
  color: white;
  font-style: bold;
  font-size: 1.5rem;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.loader {
  border: 5px solid #f3f3f3;
  border-radius: 50%;
  border-top: 5px solid #3498db;
  width: 50px;
  height: 50px;
  -webkit-animation: spin 2s linear infinite;
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

.red-bar {
  background-color: red;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 10vh;
  width: 100%;
  position: fixed;
  top: 0;
  z-index: 1000;
}

.text {
  color: white;
  font-size: 6vh;
  font-weight: bold;
}

.menu-button {
  position: absolute;
  top: 4vh;
  right: 3vh;
  cursor: pointer;
}

.bar {
    background-color: white;
    height: 0.6vh;
    margin: 1vh;
    width: 6vh;
  }

.menu-options {
  position: absolute;
  top: 10vh;
  right: 2vh;
  background-color: #fff;
  border: 1px solid #ccc;
  z-index: 1001;
}

.menu-options div {
  padding: 8px 16px;
  cursor: pointer;
}

/* Media Query for small screens */
@media (max-width: 600px) {
  .red-bar {
    flex-direction: column;
    height: 10vh;
  }

  .text {
    font-size: 6vh;
  }

  .menu-button {
    top: 2vh;
    right: 2vh;
  }

  .menu-options {
    top: 10vh;
    right: 1vh;
  }
}

/* Media Query for larger screens */
@media (min-width: 1200px) {
  .text {
    font-size: 7vh;
  }
  .menu-button {
    top: 20%;
    right: 2vh;
  }

  .menu-options {
    right: 4vh;
  }
}

</style>