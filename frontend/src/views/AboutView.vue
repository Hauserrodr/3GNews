<template>
  <div class="content">
  <div class="about">
    <G3Header :doneLoading="true" />
    <AboutContainer/>
  </div>
  <div id="footer">
        <p> DISCLAIMER: <i>This page has artistic purporse only. Made by 3G Collective.</i></p>
  </div>
  </div>
</template>

<script>
import G3Header from '@/components/G3Header.vue';
import AboutContainer from '@/components/AboutContainer.vue';

export default {
  components: { G3Header, AboutContainer }
}
</script>


<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}

#footer {
    margin-top: 2%;
    height: 2vh;
    flex-shrink: 0;
    background-color: #f00;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1.5%;
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
</style>
