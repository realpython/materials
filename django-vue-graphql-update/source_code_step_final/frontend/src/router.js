import Vue from 'vue'
import VueRouter from 'vue-router'

import Post from '@/components/Post'
import Author from '@/components/Author'
import PostsByTag from '@/components/PostsByTag'
import AllPosts from '@/components/AllPosts'

Vue.use(VueRouter)

const routes = [
  { path: '/author/:username', component: Author },
  { path: '/post/:slug', component: Post },
  { path: '/tag/:tag', component: PostsByTag },
  { path: '/', component: AllPosts },
]

const router = new VueRouter({
  routes: routes,
  mode: 'history',
})
export default router
