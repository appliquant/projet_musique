import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/start',
      name: 'start',
      component: () => import("../views/StartView.vue")
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import("../views/DashboardView.vue")
    }
  ]})

export default router
