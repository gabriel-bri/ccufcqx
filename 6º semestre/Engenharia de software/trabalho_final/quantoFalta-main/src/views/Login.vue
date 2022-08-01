<template>
  <div class="login">
    <section class="forms">
      <form class="login" @submit.prevent="loginUser">
        <i class="fa-solid fa-graduation-cap"></i>
        <input
          type="text"
          id="user"
          name="user"
          placeholder="Login"
          v-model="user"
          required
        />
        <input
          type="password"
          id="pass"
          name="pass"
          placeholder="Senha"
          v-model="pass"
          required
        />
        <input type="submit" value="Login" @click.stop.prevent="submit()" />
      </form>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: "",
      pass: "",
    };
  },
  methods: {
    loginUser() {
      const login = {
        user: this.user,
        pass: this.pass,
      };

      //limpar os campos do formulário
      this.user = "";
      this.pass = "";
    },
    submit() {
      this.$router.push("/home");
    },
  },
};
</script>

<style>
.forms {
  display: flex;
  min-height: 100vh;
}
form {
  flex: 1 1 0%;
  padding: 8rem 1rem 1rem;
}

i {
  margin-left: 50%;
  margin-bottom: 60px;
  transform: scale(5, 5);
  color: #553fde;
}

input {
  appearance: none;
  border: none;
  outline: none;
  background: none;
  display: block;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  font-size: 1.5rem;
  margin-bottom: 2rem;
  padding: 0.5rem 0rem;
}
input:not([type="submit"]) {
  opacity: 0.8;
  transition: 0.4s;
}
input:focus:not([type="submit"]) {
  opacity: 1;
}
input::placeholder {
  color: inherit;
}

form.login input:not([type="submit"]) {
  color: #2c3e50;
  border-bottom: 2px solid #2c3e50;
}
form.login input[type="submit"] {
  background-color: #553fde;
  color: #fff;
  font-weight: 700;
  padding: 1rem 2rem;
  border-radius: 0.5rem;
  cursor: pointer;
  text-transform: uppercase;
}
</style>
