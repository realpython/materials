<script setup>
import AuthorLink from "./AuthorLink.vue";
import { RouterLink } from "vue-router";

const props = defineProps({
  posts: {
    type: Array,
    required: true,
  },
  showAuthor: {
    type: Boolean,
    required: false,
    default: true,
  },
});
</script>

<template>
  <ol class="post-list">
    <li class="post" v-for="post in posts" :key="post.slug">
      <RouterLink :to="{ name: 'post', params: { slug: post.slug } }">
        {{ post.title }}
      </RouterLink>
      <span v-if="showAuthor"> by <AuthorLink :author="post.author" /> </span>
    </li>
  </ol>
</template>
