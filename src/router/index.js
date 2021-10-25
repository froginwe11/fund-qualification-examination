import {
    createRouter,
    createWebHashHistory,
} from "vue-router"

import Home from "@/views/home"
import Pracice from "@/views/practice"

const routes = [{
    path: "/",
    name: "home",
    component: Home,
}, {
    path: "/practice",
    name: "practice",
    component: Pracice
}]

export default createRouter({
    history: createWebHashHistory(),
    routes,
})