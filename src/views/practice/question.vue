<template>
  <el-card shadow="always" tabindex="-1">
    <template #header>
      <div class="card-header">
        <span class="no">{{ no }}</span>
        <span class="no">[单选题]</span>
        <span v-html="data.content.trim().replace(/^<br \/>/, '')"></span>
      </div>
    </template>
    <el-radio-group
      v-model="chosen"
      @change="optionChosen"
      :disabled="chosen !== null"
    >
      <el-radio
        v-for="(option, idx) in data.optionList"
        :key="idx"
        :label="n2a(idx)"
        :class="{
          answer: n2a(idx) === data.answer && chosen !== null,
          chosen: chosen === n2a(idx),
        }"
      >
        <span class="option">{{ n2a(idx) }}.</span>
        <span v-html="option.trim()"></span>
      </el-radio>
    </el-radio-group>
    <div class="question-info" v-if="answerVisible">
      <el-row type="flex" class="question-row bg-gray">
        <el-col :span="5" class="ainfo"
          >正确答案： <span class="correct">{{ data.answer }}</span></el-col
        >
        <el-col :span="5" class="ainfo"
          >您的答案：
          <span :class="chosen === data.answer ? 'correct' : 'wrong'">{{
            chosen
          }}</span></el-col
        >
        <el-col :span="5">
          <span class="hide-answer" @click="hide()">收起答案</span>
        </el-col>
      </el-row>
      <el-row class="question-row" type="flex">
        <el-col :span="3" class="info">易错项：</el-col>
        <el-col
          :span="21"
          class="content"
          v-text="data.examNewStats.maxWrongAnswer"
        ></el-col>
      </el-row>
      <el-row class="question-row" type="flex" v-if="data.knowledge[0]">
        <el-col :span="3" class="info">知识点：</el-col>
        <el-col :span="21" class="content">{{
          `《${data.className}》 ${data.knowledge[0].parentChapterName} > ${data.knowledge[0].chapterName} > ${data.knowledge[0].knowLedgeName} (${data.knowledge[0].yaoQiuName})`
        }}</el-col>
      </el-row>
      <el-row class="question-row" type="flex" v-if="data.knowledge[0]">
        <el-col :span="3" class="info">教材页码：</el-col>
        <el-col :span="21" class="content">{{
          data.knowledge[0].pageNum
        }}</el-col>
      </el-row>
      <el-row class="question-row" type="flex">
        <el-col :span="3" class="info">试题难度：</el-col>
        <el-col :span="21" class="content">
          本题共被作答 <span class="wrong">{{ data.expanddoExamNum }}</span> 次
          正确率 <span class="wrong">{{ data.expandPercent }} %</span>
        </el-col>
      </el-row>
      <el-row class="question-row" type="flex">
        <el-col :span="3" class="info">参考解析：</el-col>
        <el-col
          :span="21"
          class="content"
          v-html="data.analysis.trim()"
        ></el-col>
      </el-row>
      <el-row class="question-row" type="flex" v-if="data.isOfficial">
        <el-col :span="3" class="info">试题来源：</el-col>
        <el-col :span="21" class="content" v-text="data.source"></el-col>
      </el-row>
    </div>
  </el-card>
</template>

<script>
import { defineComponent, ref, getCurrentInstance } from "vue";

const m = ["A", "B", "C", "D"];

export default defineComponent({
  props: {
    no: {
      type: Number,
    },
    data: {
      type: Object,
    },
  },
  setup(props, { emit }) {
    const chosen = ref(null);
    const answerVisible = ref(false);
    const n2a = (n) => {
      return m[n];
    };
    const { proxy } = getCurrentInstance();
    return {
      chosen,
      n2a,
      answerVisible,
      toggleAnswerState() {
        answerVisible.value = !answerVisible.value;
      },
      optionChosen() {
        proxy.$el.focus();
        emit("changeState", props.no - 1, chosen.value === props.data.answer);
        answerVisible.value = true;
      },
      hide() {
        answerVisible.value = false;
      },
    };
  },
});
</script>


<style scoped>
:deep(.el-radio-group) {
  display: flex;
  flex-direction: column;
}
.option {
  font-weight: bold;
  font-size: 13px;
  /* color: #999; */
  margin-right: 5px;
}

.no {
  font-weight: bold;
  margin-right: 3px;
}
.answer :deep(.el-radio__label) {
  color: #67c23a !important;
  font-weight: bold !important;
}
.chosen :deep(.el-radio__input.is-checked) + .el-radio__label {
  color: #f56c6c;
  font-weight: bold !important;
}

.chosen.answer :deep(.el-radio__input.is-checked) :deep(.el-radio__inner) {
  border-color: #67c23a;
  background: #67c23a;
}

.el-radio :deep(.el-radio__input.is-checked) :deep(.el-radio__inner) {
  border-color: #f56c6c;
  background: #f56c6c;
}

:deep(.el-radio__label) {
  overflow: hidden;
  text-overflow: ellipsis;
  -webkit-line-clamp: 3;
  word-wrap: break-word;
  white-space: pre-line;
}
.question-info {
  margin-top: 30px;
}

.ainfo {
  color: #999;
  font-size: 14px;
}

.info {
  color: #999;
  font-size: 14px;
  /* text-align: right; */
}

.question-row {
  margin-bottom: 15px;
}

.bg-gray {
  background-color: #f5f5f5;
  padding: 10px 5px;
}
.content {
  line-height: 24px;
  color: black;
  font-weight: 550;
}
.hide-answer {
  color: rgb(64, 158, 255);
  font-size: 14px;
  cursor: pointer;
}
:focus {
  outline: unset !important;
}

.el-radio-group > :deep(.el-radio) {
  margin-bottom: 10px;
}
</style>

<style>
.correct {
  color: #67c23a !important;
  font-size: 15px;
  font-weight: bold;
}

.wrong {
  color: #f56c6c !important;
  font-size: 15px;
  font-weight: bold;
}
</style>