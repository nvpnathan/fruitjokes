import { createStore } from "vuex";

import jokes from './modules/jokes';
import users from './modules/users';

export default createStore({
  modules: {
    jokes,
    users,
  }
});