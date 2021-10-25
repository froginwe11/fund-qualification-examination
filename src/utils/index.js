export function flattenChapters(chapters) {
    let result = {}
    for (let [
            name,
            subject
        ] of Object.entries(chapters)) {
        result[name] = {}
        for (let z of subject) {
            for (let j of z.children) {
                result[name][j.chapter_id] = j.path
                for (let k of j.children) {
                    result[name][k.chapter_id] = k.path
                }
            }
        }
    }
    return result
}

export function getChapters() {
    const files = require.context("@/assets/tiku", false, /.json$/);
    const chapters = {};
    files.keys().forEach((k) => {
        let name = /.\/(.*?).json/.exec(k)[1]
        if (name.endsWith("_题库")) {
            return
        }
        name = name.replace("_", "(") + ")"
        chapters[name] = files(k);
    });
    return chapters
}

export function getExamList() {
    const files = require.context("@/assets/tiku", false, /_题库.json$/);
    const examList = {};
    files.keys().forEach((k) => {
        let name = /.\/(.*?).json/.exec(k)[1]
        name = name.replace("_题库", "").replace("_", "(") + ")"
        examList[name] = files(k);
    });
    return examList
}

export function loadJSON(path) {
    return require(`@/assets/tiku/${path}`)
}