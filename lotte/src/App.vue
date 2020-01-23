<template>
  <div id="app">
    <div class="lotto">
      <div v-for="number in lotto" :key="number">
        <Ball :number="number"></Ball>
      </div>
    </div>
    <button v-on:click="getLottoNumber">다시 뽑기</button>
  </div>
</template>

<script>
import {_} from 'vue-underscore';
import Ball from './components/Ball.vue'

export default {
  name: 'app',
  data () {
    return {
      lotto: []
    }
  },
  created() {
    this.getLottoNumber()
  },
  methods: {
    getLottoNumber() {
      let number = []
      _.times(45, n => number.push(n + 1))
      number = _.shuffle(number)            
      number.length = 6;                    
      number = _.sortBy(number)

      this.lotto = number
    }
  },
  components: {
    Ball: Ball
  }
}
</script>

<style scoped>
  .lotto {
    display: flex;
  }
</style>