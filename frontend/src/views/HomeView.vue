<template>
  <section>
    <h1><b>Welcome to FruitJokes!</b></h1>
    <p>
      <video width="750" height="500" controls autoplay >
      <source src="/videos/fruitjokes.mp4" type="video/mp4"/>
     </video>
    </p>

    <div v-if="isLoggedIn" id="logout">
      <p id="logout">Click <a href="/dashboard">here</a> to view all jokes.</p>
    </div>
    <p v-else>
      <span><a href="/register">Register</a></span>
      <span> or </span>
      <span><a href="/login">Log In</a></span>
    </p>
  </section>
</template>
<script>

import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
});
</script>
