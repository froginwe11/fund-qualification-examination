<template>
  <el-card shadow="always">
    <template #header>
      <div>
        <el-button type="text" icon="el-icon-back" @click="backToHome"
          >返回目录</el-button
        >
      </div>
    </template>
    <div style="display: flex; justify-content: center; margin-bottom: 5px">
      <el-tag type="success" size="mini">TIPS</el-tag>
    </div>
    <span class="tips">
      键盘快捷键:
      <el-tag type="info" size="mini" style="margin-right: 3px"
        >&gt; 下一题</el-tag
      >
      <el-tag type="info" size="mini" style="margin-right: 3px"
        >&lt; 上一题</el-tag
      >
      <el-tag type="info" size="mini">Enter 显示答案</el-tag>
    </span>
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
  font-size: 13px;
  color: #999;
}
</style>