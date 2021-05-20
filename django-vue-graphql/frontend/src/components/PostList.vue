<template>
  <div>
    <ol class="post-list">
      <li class="post" v-for="post in publishedPosts" :key="post.title">
          <span class="post__title">
            <router-link :to="`/post/${post.slug}`">{{ post.title }}: {{ post.subtitle }}</router-link>
          </span>
          <span v-if="showAuthor">
            by <AuthorLink :author="post.author" />
          </span>
          <div class="post__date">{{ displayableDate(post.publishDate) }}</div>
        <p class="post__description">{{ post.metaDescription }}</p>
        <ul>
          <li class="post__tags" v-for="tag in post.tags" :key="tag.name">
            <router-link :to="`/tag/${tag.name}`">#{{ tag.name }}</router-link>
          </li>
        </ul>
      </li>
    </ol>
  </div>
</template>

<script>
import AuthorLink from '@/components/AuthorLink'

export default {
  name: 'PostList',
  components: {
    AuthorLink,
  },
  props: {
    posts: {
      type: Array,
      required: true,
    },
    showAuthor: {
      type: Boolean,
      required: false,
      default: true,
    },
  },
  computed: {
    publishedPosts () {
      return this.posts.filter(post => post.published)
    }
  },
  methods: {
    displayableDate (date) {
      return new Intl.DateTimeFormat('en-US', { dateStyle: 'full' }).format(new Date(date))
    }
  },
}
</script>

<style>
.post-list {
  list-style: none;
}

.post {
  border-bottom: 1px solid #ccc;
  padding-bottom: 1rem;
}

.post__title {
  font-size: 1.25rem;
}

.post__description {
  color: #777;
  font-style: italic;
}

.post__tags {
  list-style: none;
  font-weight: bold;
  font-size: 0.8125rem;
}
</style>
