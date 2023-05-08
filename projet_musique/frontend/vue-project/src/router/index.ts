import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/start',
      name: 'start',
      component: () => import('../views/StartView.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue')
    },
    {
      path: '/other-creations',
      name: 'other-creations',
      component: () => import('../views/OtherCreationsView.vue')
    },
    {
      path: '/send',
      name: 'send',
      component: () => import('../views/SendView.vue')
    }
  ]
})

export default router
