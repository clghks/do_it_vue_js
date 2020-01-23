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
    this.getTodoList()
  },
  methods: {
    getTodoList() {
      this.$http.get('/api/todos/').then((response) => {
        if (response.data !== null && response.data.length !== 0) {
          this.todoItems = response.data
        } else {
          this.todoItems = []
        }
      })
    },
    addTodo(todoItem) {
      this.$http.post('/api/todos/', {'todo': todoItem}).then((response) => {
        this.getTodoList()
      })
    },
    removeTodo(todoItem, index) {
      this.$http.delete('/api/todos/' + todoItem.id).then((response) => {
        this.getTodoList()
      })
    },
    removeAll() {
      this.$http.delete('/api/todos/removeAll/').then((response) => {
        this.getTodoList()
      })
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
