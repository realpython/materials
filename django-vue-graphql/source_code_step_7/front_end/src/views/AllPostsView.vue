<script setup>
import PostList from "../components/PostList.vue";

const { result, loading, error } = {
  error: { message: "No connection to the GraphQL API yet." },
};
</script>

<template>
  <h2>Recent Posts</h2>
  <div v-if="loading">Loading...</div>
  <div v-else-if="error" class="warn">{{ error.message }}</div>
  <PostList v-else :posts="result.allPosts" />
</template>

<style scoped>
h2 {
  color: blue;
}
</style>
