<template>
  <div id="app">
    <TodoHeader></TodoHeader>
    <TodoInput v-on:addTodo="addTodo"></TodoInput>
    <TodoList v-on:removeTodo="removeTodo" v-bind:propsdata="todoItems"></TodoList>
    <TodoFooter v-on:removeAll="removeAll"></TodoFooter>
  </div>
</template>

<script>
import TodoHeaderVue from './components/TodoHeader.vue'
import TodoInputVue from './components/TodoInput.vue'
import TodoListVue from './components/TodoList.vue'
import TodoFooterVue from './components/TodoFooter.vue'

export default {
  data() {
    return {
      todoItems: []
    }
  },
  created() {
    if (localStorage.length > 0) {
      for (var i=0; i<localStorage.length; i++) {
        var key = localStorage.key(i);
        if (key !== "loglevel:webpack-dev-server") {
            this.todoItems.push(key);
        }
      }
    }
  },
  methods: {
    addTodo(todoItem) {
      localStorage.setItem(todoItem, todoItem);
      this.todoItems.push(todoItem);
    },
    removeTodo(todoItem, index) {
      localStorage.removeItem(todoItem)
      this.todoItems.splice(index, 1)
    },
    removeAll() {
      localStorage.clear();
      this.todoItems = [];
    }
  },
  components: {
    "TodoHeader": TodoHeaderVue,
    "TodoInput": TodoInputVue,
    "TodoList": TodoListVue,
    "TodoFooter": TodoFooterVue
  }
}
</script>

<style>
  body {
    text-align: center;
    background: #f6f6f8
  }

  input {
    border-style: groove;
    width: 200px;
  }

  button {
    border-style: groove;
  }
  
  .shadow {
    box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.03)
  }
</style>