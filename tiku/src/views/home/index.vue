<template>
  <div class="container">
    <Options style="margin-bottom: 20px; min-height: 300px" />
    <div class="bottom">
      <Chapter style="width: 80%" />
      <Donate id="donate" />
    </div>
  </div>
</template>

<script>
import Chapter from "./chapter.vue";
import Options from "./options.vue";
import Donate from "./donate.vue";
import { defineComponent } from "vue";

export default defineComponent({
  components: { Chapter, Options, Donate },
  setup() {},
});
</script>

<style scoped>
.container {
  display: flex;
  margin: 20px 10px;
  flex-direction: column;
}

.container .bottom {
  display: flex;
}

#donate {
  width: 20%;
  margin-left: 20px;
  max-height: 500px;
  position: sticky;
  top: 0;
}
</style>