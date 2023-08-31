<template>
    <div class="about">
      <G3Header :doneLoading="true" />
      <h1>This is a gallery page</h1>
    </div>
</template>
  
<script>
import G3Header from '@/components/G3Header.vue';
export default {
components: { G3Header }
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
</style>
