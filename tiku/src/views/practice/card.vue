<template>
  <el-card shadow="always">
    <template #header>
      <span>计分板</span> <span id="score" v-text="score"></span>
    </template>
    <div>
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
    return {
      score,
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
.tag {
  margin: 5px 5px 0 0;
  cursor: pointer;
  width: 34px;
  text-align: center;
}
#score {
  font-weight: bold;
  font-size: 15px;
}
</style>