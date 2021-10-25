<template>
  <el-card shadow="always" class="option-card">
    <h1 style="margin-top: 0">{{ title }}</h1>
    <el-tabs type="card">
      <el-tab-pane>
        <template #label>
          <i class="el-icon-collection"></i> 模拟考试
        </template>
        <el-form :inline="true">
          <el-form-item label="试题数量">
            <el-input-number
              :min="1"
              :max="100"
              controls-position="right"
              v-model.number="examNum"
            ></el-input-number>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="doExam">开始做题</el-button>
          </el-form-item>
        </el-form>
        <el-alert
          title="在下方选中标签的试题组中，随机抽取指定数量的试题并组卷考试"
          type="warning"
          center
          show-icon
        >
        </el-alert>
      </el-tab-pane>
      <el-tab-pane>
        <template #label>
          <i class="el-icon-circle-close"></i> 易错题
        </template>
        <el-form :inline="true">
          <el-form-item label="试题数量">
            <el-input-number
              :min="1"
              :max="100"
              controls-position="right"
              v-model.number="errExamNum"
            ></el-input-number>
          </el-form-item>
          <el-form-item label="正确率低于">
            <el-input-number
              :min="1"
              :max="100"
              controls-position="right"
              v-model.number="rate"
            >
            </el-input-number>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="doErrExam">开始做题</el-button>
          </el-form-item>
        </el-form>
        <el-alert
          title="在下方选中标签的试题组中，将其所有试题按正确率正序排列后，抽取符合正确率的指定数量试题并组卷考试"
          type="warning"
          center
          show-icon
        >
        </el-alert>
      </el-tab-pane>
    </el-tabs>
  </el-card>
</template>

<script>
import { ElMessage } from "element-plus";
import { defineComponent, ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

export default defineComponent({
  props: {
    title: {
      type: String,
      default: "test",
    },
  },
  setup(props) {
    const store = useStore();
    const router = useRouter();
    const examNum = ref(100);
    const errExamNum = ref(100);
    const rate = ref(40);
    return {
      examNum,
      errExamNum,
      rate,
      doExam() {
        if (examNum.value == null) {
          ElMessage.error("试题数量不能为空");
          examNum.value = 100;
          return;
        }
        const examIds = store.getters.randomExamIds(props.title, examNum.value);
        router.push({
          name: "practice",
          query: { name: props.title, examIds },
        });
      },
      doErrExam() {
        if (errExamNum.value == null) {
          ElMessage.error("试题数量不能为空");
          errExamNum.value = 100;
          return;
        }
        if (rate.value == null) {
          ElMessage.error("正确率阈值不能为空");
          rate.value = 40;
          return;
        }
        const examIds = store.getters.randomErrExamIds(
          props.title,
          examNum.value,
          rate.value
        );
        router.push({
          name: "practice",
          query: { name: props.title, examIds },
        });
      },
    };
  },
});
</script>


<style scoped>
.option-card {
}
</style>