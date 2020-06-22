import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../components/Home.vue';
import Feed from '../components/Feed.vue';
import Profile from '../components/Profile.vue';
import Messages from '../components/Messages.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/feed',
    name: 'Feed',
    component: Feed,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/messages',
    name: 'Messages',
    component: Messages,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;