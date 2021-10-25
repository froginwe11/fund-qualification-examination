<template>
  <el-card shadow="always">
    <el-tabs tab-position="top" :stretch="false" @tab-click="tabClick">
      <el-tab-pane
        v-for="(chapter, name) in chapters"
        :key="name"
        :label="name"
      >
        <el-tree :data="chapter" :props="props" node-key="chapter_id">
          <template #default="{ node, data }">
            <div class="custom-tree-node">
              <div class="chapter">
                <p class="chapter-name" :title="data.path">{{ node.label }}</p>
                <span class="chapter-weight" v-if="data.weight"
                  >掌握度：
                  <el-rate
                    :model-value="weightNumber(data.weight)"
                    :texts="['(了解)', '(理解)', '(掌握)']"
                    :show-text="true"
                    text-color="#999"
                    :max="3"
                    disabled
                    style="display: inline-block"
                  ></el-rate>
                </span>
              </div>
              <div class="chapter-options">
                <span class="chapter-count">{{ data.count }}</span>
                <el-button
                  :style="{
                    visibility: node.level === 1 ? 'hidden' : 'visible',
                  }"
                  class="do-exercise"
                  type="danger"
                  size="mini"
                  @click.stop="doExercise(name, data.chapter_id, node.label)"
                  >做题</el-button
                >
              </div>
            </div>
          </template>
        </el-tree>
      </el-tab-pane>
    </el-tabs>
  </el-card>
</template>

<script>
import { defineComponent, computed } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";

const props = {
  id: "chapter_id",
  label: "name",
  children: "children",
};

export default defineComponent({
  setup(_, { emit }) {
    const store = useStore();
    const router = useRouter();
    const chapters = computed(() => store.state.chapters);
    const tabClick = (tab) => {
      if (typeof tab === "string") {
        emit("tabClick", tab);
        return;
      }
      emit("tabClick", tab.props.label);
    };
    tabClick(Object.keys(chapters.value)[0]);
    return {
      props,
      chapters,
      tabClick,
      doExercise(name, chapter_id, chapter) {
        router.push({ name: "practice", query: { name, chapter, chapter_id } });
      },
      weightColor(weight) {
        switch (weight) {
          case "了解":
            return "#67C23A";
          case "理解":
            return "#E6A23C";
          case "掌握":
            return "#F56C6C";
        }
      },
      weightNumber(weight) {
        switch (weight) {
          case "了解":
            return 1;
          case "理解":
            return 2;
          case "掌握":
            return 3;
        }
      },
    };
  },
});
</script>


<style scoped>
:deep(.el-tree-node__content) {
  height: 65px;
}
.custom-tree-node {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
  padding-right: 8px;
}

.chapter {
  width: 51%;
}

.chapter-name {
  font-size: 15px;
  padding: 0;
  margin: 0;
}

.chapter-weight {
  margin-top: 8px;
  color: #999;
}
.chapter-options {
  width: 10%;
  display: flex;
  justify-content: space-between;
}
.chapter-count {
  line-height: 2;
}
.do-exercise {
  transition: 0.5s;
}

.do-exercise:hover {
  transform: translateY(-2px);
}
</style>