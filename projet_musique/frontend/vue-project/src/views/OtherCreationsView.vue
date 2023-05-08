<script setup lang="ts">
import SoundCard from '@/components/MusicCard.vue'
import sound from '../assets/audio/demo.wav'
</script>

<template>
  <main>
    <h1>Créations des autres utilisateurs</h1>

    <SoundCard :path-to-audio="sound" />
  </main>
</template>

<style scoped>
main {
  margin: 5em;
}

main > h1 {
  margin-bottom: 2em;
}

/* .music-card {
  border: 0.03em solid var(--tertiary-color);
  border-radius: 0.5em;
  padding: 1em;
}

.music-card__header {
  display: flex;
  align-items: flex-start;
  margin-bottom: 1em;
}

.music-card__author {
  font-weight: 300;
  font-size: 1em;
} */
</style>
