<template>
  <div
    class="container"
    tabindex="-1"
    v-focus
    @keyup.right.capture="move(1)"
    @keyup.left.capture="move(-1)"
    @keyup.enter.capture="toggleAnswerState()"
  >
    <div class="left">
      <Question
        @changeState="changeState"
        :ref="setRef"
        v-for="(q, no) in exam"
        :class="{ 'inactive-qestion': no !== current }"
        :key="q.examId"
        :no="no + 1"
        :data="q"
      />
      <el-button-group class="btn-group" size="medium">
        <el-button @click="move(-1)" :disabled="current === 0"
          ><i class="el-icon-arrow-left" />上一题</el-button
        >
        <el-button
          @click="toggleAnswerState()"
          @keyup.enter.stop="toggleAnswerState()"
          ><i class="el-icon-view" />查看答案</el-button
        >
        <el-button @click="move(1)" :disabled="current === exam.length - 1"
          >下一题 <i class="el-icon-arrow-right"
        /></el-button>
      </el-button-group>
    </div>
    <div class="right">
      <Options style="margin-bottom: 20px" />
      <Card :data="states" @cellSelected="cellSelected" :current="current" />
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { ElMessage } from "element-plus";
import { useRoute, useRouter } from "vue-router";
import { defineComponent, computed, ref } from "vue";
import { loadJSON } from "@/utils";
import Question from "./question.vue";
import Options from "./options.vue";
import Card from "./card.vue";

export default defineComponent({
  components: { Question, Options, Card },
  setup() {
    const store = useStore();
    const route = useRoute();
    const router = useRouter();
    const flattenchapters = computed(() => store.state.flattenchapters);
    const exam = ref([]);
    const states = ref([]);
    const questions = ref([]);
    const current = ref(0);
    const count = ref(0);
    const chapter_id = route.query.chapter_id;
    const name = route.query.name;
    const examIds = route.query.examIds;

    try {
      if (chapter_id) {
        let path = flattenchapters.value[name][chapter_id];
        let data = loadJSON(path);
        exam.value = data.examDtoList;
        count.value = data.count;
        states.value = Array.from({ length: data.count }, () => null);
      }
      if (examIds) {
        exam.value = store.getters.getExamList(name, examIds);
        count.value = exam.value.length;
        states.value = Array.from({ length: count.value }, () => null);
      }
    } catch (err) {
      ElMessage.error("Oops, 人的一生就是要不断经历重新出发的过程");
      setTimeout(() => {
        router.push({ name: "home" });
      }, 1500);
    }

    return {
      exam,
      count,
      states,
      current,
      questions,
      chapter_id,
      flattenchapters,
      move(step) {
        current.value += step;
        if (current.value < 0) {
          current.value = 0;
          return;
        } else if (current.value >= exam.value.length) {
          current.value = exam.value.length - 1;
          return;
        }
      },
      toggleAnswerState() {
        questions.value[current.value].toggleAnswerState();
      },
      setRef(el) {
        questions.value.push(el);
      },
      changeState(no, state) {
        states.value[no] = state;
      },
      cellSelected(no) {
        current.value = no;
      },
    };
  },
});
</script>


<style scoped>
.container {
  margin-top: 40px;
  display: flex;
  justify-content: center;
}

.left {
  width: 70%;
  margin-right: 20px;
}
.right {
  width: 30%;
}
.inactive-qestion {
  display: none;
}
:focus {
  outline: unset !important;
}
.btn-group {
  margin-top: 15px;
  width: 100%;
  display: flex;
  justify-content: center;
  position: sticky;
  bottom: 0;
}
.btn-group > :deep(.el-button) {
  width: 33% !important;
}
</style>