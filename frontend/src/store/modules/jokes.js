import axios from 'axios';

const state = {
  jokes: null,
  joke: null
};

const getters = {
  stateJokes: state => state.jokes,
  stateJoke: state => state.joke,
};

const actions = {
  async createJoke({dispatch}, joke) {
    await axios.post('api/v1/jokes', joke);
    await dispatch('getJokes');
  },
  async getJokes({commit}) {
    let {data} = await axios.get('api/v1/jokes');
    commit('setJokes', data);
  },
  async viewJoke({commit}, id) {
    let {data} = await axios.get(`api/v1/joke/${id}`);
    commit('setJoke', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateJoke({}, joke) {
    await axios.patch(`api/v1/joke/${joke.id}`, joke.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteJoke({}, id) {
    await axios.delete(`api/v1/joke/${id}`);
  }
};

const mutations = {
  setJokes(state, jokes){
    state.jokes = jokes;
  },
  setJoke(state, joke){
    state.joke = joke;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};