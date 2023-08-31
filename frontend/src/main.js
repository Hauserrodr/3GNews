import VueLazyload from 'vue-lazyload'

import './assets/main.css'
import errorImg from './assets/error.svg'
import loadingImg from './assets/load-loading.gif'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(VueLazyload, {
    preLoad: 1.3,
    error: errorImg,
    loading: loadingImg,
    attempt: 3,  // Number of attempts, default is 3
    transition: "fade"
  })
app.mount('#app')
