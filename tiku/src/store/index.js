import {
    createStore
} from 'vuex'

import {
    getChapters,
    flattenChapters
} from '@/utils'

// import {
//     ElLoading
// } from 'element-plus'
// const loading = ElLoading.service({
//     lock: true,
//     text: '拼命地加载数据中，先起来站会儿吧～',
//     spinner: 'el-icon-loading',
//     background: 'rgba(0, 0, 0, 0.7)',
// })
// loading.close()

export default createStore({
    state() {
        const chapters = getChapters()
        const flattenchapters = flattenChapters(chapters)
        return {
            chapters,
            flattenchapters
        }
    },
})