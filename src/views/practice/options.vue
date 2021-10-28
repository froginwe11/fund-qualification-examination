<template>
  <el-card shadow="always" :body-style="{ padding: '5px 15px' }">
    <div>
      <el-button type="text" icon="el-icon-back" @click="backToHome"
        >返回目录</el-button
      >
    </div>
  </el-card>
</template>

<script>
import { defineComponent } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  setup() {
    const router = useRouter();
    return {
      backToHome() {
        router.push({ name: "home" });
      },
    };
  },
});
</script>


<style scoped>
.tips {
  display: flex;
  justify-content: center;
  font-size: 13px;
  color: #999;
}
</style>