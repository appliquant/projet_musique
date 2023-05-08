<script setup lang="ts">
import IconStar from '../components/icons/IconStar.vue'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()

const navigateToDashboard = () => {
  router.push('/dashboard')
}
</script>
<template>
  <main>
    <IconStar class="icon icon--start" @click="navigateToDashboard" />

    <RouterLink to="/dashboard">
      <h1>Commencer</h1>
    </RouterLink>
  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  transform: translateY(-3%);
  animation: floater 1.5s infinite;
}

.icon--start {
  width: 20em !important;
  height: 20em !important;
}

@keyframes floater {
  0% {
    transform: translateY(-3%);
    transition: ease 1s;
  }
  50% {
    transform: translateY(0%);
    transition: ease 1s;
  }
}
</style>
