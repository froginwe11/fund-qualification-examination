<template>
  <el-card shadow="always">
    <template #header>
      <span style="margin: 0; text-align: center; display: block">计分板</span>
    </template>
    <div>
      <div class="info">
        得分率：
        <span style="font-weight: bold">
          <span class="correct">{{ score }}</span>
          <span> / </span>
          <span style="color: #909399">{{ answered }}</span>
          <span> ≈ </span>
          <span :class="rate >= 60 ? 'correct' : 'wrong'"
            >{{ rate }} %</span
          ></span
        >
      </div>
      <el-tag
        v-for="(state, idx) in data"
        :key="idx"
        :type="tagType(state, idx)"
        :effect="state === null ? (idx === current ? 'dark' : 'plain') : 'dark'"
        @click="onClick(idx)"
        class="tag"
      >
        {{ idx + 1 }}
      </el-tag>
    </div>
  </el-card>
</template>

<script>
import { defineComponent, computed } from "vue";

export default defineComponent({
  props: {
    data: {
      type: Array,
    },
    current: {
      type: Number,
    },
  },
  setup(props, { emit }) {
    const score = computed(() => {
      return props.data.filter((v) => v === true).length;
    });
    const answered = computed(() => {
      return props.data.filter((v) => v !== null).length;
    });
    const rate = computed(() => {
      const r = ((score.value / answered.value) * 100).toFixed(0);
      if (isNaN(r)) {
        return 0;
      }
      return r;
    });
    return {
      score,
      answered,
      rate,
      tagType(state, idx) {
        switch (state) {
          case null:
            if (props.current === idx) {
              return "info";
            }
            return undefined;
          case true:
            return "success";
          case false:
            return "danger";
        }
      },
      onClick(no) {
        emit("cellSelected", no);
      },
    };
  },
});
</script>

<style scoped>
.info {
  text-align: center;
}
.tag {
  margin: 5px 5px 0 0;
  cursor: pointer;
  width: 40px;
  text-align: center;
}
.info > span {
  font-size: 15px;
  margin-right: 10px;
}
</style>