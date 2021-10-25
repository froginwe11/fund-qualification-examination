<template>
  <div id="main">
    <router-view style="width: 80%"></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style scoped>
#main {
  display: flex;
  justify-content: center;
}
</style>

<style>
body {
  margin: 0;
}
</style>