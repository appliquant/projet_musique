<script setup lang="ts">
import { RouterLink } from 'vue-router'

import SoundCard from '@/components/MusicCard.vue'

import IconArrowLeft from '@/components/icons/IconArrowLeft.vue'
import sound1 from '../assets/audio/sound1.wav'
import sound2 from '../assets/audio/sound2.wav'
import sound3 from '../assets/audio/sound3.wav'
import sound4 from '../assets/audio/sound4.wav'
import sound5 from '../assets/audio/sound5.wav'

const sounds = [
  { id: 0, soundPath: sound1, title: 'Le son 1', author: 'Bob Dyx' },
  { id: 1, soundPath: sound2, title: 'Les marionettes', author: 'Bob Dyx' },
  { id: 2, soundPath: sound3, title: 'Le son 3', author: 'Rolan Vri' },
  { id: 3, soundPath: sound4, title: 'Le son nouveau', author: 'Klof A.' },
  { id: 4, soundPath: sound5, title: 'Le vent', author: 'Crristal' }
]
</script>

<template>
  <main>
    <div class="header-section">
      <RouterLink to="/dashboard">
        <IconArrowLeft class="icon icon--arrow" />
      </RouterLink>
      <h1>Créations des autres utilisateurs</h1>
    </div>

    <!-- <SoundCard v-for="sound in sounds" :key="sound.id" :path-to-audio="sound.soundPath" /> -->
    <SoundCard v-for="sound in sounds" :key="sound.id" :sound="sound" />
    <!-- <SoundCard :sound="sounds[0]" /> -->
  </main>
</template>

<style scoped>
main {
  margin: 5em;
}

.header-section {
  display: flex;
  align-items: center;
  margin-bottom: 2em;
}

.header-section h1 {
  margin-left: 1em;
}

.icon--arrow {
  color: white;
}
</style>
