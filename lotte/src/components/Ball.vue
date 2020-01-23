<template>
    <div class="ballStyle" :style="getBallColor">
        <div class="textStyle">{{ number }}</div>
    </div>
</template>

<script>
export default {
    props: ['number'],
    computed: {
        getBallColor() {
            if (this.number <= 10) {
                return 'background-color: #fbc400;';
            } else if (this.number <= 20) {
                return 'background-color: #69c8f2;';
            } else if (this.number <= 30) {
                return 'background-color: #ff7272;';
            } else if (this.number <= 40) {
                return 'background-color: #aaa;';
            } else {
                return 'background-color: #b0d840;';
            } 
        }
    }
}
</script>

<style scoped>
.ballStyle {
    display: flex;
    width: 50px;
    height: 50px;
    border-radius: 25px;
    align-items: center;
    justify-content: center;
    margin: 5px;
}

.textStyle {
    vertical-align: middle;
    font-size: 18px;
    color: white;
    font-weight: bold;
    text-align: center;
}
</style>