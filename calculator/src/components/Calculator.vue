<template>
    <div>
        <table class="calculator">
            <tr>
                <td colspan="4">
                    <div class="current">{{ current }}</div>
                </td>
            </tr>
            <tr>
                <td>
                    <button v-on:click='clear'>AC</button>
                </td>
                <td>
                    <button v-on:click='reverse'>+/−</button>
                </td>
                <td>
                    <button v-on:click='percent'>%</button>
                </td>
                <td>
                    <button v-on:click='divide'>/</button>
                </td>
            </tr>
            <tr>
                <td>
                    <button v-on:click='append("1")'>1</button>
                </td>
                <td>
                    <button v-on:click='append("2")'>2</button>
                </td>
                <td>
                    <button v-on:click='append("3")'>3</button>
                </td>
                <td>
                    <button v-on:click='multiply'>X</button>
                </td>
            </tr>
            <tr>
                <td>
                    <button v-on:click='append("4")'>4</button>
                </td>
                <td>
                    <button v-on:click='append("5")'>5</button>
                </td>
                <td>
                    <button v-on:click='append("6")'>6</button>
                </td>
                <td>
                    <button v-on:click='minus'>-</button>
                </td>
            </tr>
            <tr>
                <td>
                    <button v-on:click='append("7")'>7</button>
                </td>
                <td>
                    <button v-on:click='append("8")'>8</button>
                </td>
                <td>
                    <button v-on:click='append("9")'>9</button>
                </td>
                <td>
                    <button v-on:click='plus'>+</button>
                </td>
            </tr>
            <tr>
                <td colspan="3">
                    <button class='colspan_3' v-on:click='append("0")'>0</button>
                </td>
                <td>
                    <button v-on:click='answer'>=</button>
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
export default {
    data() {
        return {
            previous: '0',
            current: '0',
            operator: ''
        }
    },
    methods: {
        clear() {
            this.previous = '0'
            this.current = '0';
        },
        reverse() {
            this.current = parseInt(this.current) * -1
        },
        percent() {
            this.current = parseInt(this.current) / 100
        },
        setPrevious() {
            this.previous = this.current;
            this.current = '0'
        },
        divide() {
            this.operator = '/'
            this.setPrevious()
        },
        multiply() {
            this.operator = '*'
            this.setPrevious()
        },
        minus() {
            this.operator = '-'
            this.setPrevious()
        },
        plus() {
            this.operator = '+'
            this.setPrevious()
        },
        answer() {
            if (this.operator === '+') {
                this.current = parseInt(this.previous) + parseInt(this.current)
            } else if (this.operator === '-') {
                this.current = parseInt(this.previous) - parseInt(this.current)
            } else if (this.operator === '/') {
                this.current = parseInt(this.previous) / parseInt(this.current)
            } else if (this.operator === '*') {
                this.current = parseInt(this.previous) * parseInt(this.current)
            }
            this.previous = '0'
        },
        append(number){
            if (this.current === '0' || this.current === 0) {
                this.current = number
            } else {
                this.current = this.current + number
            }
        },
    }
}
</script>

<style scoped>
.calculator {
    margin: auto;
}

.current {
    font-size:60px;
    font-weight:100;
    line-height:110px;
}

button {
    width: 70px;
    height: 70px;
    float:left;
    color:black;
    font-size:24px;
    text-align:center;
}

.colspan_3 {
    width: 220px;
    height: 70px;
    padding: 0px;
}
</style>