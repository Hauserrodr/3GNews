<template>
    <main class='content'>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
        <div id="content">    
            <div id="G3">
                <h1>Sobre o G3</h1>
                    <article>
                        <h2> G3 - O SEU Site de Informações</h2>
                        <article>
                          <p class="poem">
                            No reino das máquinas pensantes, um sopro de criatividade emerge.<br>
                            Linhas e cores dançam em harmonia, como um poema sem palavras, guiados por circuitos eletrônicos.<br>
                            A inteligência, tão artificial quanto sublime, pinta o mundo com sua alma digital.<br>
                            Nas páginas do jornal, traços e desenhos nascem de zeros e uns,<br>
                            Revelando a magia da mente mecânica.<br>
                            Cada imagem é um espelho da mente humana,<br>
                            Refletindo sonhos e pensamentos por meio da IA,<br>
                            Um arquiteto de visões em um mundo de tinta binária.
                        </p>
                    </article>
                </article>
            </div>
            <div id="GGG">
                <h1>Sobre o G3</h1>
                <article>
                    <h2> <i>3G stands for G and G and G </i>  </h2>
                    <p>A proposta do Coletivo 3G não é apenas estética, mas também filosófica. Suas criações exploram os recantos mais profundos da experiência humana na era digital. Questões sobre identidade, privacidade, conexão e desconexão são tecidas habilmente em cada pixel. Através da combinação de elementos visuais, algoritmos e interatividade, o coletivo promove uma reflexão sobre como nós, seres humanos, nos relacionamos com a tecnologia e como ela molda nosso entendimento do mundo.</p>
                    <p>O coletivo não se contenta em apenas gerar arte visualmente cativante, mas busca também a interseção entre o ser humano e o ciberespaço. Suas obras não são meros objetos de contemplação passiva, mas convites à participação e à co-criação. A audiência é convidada a explorar, manipular e, em última instância, ser parte integrante do processo artístico. Essa abordagem transforma o espectador em colaborador, fundindo o virtual e o real em uma experiência única.</p>
                </article>
            </div>
        </div>

    </main>
</template>
<script>
export default {
    name: 'AboutContainer',
}
</script>
<style scoped>
body #call, #sendnews, #sendnewsbox, .info{
    background-color: #FFF;
}

main {
    display: flex;
    flex-direction: column;
    align-content: center;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    padding: 50px;
}
main h1, h2, article {
    color: #f00;
    text-align: justify;
}

h1 {
    font-size: 2rem
}
h2 {
    font-size: 1.5rem;
}
article {
    font-size: 1rem;
}

.content {
    background-color: #f00;
    border-radius: 11px;
    width: 90vw;
    margin: 0 auto;
    border: 10px;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-content: center;
    align-items: center;
    padding: 20px;
    gap:20px;
    justify-content: center;
}

#G3, #GGG{
    border: 3px solid #fff;
    border-radius: 10px;
    background-color: #fff;
    width: 80vw;
    display: flex;
    gap: 10px;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    margin: 10vh;
}
#quote {
    text-align: end;
}

h1 {
  transition: opacity 0.3s ease;
}

h1.fade-in {
  opacity: 1;
}

#logo {
    color: #FFF;
    flex-shrink: 0;
    text-align: center;
    font-size: 48px;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    margin: 0 auto;
}
body {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 1rem;
    background-color: #fff;
    
}

header, #footer {
    background-color: #f00;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1.5%;
}

header {
    height: 64px;
}

#footer {
    margin-top: 2%;
    height: 48px;
    flex-shrink: 0;
}

#footer p, #logo {
    color: #FFF;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

#footer p {
    font-size: 2.5vw;
}

#logo {
    text-align: center;
    font-weight: 700;
    line-height: normal;
    margin: auto;
    font-size: 3vw;
}

#menu-bt {
    color: #FFF;
    padding: 10px;
}

.material-symbols-outlined {
    font-variation-settings:
    'FILL' 0,
    'wght' 700,
    'GRAD' 0,
    'opsz' 40
}

#menu{
    display: flex;
    align-items: start;
}
menu>ul {
    list-style-type: none;
}
@media (min-width: 769px) {
    .gallery {
        background-color: #f00;
        align-items: center;
        margin: 0 auto;
    }
    .gallery h2{
        color: #FFF;
        text-align: start;
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
        gap: 20px;
        padding: 20px;
    }
}
body {
  background: #f7f7f7; /*lighter background for contrast with red*/
}

.content {
  background: #f00; 
  border-radius: 10px; /*rounded corners*/
  box-shadow: 0 5px 15px rgba(0,0,0,0.1); /* subtle shadow*/
}

h1, h2 {
  font-family: 'Playfair Display', serif; /* elegant serif font */
}

p {
  line-height: 1.6; /* Increase line-height for readability */
}

.btn {
  background: #d60404; /* darker red for buttons */
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  text-transform: uppercase;
  letter-spacing: .1em;
  transition: background .3s ease;
}

.btn:hover {
  background: #ad0404;
} 

/* Select elements for accent colors */
a, 
.menu li.active a {
  color: #d60404; 
}

a:hover {
  color: #ad0404;
}

/* Consistent spacing */
section,
.menu {
  padding: 40px;  
}

@media (max-width: 600px) {
  /* Responsive adjustments */
  .content {
    padding: 20px;
  } 
  
  h1 {
    font-size: 2rem;
  }
  
  .menu {
    padding: 20px;
  }
}
/* Fade in animation on page load */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

body {
  animation: fadeIn 0.5s ease;
}

/* Bounce animation on buttons */
.btn {
  transition: transform 0.3s ease;  
}

.btn:hover {
  transform: scale(1.1); 
}

/* Slide in menu on click */
.menu {
  transform: translateX(-100%);
  transition: transform 0.3s ease;
}

.menu.active {
  transform: translateX(0);
}

/* Smooth scrolling anchor links */
html {
  scroll-behavior: smooth; 
}

a[href^="#"] {
  color: #d60404;
}

a[href^="#"]:hover {
  color: #ad0404;  
}

/* Loading animation on page load */
.loader {
  border: 5px solid #f3f3f3;
  border-top: 5px solid #d60404;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

</style>