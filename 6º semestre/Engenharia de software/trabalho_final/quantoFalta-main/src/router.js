import { createRouter, createWebHistory } from "vue-router";

function lazyLoad(view) {
  return () => import(`./views/${view}.vue`);
}

const routes = [
  {
    path: "/",
    name: "Login",
    component: lazyLoad("Login"),
  },
  {
    path: "/home",
    name: "Home",
    component: lazyLoad("Home"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
