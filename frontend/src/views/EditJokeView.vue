<template>
    <section>
      <h1>Edit joke</h1>
      <hr/><br/>
  
      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Title:</label>
          <input type="text" name="title" v-model="form.title" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Content:</label>
          <textarea
            name="content"
            v-model="form.content"
            class="form-control"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  export default defineComponent({
    name: 'EditJoke',
    props: ['id'],
    data() {
      return {
        form: {
          title: '',
          content: '',
        },
      };
    },
    created: function() {
      this.GetJoke();
    },
    computed: {
      ...mapGetters({ joke: 'stateJoke' }),
    },
    methods: {
      ...mapActions(['updateJoke', 'viewJoke']),
      async submit() {
      try {
        let joke = {
          id: this.id,
          form: this.form,
        };
        await this.updateJoke(joke);
        this.$router.push({name: 'Joke', params:{id: this.joke.id}});
      } catch (error) {
        console.log(error);
      }
      },
      async GetJoke() {
        try {
          await this.viewJoke(this.id);
          this.form.title = this.joke.title;
          this.form.content = this.joke.content;
        } catch (error) {
          console.error(error);
          this.$router.push('/dashboard');
        }
      }
    },
  });
  </script>