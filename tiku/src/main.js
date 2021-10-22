import {
    createApp
} from 'vue'
import store from "@/store"
import router from "@/router"
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'

const app = createApp(App)
app.directive('focus', {
    mounted(el) {
        el.focus();
    },
    beforeUpdate(el) {
        el.focus();
    },
})

app.use(ElementPlus)
app.use(store)
app.use(router)
app.mount('#app')