<template>
  <el-card shadow="always">
    <div class="container">
      <el-image
        style="width: 100px; height: 100px; margin: 5px"
        :src="coffee"
        fit="contain"
      ></el-image>
      <h4 style="text-align: center">
        祝你考试顺利呀 苟富贵勿相忘<br />请作者喝杯咖啡
      </h4>
      <el-image
        style="width: 200px; height: 200px; margin: 5px"
        :src="wcpay"
        fit="contain"
      ></el-image>
      <el-image
        style="width: 200px; height: 200px; margin: 5px"
        :src="alipay"
        fit="contain"
      ></el-image>
      <div>
        <el-link
          href="https://gitee.com/nbody1996/fund-qualification-examination"
          target="_blank"
          type="danger"
          >项目代码地址</el-link
        >
      </div>
    </div>
  </el-card>
</template>

<script>
import { defineComponent } from "vue";

import wcpay from "@/assets/donate/wcpay.jpg";
import alipay from "@/assets/donate/alipay.jpg";
import coffee from "@/assets/donate/coffee.png";

export default defineComponent({
  setup() {
    return {
      wcpay,
      alipay,
      coffee,
    };
  },
});
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
</style>
