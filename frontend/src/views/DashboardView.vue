<template>
  <div>
    <section>
      <h1>Add new joke</h1>
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

    <br/><br/>

    <section>
      <h1>Jokes</h1>
      <hr/><br/>

      <div v-if="jokes.length">
        <div v-for="joke in jokes" :key="joke.id" class="jokes">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>Joke Title:</strong> {{ joke.title }}</li>
                <li><strong>Content:</strong> {{ joke.content }}</li>
                <li><router-link :to="{name: 'Joke', params:{id: joke.id}}">Edit/Delete</router-link></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>

      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';
export default defineComponent({
  name: 'DashBoard',
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getJokes');
  },
  computed: {
    ...mapGetters({ jokes: 'stateJokes'}),
  },
  methods: {
    ...mapActions(['createJoke']),
    async submit() {
      await this.createJoke(this.form);
    },
  },
});
</script>