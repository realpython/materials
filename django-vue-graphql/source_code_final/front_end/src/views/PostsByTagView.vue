<script setup>
import PostList from "../components/PostList.vue";

import { useRoute } from "vue-router";
import { useQuery } from "@vue/apollo-composable";
import gql from "graphql-tag";

const route = useRoute();
const tag = route.params.tag;
const { result, loading, error } = useQuery(gql`
      query {
        postsByTag(
          tag: "${tag}"
        ) {
            title
            slug
            author {
              user {
                username
                firstName
                lastName
              }
            }
          }
        }
    `);
</script>

<template>
  <div v-if="loading">Loading...</div>
  <div v-else-if="error" class="warn">{{ error.message }}</div>
  <section v-else :set="(tagPosts = result.postsByTag)">
    <h2>Posts Tagged With "{{ tag }}"</h2>
    <PostList v-if="tagPosts.length > 0" :posts="tagPosts" />
    <p v-else>No posts found for this tag</p>
  </section>
</template>

<style scoped>
h2 {
  color: orange;
}
</style>
