<template>
    
   <div class="container">
        <div class="left-side">
            <h1>Voir autres créations</h1>
        </div>
        <div class="right-side">Envoyer</div>
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
  background-color: var(--primary-color);
  height: 100vh;
}

.right-side {
  flex: 1;
  background-color: var(--secondary-color);
  height: 100vh;

  /* background-color: #161a1d; */
  /* opacity: 0.5; */
  /* background-image: repeating-radial-gradient(circle at 0 0, transparent 0, #161a1d 31px),
    repeating-linear-gradient(#4eff6455, #4eff64); */

  /* display: flex;
  justify-content: center;
  align-items: center; */
}
</style>