<template>
    <div v-if="joke">
      <p><strong>Title:</strong> {{ joke.title }}</p>
      <p><strong>Content:</strong> {{ joke.content }}</p>
      <p><strong>Author:</strong> {{ joke.author.username }}</p>
  
      <div v-if="user.id === joke.author.id">
        <p><router-link :to="{name: 'EditJoke', params:{id: joke.id}}" class="btn btn-primary">Edit</router-link></p>
        <p><button @click="removeJoke()" class="btn btn-secondary">Delete</button></p>
      </div>
    </div>
  </template>
  
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  export default defineComponent({
    name: 'Joke',
    props: ['id'],
    async created() {
      try {
        await this.viewJoke(this.id);
      } catch (error) {
        console.error(error);
        this.$router.push('/dashboard');
      }
    },
    computed: {
      ...mapGetters({ joke: 'stateJoke', user: 'stateUser'}),
    },
    methods: {
      ...mapActions(['viewJoke', 'deleteJoke']),
      async removeJoke() {
        try {
          await this.deleteJoke(this.id);
          this.$router.push('/dashboard');
        } catch (error) {
          console.error(error);
        }
      }
    },
  });
  </script>