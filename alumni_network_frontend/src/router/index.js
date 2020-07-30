import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../components/Home.vue';
import Feed from '../components/Feed.vue';
import Profile from '../components/Profile.vue';
import Messages from '../components/Messages.vue';
import Verify from '../components/Verify.vue';
import CompleteProfile from '../components/CompleteProfile.vue';
import Discover from '../components/Discover.vue';
import Category from '../components/Category.vue';
import User from '../components/User.vue';

Vue.use(VueRouter);

const routes = [{
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
    {
        path: '/verify',
        name: 'Verify',
        component: Verify,
    },
    {
        path: '/completeprofile',
        name: 'CompleteProfile',
        component: CompleteProfile,
    },
    {
        path: '/discover',
        name: 'Discover',
        component: Discover,
    },
    {
        path: '/category',
        name: 'Category',
        component: Category,
    },
    {
        path: '/user',
        name: 'User',
        component: User,
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;