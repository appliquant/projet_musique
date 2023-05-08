<script setup lang="ts">
import { onMounted, ref, computed } from 'vue'
import WaveSurfer from 'wavesurfer.js'

import sound from '../assets/audio/demo.wav'
import IconPlay from '@/components/icons/IconPlay.vue'
import IconStop from '@/components/icons/IconStop.vue'

let wavesurfer: WaveSurfer | null = null

const isPlaying = ref(false)
const duration = ref(0)

const handlePlayingAudio = () => {
  if (!wavesurfer) return

  if (isPlaying.value === false) {
    isPlaying.value = true
    return wavesurfer.play()
  } else {
    isPlaying.value = false
    return wavesurfer.pause()
  }
}

onMounted(() => {
  wavesurfer = WaveSurfer.create({
    container: '#waveform',
    scrollParent: false
  })

  const audio = new Audio(sound)

  wavesurfer.load(audio)
  wavesurfer.on('ready', () => {
    duration.value = Math.round(wavesurfer?.getDuration() ?? 0)
  })
})
</script>

<template>
  <main>
    <h1>Créations des autres utilisateurs</h1>

    <div class="music-card">
      <div class="music-card__header">
        <div>
          <IconPlay v-if="!isPlaying" class="icon" @click="handlePlayingAudio" />
          <IconStop v-if="isPlaying" class="icon" @click="handlePlayingAudio" />
        </div>
        <div>
          <h1>Création #1</h1>
          <p class="music-card__author">bob dyx ● {{ duration }}s</p>
        </div>
      </div>
      <div id="waveform"></div>
    </div>
  </main>
</template>

<style scoped>
main {
  margin: 5em;
  /* display: flex; */
  /* flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  position: relative; */
}

main > h1 {
  margin-bottom: 2em;
}

.music-card {
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
}
</style>
