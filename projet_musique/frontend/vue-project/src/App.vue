<script setup lang="ts">
import { RouterView, useRouter } from 'vue-router'
import { onMounted } from 'vue'

const router = useRouter()

onMounted(() => {
  // Naviguer vers /start quand on vient sur "/"
  router.push({ name: 'start' })
})
</script>

<template>
  <RouterView />
</template>

L
