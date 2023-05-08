<template>
  <div class="container">
    <div class="left-side">
      <button class="button--primary">
        <h1>Voir autres créations</h1>
      </button>
    </div>
    <div class="right-side">
      <button class="button--secondary">
        <h1>Envoyer</h1>
      </button>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.left-side {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;

  background-color: var(--primary-color);
  height: 100vh;
}

.right-side {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--secondary-color);
  height: 100vh;
}
</style>
