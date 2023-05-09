<script setup lang="ts">
import { RouterLink } from 'vue-router'
import IconArrowLeft from '@/components/icons/IconArrowLeft.vue'
</script>

<template>
  <main>
    <div class="left-side">
      <div class="header-section">
        <RouterLink to="/dashboard">
          <IconArrowLeft class="icon icon--arrow" />
        </RouterLink>
        <h1>Envoyer votre création à votre courriel</h1>
      </div>

      <p class="paragraph">
        Vous pouvez envoyer votre création à votre courriel. Vous pouvez aussi choisir de
        sauvegarder votre création pour que les autres utilisateurs la voient.
      </p>

      <form action="">
        <label for="email">Courriel</label>
        <input
          type="email"
          id="courriel"
          placeholder="123@email.com"
          minlength="0"
          maxlength="50"
          required
          autocomplete="email"
        />
        <label for="saveSound">
          Sauvegarder création
          <input type="checkbox" id="saveSound" name="saveSound" value="saveSound" checked />
        </label>

        <button class="button--primary" type="submit" @click.prevent="">Envoyer</button>
      </form>
    </div>

    <div class="right-side"></div>
  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  height: 100vh;
}

.left-side {
  flex: 1;
  background-color: var(--primary-color);
  height: calc(100vh - var(--header-height));
  padding: 5em;
}

.right-side {
  flex: 2;
  background-color: var(--secondary-color);
  height: calc(100vh - var(--header-height));

  background-color: #161a1d;
  opacity: 0.5;
  background-image: repeating-radial-gradient(circle at 0 0, transparent 0, #161a1d 31px),
    repeating-linear-gradient(#4eff6455, #4eff64);

  display: flex;
  justify-content: center;
  align-items: center;
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

.paragraph {
  margin-bottom: 2em;
}
</style>
