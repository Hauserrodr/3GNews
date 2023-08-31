<template>
    <div class="userNewsForm">
        <div class="popup" v-if="showPopup" @click="closePopup">
            <span>Obrigado por reportar sua notícia! Espere um minuto e atualize a página para ver sua notícia em destaque com as imagens geradas pela nossa inteligência artificial!</span>
        </div>
      <div class="first-column">
        <div class="input-fields">
          <label for="apelido" style="font-style:bold">APELIDO:</label>
          <input id="apelido" type="text" placeholder="Apelido" v-model="apelido" @input="limitNickname">
          <label for="selectedCidade" style="font-style:bold">CIDADE:</label>
          <select id="selectedCidade" v-model="selectedCidade">
            <option v-for="city in regions" :key="city.cidade">{{ city.cidade }}</option>
          </select>
          <label for="selectedBairro" style="font-style:bold">BAIRRO:</label>
          <select id="selectedBairro" v-model="selectedBairro">
            <option v-for="bairro in selectedCidadeBairros" :key="bairro">{{ bairro }}</option>
          </select>
        </div>
        <h1 class="news-header-text">NOTÍCIAS DA REGIÃO METROPOLITANA</h1>
      </div>
      <div class="second-column">
        <div class="white-rectangle">
          <h1>Seja um Repórter!</h1>
          <h2>Faça parte de nossa equipe trazendo sua notícia para nosso jornal.</h2>
        </div>
        <div class="news-input-div">
            <textarea 
                placeholder="Nos conte a SUA notícia. Como foi seu dia? Como está o tempo na sua região? Algo atípico aconteceu com você hoje?" 
                v-model="userHistory" 
                @input="limitText"
                class="news-input"></textarea>
            <span class="char-counter">{{ userHistory.length }}/1000</span>
        </div>

      </div>
      <button @click="sendData">Enviar</button>
    </div>
</template>

<script>
import regions from '@/regions.json';
import axios from 'axios';

export default {
    name: 'UserNewsForm',
    data() {
        return {
        apelido: "",
        selectedCidade: "",
        selectedBairro: "",
        userHistory: "",
        regions: regions,
        showPopup: false
        }
    },
    computed: {
        selectedCidadeBairros() {
        const city = this.regions.find(c => c.cidade === this.selectedCidade);
        return city ? city.bairros : [];
        }
    },
    methods: {
        async sendData() {
            try {
                const params = {
                    user_name: this.apelido,
                    user_region: this.selectedCidade,
                    user_microregion: this.selectedBairro,
                    user_history: this.userHistory
                };

                const response = await axios.get('http://127.0.0.1:7777/generate_user_news', { params });

                if (response.data.error) {
                    console.error('Error from server:', response.data);
                } else {
                    console.log('Data received:', response.data);
                    this.showPopup = true;  // Show the popup
                }
            } catch (error) {
                console.error('An error occurred:', error);
            }
        },
        limitNickname() {
            if (this.apelido.length > 50) {
            this.apelido = this.apelido.substring(0, 50);
            }
        },
        limitText() {
            if (this.userHistory.length > 1000) {
            this.userHistory = this.userHistory.substring(0, 1000);
            }
        },
        closePopup() {
            this.showPopup = false;
        }
    }
}
</script>

<style>
.char-counter {
  position: relative;
  float: right;
  margin-top: -50px;
  margin-right: 20px;
  color: white;
}

.userNewsForm {
  display: grid;
  grid-template-columns: 40% 60%;
  width: 90%;
  height: auto;
  background-color: #f1f1f1;
  margin: 2rem auto;
  margin-top: 10rem;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}

.first-column, .second-column {
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.first-column {
  border-right: 1px solid black; /* Changed to black for better visibility */
}

.input-fields {
  flex-basis: 30%;
  gap: 10px;
  display: flex;
  flex-direction: column;
}

.input-fields label {
  font-size: 1.5em;
  margin-bottom: 8px;
  color: black; /* Changed to black for better visibility */
  font-style: bold;
}

.input-fields input, .input-fields select {
  padding: 10px;
  border: 1px solid #ff0000; /* Bright red border */
  border-radius: 5px;
  background-color: #ff0000; /* Bright red background */
  color: white; /* White text */
  margin-bottom: 16px; /* Spacing between elements */
}

.news-header-text {
  font-size: 1.5em;
  font-weight: bold;
  color: black; /* Changed to black for better visibility */
}

.second-column {
  background-color: #ff0000; /* Bright red background */
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}

.white-rectangle {
  background-color: #ff0000; /* Bright red background */
  flex-basis: 30%;
  padding: 1rem;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  gap: 10px;
  color: white; /* White text */
}

.news-input-div {
  flex-grow: 1;
  padding: 20px;
}

.news-input {
  width: 100%;
  height: 100%;
  padding: 10px;
  border: 1px solid #ff0000; /* Bright red border */
  border-radius: 5px;
  background-color: #ff0000; /* Bright red background */
  color: white; /* White text */
  font-size: 2rem;
}

button {
  grid-column: 1 / 3;
  margin-top: 20px;
  background-color: #ff0000; /* Bright red background */
  color: white; /* White text */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  padding: 10px 20px;
  font-size: 1em;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #cc0000; /* Darker red on hover */
}

.popup {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.8); /* Semi-transparent background */
    z-index: 9999; /* Ensure it appears above other elements */
}

.popup span {
    width: 50%;
    display: block;
    background-color: #ff0000; /* Bright red background */
    padding: 20px;
    border-radius: 15px;
    font-size: 1.5em;
    color: white; /* White text */
}

</style>