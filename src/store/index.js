import {
    createStore
} from 'vuex'

import {
    getChapters,
    flattenChapters,
    getExamList,
} from '@/utils'

export default createStore({
    state() {
        const chapters = getChapters()
        const flattenchapters = flattenChapters(chapters)
        const examList = getExamList()
        return {
            chapters,
            flattenchapters,
            examList,
        }
    },
    getters: {
        randomErrExamIds: (state) => (name, num, rate) => {
            let examList = Object.entries(state.examList[name])
            let examIds = examList.filter(([, v]) => {
                return Number.parseInt(v.expandPercent) <= rate
            }).map(([, v]) => v.examId).slice(0, num)
            for (let i = 0; i < 5; i++) {
                examIds.sort(() => 0.5 - Math.random())
            }
            return examIds.join(",")
        },
        randomExamIds: (state) => (name, num) => {
            let examIds = Object.keys(state.examList[name])
            for (let i = 0; i < 5; i++) {
                examIds.sort(() => 0.5 - Math.random())
            }
            return examIds.slice(0, num).join(",")
        },
        getExamList: (state) => (name, ids) => {
            const result = []
            const examList = state.examList[name]
            for (let i of ids.split(",")) {
                result.push(examList[i])
            }
            return result
        }
    }
})