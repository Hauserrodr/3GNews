import VueLazyload from 'vue-lazyload'

import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(VueLazyload, {
    preLoad: 1.3,  // Preload height ratio, default is 1.3
    error: 'path/to/error/image.png',  // Path to error image
    loading: 'path/to/loading/gif_or_image.gif',  // Path to a loading image/gif
    attempt: 1,  // Number of attempts, default is 3
    transition: "fade"
  })
app.mount('#app')
