import { createRouter, createWebHistory } from "vue-router";
import AuthorView from "../views/AuthorView.vue";
import AllPostsView from "../views/AllPostsView.vue";
import PostView from "../views/PostView.vue";
import PostsByTagView from "../views/PostsByTagView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "posts",
      component: AllPostsView,
    },
    {
      path: "/author/:username",
      name: "author",
      component: AuthorView,
    },
    {
      path: "/post/:slug",
      name: "post",
      component: PostView,
    },
    {
      path: "/tag/:tag",
      name: "tag",
      component: PostsByTagView,
    },
  ],
});

export default router;
