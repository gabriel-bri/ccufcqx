<template>
  <div>
    <section class="greeting">
      <h2 class="title">
        <i class="fa-solid fa-graduation-cap"></i> Quanto Falta?
      </h2>
    </section>

    <section class="create-todo">
      <h3>CRIANDO UMA TAREFA/COMPROMISSO</h3>

      <form id="new-todo-form" @submit.prevent="addTodo">
        <h4>Que atividade você quer fazer?</h4>
        <input
          type="text"
          name="content"
          id="content"
          placeholder="Ex: Atividade de engenharia de software"
          autocomplete="off"
          v-model="input_content"
        />

        <h4>Escolha uma categoria</h4>
        <div class="options">
          <label>
            <input
              type="radio"
              name="category"
              id="category1"
              value="task"
              v-model="input_category"
            />
            <span class="bubble task"></span>
            <div>Tarefa</div>
          </label>

          <label>
            <input
              type="radio"
              name="category"
              id="category2"
              value="commitment"
              v-model="input_category"
            />
            <span class="bubble commitment"></span>
            <div>Compromisso</div>
          </label>
        </div>

        <h4>Em que dia deve ser entregue/Quando vai acontecer?</h4>
        <input type="date" name="data" id="data" v-model="input_date" />

        <h4>Quais são os detalhes?</h4>
        <input
          type="text"
          name="detail"
          id="detail"
          placeholder="Ex: Lista de exercicios sobre SOLID"
          autocomplete="off"
          v-model="input_detail"
        />

        <input type="submit" value="Adicionar" />
      </form>
    </section>

    <section class="todo-list">
      <h3>LISTA DE TAREFAS E COMPROMISSOS</h3>
      <div class="list" id="todo-list">
        <div
          v-for="todo in todos_asc"
          :class="`todo-item ${todo.done && 'done'}`"
        >
          <label>
            <input type="checkbox" v-model="todo.done" />
            <span
              :class="`bubble ${
                todo.category == 'task' ? 'task' : 'commitment'
              }`"
            ></span>
          </label>

          <div class="todo-content">
            <input type="text" v-model="todo.content" />
            <input type="text" v-model="todo.detail" />
            <input type="date" v-model="todo.date" />
          </div>

          <div class="actions">
            <button class="delete" @click="removeTodo(todo)">Apagar</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from "vue";

const todos = ref([]);
const name = ref("");

const input_content = ref("");
const input_detail = ref("");
const input_date = ref("");
const input_category = ref(null);

const todos_asc = computed(() =>
  todos.value.sort((a, b) => {
    return a.createdAt - b.createdAt;
  })
);

watch(name, (newVal) => {
  localStorage.setItem("name", newVal);
});

watch(
  todos,
  (newVal) => {
    localStorage.setItem("todos", JSON.stringify(newVal));
  },
  {
    deep: true,
  }
);

const addTodo = () => {
  if (
    input_detail.value.trim() === "" ||
    input_content.value.trim() === "" ||
    input_date.value.trim() === "" ||
    input_category.value === null
  ) {
    return;
  }

  todos.value.push({
    content: input_content.value,
    category: input_category.value,
    date: input_date.value,
    detail: input_detail.value,
    done: false,
    editable: false,
    createdAt: new Date().getTime(),
  });
};

const removeTodo = (todo) => {
  todos.value = todos.value.filter((t) => t !== todo);
};

onMounted(() => {
  name.value = localStorage.getItem("name") || "";
  todos.value = JSON.parse(localStorage.getItem("todos")) || [];
});
</script>
