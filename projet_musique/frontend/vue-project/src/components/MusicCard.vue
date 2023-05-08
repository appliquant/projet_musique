<script setup lang="ts">
import { onMounted, ref, onUpdated } from 'vue'
const props = defineProps<{
  /**
   * Objet contenant l'id du son et le chemin vers le son
   */
  sound: { id: number; soundPath: string; title: string; author: string }
}>()

import WaveSurfer from 'wavesurfer.js'

import IconPlay from '@/components/icons/IconPlay.vue'
import IconStop from '@/components/icons/IconStop.vue'

// Instance wavesurfer
let wavesurfer: WaveSurfer | null = null

// Id du waveform dépendant de l'id du son (unique pour chaque composant)
// Car si on a plusieurs composants, il faut que chaque waveform ait un id unique
const waveformId = `waveform-${props.sound.id}`

// Variables
const isPlaying = ref(false)
const duration = ref(0)

/**
 * Jouer le son
 */
const playAudio = () => {
  if (!wavesurfer) return

  isPlaying.value = true
  return wavesurfer.play()
}

/**
 * Arrêter le son
 */
const stopAudio = () => {
  if (!wavesurfer) return

  isPlaying.value = false
  return wavesurfer.pause()
}

/**
 * Fonction pour determiner si le son doit
 * être joué ou non
 */
const handlePlayingAudio = () => {
  if (!wavesurfer) return

  if (isPlaying.value === false) {
    return playAudio()
  } else {
    return stopAudio()
  }
}

onMounted(() => {
  // Initialiser wavesurfer
  wavesurfer = WaveSurfer.create({
    container: '#' + waveformId,
    scrollParent: false
  })

  // Charger le son
  const audio = new Audio(props.sound.soundPath)

  // Charger le son dans wavesurfer
  wavesurfer.load(audio)

  // Quand le son est prêt
  wavesurfer.on('ready', () => {
    // Afficher la durée du son
    duration.value = Math.round(wavesurfer?.getDuration() ?? 0)
  })
})
</script>
<template>
  <!-- Composant -->
  <div class="music-card">
    <div class="music-card__header">
      <div>
        <IconPlay v-if="!isPlaying" class="icon" @click="handlePlayingAudio" />
        <IconStop v-if="isPlaying" class="icon" @click="handlePlayingAudio" />
      </div>
      <div>
        <h1>{{ props.sound.title }}</h1>
        <p class="music-card__author">{{ props.sound.author }} ● {{ duration }}s</p>
      </div>
    </div>
    <div :id="waveformId"></div>
  </div>
</template>

<style scoped>
.music-card {
  border: 0.03em solid var(--tertiary-color);
  border-radius: 0.5em;
  padding: 1em;
  margin-bottom: 2em;
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
