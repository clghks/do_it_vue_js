<template>
   <div>
       <button v-on:click="setLocation('seoul')">서울</button>
       <button v-on:click="setLocation('daejeon')">대전</button>
       <button v-on:click="setLocation('daegu')">대구</button>
       <button v-on:click="setLocation('busan')">부산</button>
   </div>
</template>

<script>
export default {
   methods: {
       setLocation(location) {
           this.$emit('updateWeather', location);
       }
   }
}
</script>

<style scoped>
button{
   width: 77px;
   height: 52px;
   background: #7185ec;
   color: #fff;
   font-size: 20px;
   border-radius: 4px;
   text-align: center;
}
</style>
