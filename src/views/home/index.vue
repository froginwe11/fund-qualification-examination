<template>
  <el-row class="container" :gutter="20">
    <el-col :lg="18" :md="24">
      <Options style="margin-bottom: 20px" :title="title" />
      <Chapter style="margin-bottom: 20px" @tabClick="tabClick" />
    </el-col>
    <el-col :lg="6" :md="24">
      <Donate id="donate" />
    </el-col>
  </el-row>
</template>

<script>
import Chapter from "./chapter.vue";
import Options from "./options.vue";
import Donate from "./donate.vue";
import { defineComponent, ref } from "vue";

export default defineComponent({
  components: { Chapter, Options, Donate },
  setup() {
    const title = ref("");
    return {
      title,
      tabClick(label) {
        title.value = label;
      },
    };
  },
});
</script>

<style scoped>
.container {
  margin: 10px 0;
}

#donate {
  position: sticky;
  top: 0;
}
</style>